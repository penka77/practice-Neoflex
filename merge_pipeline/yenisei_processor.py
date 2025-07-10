from pyspark.sql.functions import col, explode
from .topic_processor import TopicProcessor

class YeniseiProcessor(TopicProcessor):
    def process(self):
        df = self.read().withColumn("order", explode("list_orders"))
        return df.select(
            col("bank_id"),
            col("info_client.card").alias("card"),
            col("info_client.bank").alias("bank"),
            col("info_client.pay_system").alias("pay_system"),
            col("info_transaction.number_transaction").alias("transaction_id"),
            col("info_transaction.datetime").alias("transaction_time"),
            col("info_transaction.id_terminal").alias("terminal_id"),
            col("info_market.market").alias("market_id"),
            col("info_market.mcc").cast("string").alias("mcc"),
            col("info_market.address").alias("market_address"),
            col("order.name_position").alias("product_name"),
            col("order.budget").alias("product_budget"),
            col("order.price").cast("double").alias("product_price")
        ) 