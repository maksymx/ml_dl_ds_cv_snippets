import os

os.environ[
    'PYSPARK_SUBMIT_ARGS'] = '--driver-class-path postgresql-42.1.4.jar --jars postgresql-42.1.4.jar pyspark-shell'

from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext

conf = SparkConf().setMaster("local").setAppName("My app").set("spark.executor.memory", "1g")
sc = SparkContext(conf=conf)

print(sc)

x = ['spark', 'rdd', 'example', 'sample', 'example']
y = sc.parallelize(x)
print(y.collect())

rdd1 = sc.parallelize([('a', 7), ('a', 2), ('b', 2)])
print(rdd1.reduce(lambda a, b: a + b))

rdd2 = sc.parallelize([("a", ["x", "y", "z"]), ("b", ["p", "r"])])
print(rdd2.flatMapValues(lambda x: x).collect())

properties = {"driver": "org.postgresql.Driver"}
url = 'jdbc:postgresql://localhost/db_name'

sqlContext = SQLContext(sc)
dataframe_psql = sqlContext.read.format("jdbc").option("url", url).option("driver", properties["driver"]) \
    .option("dbtable", "table_name").load()

dataframe_psql.show()
