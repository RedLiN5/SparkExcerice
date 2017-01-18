#### Build pair RDD

RDD —> pair RDD by `map()`

```python
>>> lines = sc.parallelize(['hello world', 'hi'])
>>> pairs = lines.map(lambda x: (x.split(' ')[0], x))
>>> print pairs.collect()
[('hello', 'hello world'), ('hi', 'hi')]
```



```python
>>> lines = sc.parallelize(['hello world', 'hi', 'hello', 'hi'])
>>> words = lines.flatMap(lambda x: x.split(" "))
>>> words.collect()
['hello', 'world', 'hi', 'hello', 'hi']
>>> result = words.map(lambda x: (x, 1)).reduceByKey(lambda x, y: x + y)
>>> result.collect()
[('world', 1), ('hi', 2), ('hello', 2)]
```



分区数决定了在RDD上执行操作时的并行度.

```python
>>> data = [('a', 3), ('b', 4), ('a', 1)]
>>> sc.parallelize(data).reduceByKey(lambda x, y: x + y, 10) # 分区数为10
```

