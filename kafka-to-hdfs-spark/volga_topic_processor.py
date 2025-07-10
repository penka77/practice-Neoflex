from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType, ArrayType
from base_topic_processor import BaseTopicProcessor

class VolgaTopicProcessor(BaseTopicProcessor):
    def __init__(self, spark):
        topic = "volga_topic"
        schema = StructType([
            StructField("bank_id", StringType(), True),
            StructField("client_info", StructType([
                StructField("card", StringType(), True),
                StructField("bank", StringType(), True),
                StructField("pay_system", StringType(), True)
            ]), True),
            StructField("market_info", StructType([
                StructField("terminal", StringType(), True),
                StructField("transaction", StringType(), True),
                StructField("date", StringType(), True),
                StructField("market", StringType(), True),
                StructField("mcc", IntegerType(), True),
                StructField("address", StringType(), True)
            ]), True),
            StructField("products", ArrayType(StructType([
                StructField("name", StringType(), True),
                StructField("budget", StringType(), True),
                StructField("price", DoubleType(), True),
                StructField("product_type", StringType(), True)
            ])), True)
        ])
        super().__init__(spark, topic, schema) 