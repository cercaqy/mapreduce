export MR_OUTPUT=/user/root/taxi-output

hadoop fs -rm -r $MR_OUTPUT


hadoop jar "$HADOOP_MAPRED_HOME"/hadoop-streaming.jar \
-Dmapred.job.name='Taxi streaming job' \
-Dmapred.reduce.tasks=1 \
-file /tmp/mapreduce/mapper.py -mapper /tmp/mapreduce/mapper.py \
-file /tmp/mapreduce/reducer.py -reducer /tmp/mapreduce/reducer.py \
-input /user/root/taxi2020/ -output $MR_OUTPUT