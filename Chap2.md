#### Under *pyspark*

```python
>>> sc
<pyspark.context.SparkContext object at 0x108c4f790>

>>> lines
README.md MapPartitionsRDD[1] at textFile at NativeMethodAccessorImpl.java:0
    
>>> lines.count()
104

>>> lines.first()
u'# Apache Spark'

>>> pythonLines = lines.filter(lambda line: 'Python' in line)
>>> pythonLines
PythonRDD[4] at RDD at PythonRDD.scala:48
>>> pythonLines.first()
u'high-level APIs in Scala, Java, Python, and R, and an optimized engine that'

```

