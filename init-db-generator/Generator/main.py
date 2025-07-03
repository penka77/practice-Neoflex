import datetime
import time

from Connections import Connections
from Cursors import Cursors
from RecordInformation import RecordInformation

if __name__=="__main__":
    connections = Connections()
    cursors = Cursors(connections)
    record_information = RecordInformation()

    start = time.time()
    record_information.record(cursors)
    connections.commit()
    print(time.time() - start)
    
    cursors.close()
    connections.close()