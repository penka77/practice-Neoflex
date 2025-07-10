from pyspark.sql.functions import col, explode, lit
from .topic_processor import TopicProcessor

class AmurProcessor(TopicProcessor):
    def process(self):
        df = self.read().withColumn("purchase", explode("purchases"))
        return df.select(
            col("bank_id"),
            col("info_client.card").alias("card"),
            col("info_client.bank").alias("bank"),
            col("info_client.pay_system").alias("pay_system"),
            col("info_transaction.transaction").alias("transaction_id"),
            col("info_transaction.datetime").alias("transaction_time"),
            col("info_transaction.terminal").alias("terminal_id"),
            col("info_market.market").alias("market_id"),
            col("info_market.mcc").cast("string").alias("mcc"),
            col("info_market.address").alias("market_address"),
            col("purchase.position").alias("product_name"),
            lit(None).cast("string").alias("product_budget"),
            col("purchase.price").cast("double").alias("product_price")
        ) 