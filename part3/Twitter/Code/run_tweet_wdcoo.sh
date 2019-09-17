hdfs dfs -rmr -skipTrash output/tweet/wdcoo*
hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -file wdCooc/mapper.py -file wdCooc/reducer.py -mapper "python mapper.py http,co,ai,rt,machinelearning,intelligence,data,via,learning" -reducer "python reducer.py" -input input/tweet  -output output/tweet/wdcoo
