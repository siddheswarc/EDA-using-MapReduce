hdfs dfs -rmr -skipTrash output/cc/top*
echo 1
hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -file topN/mapper_top.py -file topN/reducer_top.py -mapper "python mapper_top.py" -reducer "python reducer_top.py" -input output/cc/cnt*  -output output/cc/top
