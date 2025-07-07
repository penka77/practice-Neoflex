# Используем официальный образ Python
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY export_to_hdfs.py ./
COPY postgresql-42.7.7.jar ./

CMD ["python", "export_to_hdfs.py"]