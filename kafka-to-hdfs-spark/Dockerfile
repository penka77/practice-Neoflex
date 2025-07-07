FROM bde2020/spark-master:3.2.1-hadoop3.2

COPY kafka_to_hdfs.py /spark/apps/

WORKDIR /spark/apps

RUN chmod +x kafka_to_hdfs.py

CMD ["/spark/bin/spark-submit", "--master", "spark://spark-master:7077", "--packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.1", "kafka_to_hdfs.py"] 