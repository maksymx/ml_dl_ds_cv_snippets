import os

from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext

os.environ['PYSPARK_SUBMIT_ARGS'] = '--driver-class-path postgresql-42.1.4.jar ' \
                                    '--jars postgresql-42.1.4.jar pyspark-shell'

conf = SparkConf().setMaster("local").setAppName("My app").set("spark.executor.memory", "1g")
sc = SparkContext(conf=conf)

properties = {"driver": "org.postgresql.Driver"}
url = 'jdbc:postgresql://localhost/db_name'

sqlContext = SQLContext(sc)
dataframe_psql = sqlContext.read.format("jdbc").option("url", url).option("driver", properties["driver"]) \
    .option("dbtable", "table_name").load()

dataframe_psql.show()
