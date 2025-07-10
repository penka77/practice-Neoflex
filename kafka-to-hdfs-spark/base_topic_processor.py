from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import StructType
import sys
import traceback
from typing import Optional

class BaseTopicProcessor:
    def __init__(self, spark: SparkSession, topic: str, schema: StructType):
        self.spark = spark
        self.topic = topic
        self.schema = schema
        # Маппинг топиков к правильным именам папок
        self.topic_folder_mapping = {
            "amur_topic": "amurTopic",
            "neva_topic": "nevaTopic", 
            "ob_topic": "obTopic",
            "volga_topic": "volgaTopic",
            "yenisei_topic": "yeniseiTopic"
        }

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
                folder_name = self.topic_folder_mapping.get(self.topic, self.topic)
                hdfs_path_parquet = f"hdfs://namenode:9000/data/kafka_data/{folder_name}"
                print(f"[DEBUG] topic={self.topic}, folder_name={folder_name}, hdfs_path={hdfs_path_parquet}")
                df.write.mode("append").parquet(hdfs_path_parquet)
                print(f"[INFO] Successfully wrote {row_count} rows to {hdfs_path_parquet}")
        except Exception as e:
            print(f"[ERROR] Error writing to HDFS for {self.topic}: {e}")
            traceback.print_exc(file=sys.stdout) 