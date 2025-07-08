from pyspark.sql import SparkSession
from amur_topic_processor import AmurTopicProcessor
from neva_topic_processor import NevaTopicProcessor
from ob_topic_processor import ObTopicProcessor
from volga_topic_processor import VolgaTopicProcessor
from yenisei_topic_processor import YeniseiTopicProcessor
from base_topic_processor import BaseTopicProcessor
from typing import List
import sys
import traceback

def create_spark_session() -> SparkSession:
    return SparkSession.builder \
        .appName("KafkaToHDFS") \
        .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.1") \
        .getOrCreate()

def main() -> None:
    try:
        spark = create_spark_session()
        processors: List[BaseTopicProcessor] = [
            AmurTopicProcessor(spark),
            NevaTopicProcessor(spark),
            ObTopicProcessor(spark),
            VolgaTopicProcessor(spark),
            YeniseiTopicProcessor(spark)
        ]
        for processor in processors:
            parsed_df = processor.process()
            if parsed_df is None:
                continue
            parsed_df.writeStream \
                .foreachBatch(lambda df, epoch_id: processor.write_to_hdfs(df, epoch_id)) \
                .outputMode("append") \
                .trigger(processingTime="10 seconds") \
                .start()
        spark.streams.awaitAnyTermination()
    except Exception as e:
        print(f"[ERROR] Main error: {e}")
        traceback.print_exc(file=sys.stdout)

if __name__ == "__main__":
    main() 