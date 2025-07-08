from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import StructType
import sys
import traceback
from typing import Optional

class BaseTopicProcessor:
    topic: str
    schema: StructType

    def __init__(self, spark: SparkSession):
        self.spark = spark

    def process(self) -> Optional[DataFrame]:
        kafka_df = self.spark.readStream \
            .format("kafka") \
            .option("kafka.bootstrap.servers", "kafka1:29092") \
            .option("subscribe", self.topic) \
            .option("startingOffsets", "earliest") \
            .load()
        parsed_df = kafka_df.selectExpr("CAST(value AS STRING) as json") \
            .select(from_json(col("json"), self.schema).alias("data")) \
            .select("data.*")
        return parsed_df

    def write_to_hdfs(self, df: DataFrame, epoch_id: int) -> None:
        try:
            row_count = df.count()
            if row_count > 0:
                hdfs_path_json = f"hdfs://namenode:9000/data/kafka_data/{self.topic}_json"
                df.write.mode("append").json(hdfs_path_json)
        except Exception as e:
            print(f"[ERROR] Error writing to HDFS for {self.topic}: {e}")
            traceback.print_exc(file=sys.stdout) 