from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster('local').setAppName('My App')
sc = SparkContext(conf = conf)

lines = sc.textFile('README_example.md')
