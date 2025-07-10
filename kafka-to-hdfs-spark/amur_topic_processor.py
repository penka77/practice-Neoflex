from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType, ArrayType
from base_topic_processor import BaseTopicProcessor

class AmurTopicProcessor(BaseTopicProcessor):
    def __init__(self, spark):
        topic = "amur_topic"
        schema = StructType([
            StructField("bank_id", StringType(), True),
            StructField("info_client", StructType([
                StructField("card", StringType(), True),
                StructField("bank", StringType(), True),
                StructField("pay_system", StringType(), True)
            ]), True),
            StructField("info_transaction", StructType([
                StructField("terminal", StringType(), True),
                StructField("transaction", StringType(), True),
                StructField("datetime", StringType(), True)
            ]), True),
            StructField("info_market", StructType([
                StructField("market", StringType(), True),
                StructField("mcc", IntegerType(), True),
                StructField("address", StringType(), True)
            ]), True),
            StructField("purchases", ArrayType(StructType([
                StructField("position", StringType(), True),
                StructField("barcode", StringType(), True),
                StructField("price", DoubleType(), True)
            ])), True)
        ])
        super().__init__(spark, topic, schema) 