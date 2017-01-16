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



Persist RDD in memory

```python
>>> pythonLines.persist()
>>> pythonLines.count()
2

>>> pythonLines.first()
u'## Interactive Python Shell'
```



```python
>>> nums = sc.parallelize([1,2,3,4])
>>> sqaured = nums.map(lambda x: x**2).collect()
>>> type(sqaured)
list
>>> for num in sqaured:
        print "%i" %(num)
```



```python
>>> lines = sc.parallelize(['hello world', 'hi'])
>>> words = lines.flatMap(lambda line: line.split(' '))
>>> words.first()
'hello'
>>> words = lines.map(lambda line: line.split(' '))
['hello', 'world']
```



#### rdd.reduce()

```python
>>> nums = sc.parallelize([1,2,3,4])
>>> sum = nums.reduce(lambda x, y: x + y)
>>> sum
10
```



