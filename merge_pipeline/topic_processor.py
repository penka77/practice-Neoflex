from pyspark.sql import DataFrame
from pyspark.sql.functions import col, explode, lit

class TopicProcessor:
    def __init__(self, spark, parquet_path: str):
        self.spark = spark
        self.parquet_path = parquet_path

    def read(self) -> DataFrame:
        return self.spark.read.parquet(self.parquet_path)

    def process(self) -> DataFrame:
        raise NotImplementedError("process() должен быть реализован в наследнике") 