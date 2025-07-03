from Connections import Connections


class Cursors:
    def __init__(self, connections: Connections):
        self.cursor = connections.connection.cursor()
        self.cursor_metrics = connections.connection_metrics.cursor()

    def close(self):
        self.cursor.close()
        self.cursor_metrics.close()