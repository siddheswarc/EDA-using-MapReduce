hdfs dfs -rmr -skipTrash output/cc/wdcoo*
hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -file wdCooc/mapper.py -file wdCooc/reducer.py -mapper "python mapper.py learning,data,ai,machine,neural,network,like,one,part,image" -reducer "python reducer.py" -input input/cc -output output/cc/wdcoo
