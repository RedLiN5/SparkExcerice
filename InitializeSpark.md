#### **Install Apache Spark**

```shell
brew update
brew install scala
brew install apache-spark
```



#### **Set up env variables**

Add following code to your ` .bash_profile`

```shell
# For a ipython notebook and pyspark integration
if which pyspark > /dev/null; then
  export SPARK_HOME="/usr/local/Cellar/apache-spark/1.3.1_1/libexec/"
  export PYSPARK_SUBMIT_ARGS="--master local[2]"
fi
```



Check SPARK_HOME path using following brew command

```shell
$ brew info apache-spark
apache-spark: stable 1.3.1, HEAD
https://spark.apache.org/
/usr/local/Cellar/apache-spark/1.3.1_1 (361 files, 278M) *
  Built from source
From: https://github.com/Homebrew/homebrew/blob/master/Library/Formula/apache-spark.rb
```



### Run SPARK on Pycharm

Error:

```python
Could not find valid SPARK_HOME while searching ['/Users/Leslie/GitHub', '/Users/Leslie/anaconda/lib/python2.7/site-packages/pyspark', '/Users/Leslie/anaconda/lib/python2.7/site-packages/pyspark', '/Users/Leslie/anaconda/lib/python2.7']
```

1. Go to **Run** -> **Edit configurations**

2. Add new Python configuration

3. Set **Script** path so it points to the script you want to execute. 

   `Script`: `/Users/Leslie/GitHub/SparkExercise/Chap3_RDD.py`

4. Edit **Environment variables** field so it contains at least:

   `SPARK_HOME`: `/Users/Leslie/Spark/spark-2.1.0`

   `PYTHONPATH`: `$SPARK_HOME/python:$SPARK_HOME//Users/Leslie/Spark/spark-2.1.0/python/lib/py4j-0.10.4-src.zip`

5. **Apply** the settings




### Error

```Shell
Error in pyspark startup:
IPYTHON and IPYTHON_OPTS are removed in Spark 2.0+. Remove these from the environment and set PYSPARK_DRIVER_PYTHON and PYSPARK_DRIVER_PYTHON_OPTS instead.
```

Delete `IPYTHON` and `IPYTHON_OPTS` in **.bashrc** (or **.zshrc**). And add:

```shell
export PYSPARK_DRIVER_PYTHON="ipython"
export PYSPARK_DRIVER_PYTHON_OPTS="notebook" pyspark
```

Then *Spark* can be started via IPython.

