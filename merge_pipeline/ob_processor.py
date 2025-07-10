from pyspark.sql.functions import col, explode
from .topic_processor import TopicProcessor

class ObProcessor(TopicProcessor):
    def process(self):
        df = self.read().withColumn("order", explode("orders"))
        return df.select(
            col("bank").alias("bank_id"),
            col("card").alias("card"),
            col("card_bank").alias("bank"),
            col("payment_system").alias("pay_system"),
            col("transaction").alias("transaction_id"),
            col("transaction_time"),
            col("terminal_id"),
            col("market_data.market").alias("market_id"),
            col("market_data.mcc").cast("string").alias("mcc"),
            col("market_data.address").alias("market_address"),
            col("order.position").alias("product_name"),
            col("order.category").alias("product_budget"),
            col("order.cost").cast("double").alias("product_price")
        ) 