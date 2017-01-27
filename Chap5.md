| **格式名称**         | **结构化** | 备注   |
| ---------------- | ------- | ---- |
| 文本               | 否       |      |
| JSON             | 半结构化    |      |
| CSV              | 是       |      |
| SequenceFiles    | 是       |      |
| protocol buffers | 是       |      |
| 对象文件             | 是       |      |

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

