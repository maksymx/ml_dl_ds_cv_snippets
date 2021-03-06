import tensorflow as tf
from pyspark.ml.feature import VectorAssembler, OneHotEncoder
from pyspark.ml.pipeline import Pipeline
from sparkflow.graph_utils import build_graph
from sparkflow.tensorflow_async import SparkAsyncDL


# simple tensorflow network
def small_model():
    x = tf.placeholder(tf.float32, shape=[None, 784], name='x')
    y = tf.placeholder(tf.float32, shape=[None, 10], name='y')
    layer1 = tf.layers.dense(x, 256, activation=tf.nn.relu)
    layer2 = tf.layers.dense(layer1, 256, activation=tf.nn.relu)
    out = tf.layers.dense(layer2, 10)
    z = tf.argmax(out, 1, name='out')
    loss = tf.losses.softmax_cross_entropy(y, out)
    return loss


df = spark.read.option("inferSchema", "true").csv('mnist_train.csv')
mg = build_graph(small_model)
# Assemble and one hot encode
va = VectorAssembler(inputCols=df.columns[1:785], outputCol='features')
encoded = OneHotEncoder(inputCol='_c0', outputCol='labels', dropLast=False)

spark_model = SparkAsyncDL(
    inputCol='features',
    tensorflowGraph=mg,
    tfInput='x:0',
    tfLabel='y:0',
    tfOutput='out:0',
    tfLearningRate=.001,
    iters=20,
    predictionCol='predicted',
    labelCol='labels',
    verbose=1
)

p = Pipeline(stages=[va, encoded, spark_model]).fit(df)
p.write().overwrite().save("location")
