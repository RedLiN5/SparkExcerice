#### Save JSON

```python
import json
input = sc.textFile("../python/README.md")
(input.filter(lambda x: x['lovesPandas']).map(lambda x: json.dumps(x)).saveAsTextFile('file.json'))
```



#### Read JSON

```python
data = input.map(lambda x: json.loads(x))
```

