hdfs dfs -rmr -skipTrash output/nyt/top*
echo 1
hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -file topN/mapper_top.py -file topN/reducer_top.py -mapper "python mapper_top.py" -reducer "python reducer_top.py" -input output/nyt/cnt*  -output output/nyt/top
