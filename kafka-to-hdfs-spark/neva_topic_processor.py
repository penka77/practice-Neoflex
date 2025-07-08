from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType, ArrayType
from base_topic_processor import BaseTopicProcessor

class NevaTopicProcessor(BaseTopicProcessor):
    topic = "neva_topic"
    schema = StructType([
        StructField("id_bank", StringType(), True),
        StructField("transaction", StringType(), True),
        StructField("transaction_time", StringType(), True),
        StructField("terminal_id", StringType(), True),
        StructField("terminal_os", StringType(), True),
        StructField("card_number", StringType(), True),
        StructField("bank_card", StringType(), True),
        StructField("pay_system", StringType(), True),
        StructField("market_id", StringType(), True),
        StructField("market_name", StringType(), True),
        StructField("mcc", IntegerType(), True),
        StructField("market_address", StringType(), True),
        StructField("buys", ArrayType(StructType([
            StructField("position", StringType(), True),
            StructField("category", StringType(), True),
            StructField("price", DoubleType(), True)
        ])), True)
    ]) 