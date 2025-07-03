from time import sleep
from confluent_kafka import Producer

from BanksCheque.AmurBank.AmurCheque import AmurCheque
from BanksCheque.BankCheque import BankCheque
from BanksCheque.BankFactory import BankFactory
from BanksCheque.NevaBank.NevaCheque import NevaCheque
from BanksCheque.ObBank.ObCheque import ObCheque
from BanksCheque.Purchase import Purchase
from BanksCheque.VolgaBank.VolgaCheque import VolgaCheque
from BanksCheque.YeniseiBank.YeniseiCheque import YeniseiCheque
from Connections import Connections
from Cursors import Cursors


class RecordCheque:
    def __init__(self):
        self.connections = Connections()
        self.cursors = Cursors(self.connections)
        self.__set_cursors()

    def stream_cheque(self):
        producer = Producer({'bootstrap.servers': 'kafka1:19092'})
        try:
            while True:
                producer.poll(0)
                purchase = Purchase()
                bank_cheque = BankFactory.create_bank(purchase)
                producer.produce(bank_cheque.topic, str(bank_cheque.cheque), callback=RecordCheque.delivery_report)
                sleep(0.4)
        except Exception as e:
            print(e)
            producer.flush()
            self.cursors.close()
            self.connections.close()

    def __set_cursors(self):
        Purchase.set_cursors(self.cursors)
        BankCheque.set_cursors(self.cursors)
        AmurCheque.set_bank_id()
        NevaCheque.set_bank_id()
        ObCheque.set_bank_id()
        VolgaCheque.set_bank_id()
        YeniseiCheque.set_bank_id()

    @staticmethod
    def delivery_report(err, msg):
        """ Called once for each message produced to indicate delivery result.
            Triggered by poll() or flush(). """
        if err is not None:
            print('Message delivery failed: {}'.format(err))
        else:
            print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

