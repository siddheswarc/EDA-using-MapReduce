hdfs dfs -rmr -skipTrash output/nyt/wdcoo*
hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -file wdCooc/mapper.py -file wdCooc/reducer.py -mapper "python mapper.py xe,said,mr,new,company,technology,like,one,google,people" -reducer "python reducer.py" -input input/nyt -output output/nyt/wdcoo
