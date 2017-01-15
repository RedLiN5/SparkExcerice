from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster('local').setAppName('My App')
sc = SparkContext(conf = conf)

lines = sc.textFile('README_example.md')

pythonLines = lines.filter(lambda line: 'Python' in line)
print('First element:', pythonLines.first())

# Persist RDD in memory
pythonLines.persist()

print 'Count:', pythonLines.count()
