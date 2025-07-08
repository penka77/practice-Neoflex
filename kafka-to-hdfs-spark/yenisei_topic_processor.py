from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType, ArrayType
from base_topic_processor import BaseTopicProcessor

class YeniseiTopicProcessor(BaseTopicProcessor):
    topic = "yenisei_topic"
    schema = StructType([
        StructField("bank_id", StringType(), True),
        StructField("info_client", StructType([
            StructField("card", StringType(), True),
            StructField("bank", StringType(), True),
            StructField("pay_system", StringType(), True)
        ]), True),
        StructField("info_transaction", StructType([
            StructField("id_terminal", StringType(), True),
            StructField("os_terminal", StringType(), True),
            StructField("number_transaction", StringType(), True),
            StructField("datetime", StringType(), True)
        ]), True),
        StructField("info_market", StructType([
            StructField("market", StringType(), True),
            StructField("mcc", IntegerType(), True),
            StructField("address", StringType(), True)
        ]), True),
        StructField("list_orders", ArrayType(StructType([
            StructField("name_position", StringType(), True),
            StructField("budget", StringType(), True),
            StructField("price", DoubleType(), True)
        ])), True)
    ]) 