from pyspark.sql import SparkSession
from functools import reduce
from amur_processor import AmurProcessor
from neva_processor import NevaProcessor
from ob_processor import ObProcessor
from volga_processor import VolgaProcessor
from yenisei_processor import YeniseiProcessor

TOPIC_PATHS = {
    'amur': 'hdfs://namenode:9000/data/kafka_data/amurTopic/*.parquet',
    'neva': 'hdfs://namenode:9000/data/kafka_data/nevaTopic/*.parquet',
    'ob': 'hdfs://namenode:9000/data/kafka_data/obTopic/*.parquet',
    'volga': 'hdfs://namenode:9000/data/kafka_data/volgaTopic/*.parquet',
    'yenisei': 'hdfs://namenode:9000/data/kafka_data/yeniseiTopic/*.parquet',
}

PROCESSORS = [
    AmurProcessor,
    NevaProcessor,
    ObProcessor,
    VolgaProcessor,
    YeniseiProcessor
]

def main():
    spark = SparkSession.builder.appName("MergeKafkaParquetOOP").getOrCreate()
    dfs = []
    for proc_cls, topic in zip(PROCESSORS, TOPIC_PATHS):
        processor = proc_cls(spark, TOPIC_PATHS[topic])
        dfs.append(processor.process())
    result = reduce(lambda a, b: a.unionByName(b, allowMissingColumns=True), dfs)
    result.show(truncate=False)
    result.write.mode("overwrite").parquet("hdfs://namenode:9000/data/kafka_data/merged_result.parquet")

if __name__ == "__main__":
    main() 