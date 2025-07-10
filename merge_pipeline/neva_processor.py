from pyspark.sql.functions import col, explode
from .topic_processor import TopicProcessor

class NevaProcessor(TopicProcessor):
    def process(self):
        df = self.read().withColumn("buy", explode("buys"))
        return df.select(
            col("id_bank").alias("bank_id"),
            col("card_number").alias("card"),
            col("bank_card").alias("bank"),
            col("pay_system"),
            col("transaction").alias("transaction_id"),
            col("transaction_time"),
            col("terminal_id"),
            col("market_id"),
            col("mcc").cast("string").alias("mcc"),
            col("market_address"),
            col("buy.position").alias("product_name"),
            col("buy.category").alias("product_budget"),
            col("buy.price").cast("double").alias("product_price")
        ) 