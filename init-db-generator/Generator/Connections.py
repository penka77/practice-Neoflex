import psycopg2
from psycopg2._psycopg import connection


class Connections:
    def __init__(self):
        self.connection = self.__init_connection(
            "postgres_user", "postgres_password", "postgres_container", "5432","retail"
        )
        self.connection_metrics = self.__init_connection(
            "postgres_user", "postgres_password", "postgres_container", "5432","metrics"
        )

    def __init_connection(self, user: str, password: str, host: str, port: str, database: str) -> connection:
        return psycopg2.connect(
            user=user,
            password=password,
            host=host,
            port=port,
            database=database
        )

    def commit(self):
        self.connection.commit()
        self.connection_metrics.commit()

    def close(self):
        self.connection.close()
        self.connection_metrics.close()