from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType, ArrayType
from base_topic_processor import BaseTopicProcessor

class ObTopicProcessor(BaseTopicProcessor):
    def __init__(self, spark):
        topic = "ob_topic"
        schema = StructType([
            StructField("bank", StringType(), True),
            StructField("transaction", StringType(), True),
            StructField("transaction_time", StringType(), True),
            StructField("terminal_id", StringType(), True),
            StructField("terminal_imei", StringType(), True),
            StructField("card", StringType(), True),
            StructField("card_bank", StringType(), True),
            StructField("payment_system", StringType(), True),
            StructField("market_data", StructType([
                StructField("market", StringType(), True),
                StructField("name_market", StringType(), True),
                StructField("mcc", IntegerType(), True),
                StructField("address", StringType(), True)
            ]), True),
            StructField("orders", ArrayType(StructType([
                StructField("position", StringType(), True),
                StructField("category", StringType(), True),
                StructField("cost", DoubleType(), True),
                StructField("barcode", StringType(), True),
                StructField("type", StringType(), True)
            ])), True)
        ])
        super().__init__(spark, topic, schema) 