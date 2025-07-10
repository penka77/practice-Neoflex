from pyspark.sql.functions import col, explode
from .topic_processor import TopicProcessor

class VolgaProcessor(TopicProcessor):
    def process(self):
        df = self.read().withColumn("product", explode("products"))
        return df.select(
            col("bank_id"),
            col("client_info.card").alias("card"),
            col("client_info.bank").alias("bank"),
            col("client_info.pay_system").alias("pay_system"),
            col("market_info.transaction").alias("transaction_id"),
            col("market_info.date").alias("transaction_time"),
            col("market_info.terminal").alias("terminal_id"),
            col("market_info.market").alias("market_id"),
            col("market_info.mcc").cast("string").alias("mcc"),
            col("market_info.address").alias("market_address"),
            col("product.name").alias("product_name"),
            col("product.budget").alias("product_budget"),
            col("product.price").cast("double").alias("product_price")
        ) 