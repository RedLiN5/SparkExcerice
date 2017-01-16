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



