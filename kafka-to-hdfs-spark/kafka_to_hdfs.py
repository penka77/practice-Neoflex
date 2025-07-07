from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType, ArrayType
import sys
import traceback

def get_schema_for_topic(topic):
    if topic == "amur_topic":
        return StructType([
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
    elif topic == "neva_topic":
        return StructType([
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
    elif topic == "ob_topic":
        return StructType([
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
    elif topic == "volga_topic":
        return StructType([
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
    elif topic == "yenisei_topic":
        return StructType([
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
    else:
        return None

def create_spark_session():
    return SparkSession.builder \
        .appName("KafkaToHDFS") \
        .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.1") \
        .getOrCreate()

def process_topic(spark, topic):
    schema = get_schema_for_topic(topic)
    if schema is None:
        return None
    kafka_df = spark.readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "kafka1:29092") \
        .option("subscribe", topic) \
        .option("startingOffsets", "earliest") \
        .load()
    parsed_df = kafka_df.selectExpr("CAST(value AS STRING) as json") \
        .select(from_json(col("json"), schema).alias("data")) \
        .select("data.*")
    return parsed_df

def write_to_hdfs(df, epoch_id, topic):
    try:
        row_count = df.count()
        if row_count > 0:
            hdfs_path_json = "hdfs://namenode:9000/data/kafka_data/{}_json".format(topic)
            df.write.mode("append").json(hdfs_path_json)
    except Exception as e:
        print("[ERROR] Error writing to HDFS for {}: {}".format(topic, str(e)))
        traceback.print_exc(file=sys.stdout)

def main():
    try:
        spark = create_spark_session()
        topics = ["amur_topic", "neva_topic", "ob_topic", "volga_topic", "yenisei_topic"]
        for topic in topics:
            parsed_df = process_topic(spark, topic)
            if parsed_df is None:
                continue
            parsed_df.writeStream \
                .foreachBatch(lambda df, epoch_id: write_to_hdfs(df, epoch_id, topic)) \
                .outputMode("append") \
                .trigger(processingTime="10 seconds") \
                .start()
        spark.streams.awaitAnyTermination()
    except Exception as e:
        print("[ERROR] Main error: {}".format(str(e)))
        traceback.print_exc(file=sys.stdout)

if __name__ == "__main__":
    main()