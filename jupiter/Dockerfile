FROM jupyter/base-notebook:python-3.9.13

USER root

RUN apt-get update
RUN apt-get install -y default-jdk
RUN pip install pyspark==3.2.1
RUN pip install psycopg2-binary

COPY example.ipynb /app/example.ipynb
WORKDIR /app

EXPOSE 8888

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]