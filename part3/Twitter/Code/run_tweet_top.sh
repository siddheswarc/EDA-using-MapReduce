hdfs dfs -rmr -skipTrash output/tweet/top*
echo 1
hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -file topN/mapper_top.py -file topN/reducer_top.py   -mapper "python mapper_top.py" -reducer "python reducer_top.py" -input output/tweet/cnt*  -output output/tweet/top
