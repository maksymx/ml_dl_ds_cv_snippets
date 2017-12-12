from pyspark import SparkConf, SparkContext

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
