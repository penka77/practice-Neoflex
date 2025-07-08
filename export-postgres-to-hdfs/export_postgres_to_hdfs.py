from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .master("spark://spark-master:7077")
    .config("spark.jars", "/jars/postgresql-42.7.7.jar")
    .getOrCreate()
)
jdbc_url = "jdbc:postgresql://postgres:5432/postgres_db"
properties = {
    "user": "postgres_user",
    "password": "postgres_password",
    "driver": "org.postgresql.Driver"
}

tables = [
    ("data.cards", "data_cards"),
    ("data.banks", "data_banks"),
    ("data.peoples", "data_peoples"),
    ("data.organizations", "data_organizations"),
    ("data.mcc", "data_mcc"),
]

for table, folder in tables:
    print(f"Экспорт {table} -> {folder}")
    df = spark.read.jdbc(url=jdbc_url, table=table, properties=properties)
    df.write.mode("overwrite").parquet(f"hdfs://namenode:9000/user/hadoop/{folder}")
    print(f"Готово: {folder}")

spark.stop()
print("[COMPLETE] Экспорт завершён!") 