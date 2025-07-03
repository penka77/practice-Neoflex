from BanksCheque.AmurBank.AmurCheque import AmurCheque
from BanksCheque.BankCheque import BankCheque
from BanksCheque.NevaBank.NevaCheque import NevaCheque
from BanksCheque.ObBank.ObCheque import ObCheque
from BanksCheque.Purchase import Purchase
from BanksCheque.VolgaBank.VolgaCheque import VolgaCheque
from BanksCheque.YeniseiBank.YeniseiCheque import YeniseiCheque


class BankFactory:
    @staticmethod
    def create_bank(purchase: Purchase) -> BankCheque:
        if purchase.terminal["bank"] == "АМУР":
            return AmurCheque(purchase)
        if purchase.terminal["bank"] == "ВОЛГА":
            return VolgaCheque(purchase)
        if purchase.terminal["bank"] == "ОБЬ":
            return ObCheque(purchase)
        if purchase.terminal["bank"] == "НЕВА":
            return NevaCheque(purchase)
        if purchase.terminal["bank"] == "ЕНИСЕЙ":
            return YeniseiCheque(purchase)