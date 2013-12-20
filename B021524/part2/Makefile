ID = B021524
CC = javac
#HADOOP_INSTALL_PATH = /hadoop/hadoop-1.0.1/lib/commons-cli-1.2.jar:/hadoop/hadoop-1.0.1/hadoop-core-1.0.1.jar
EXECUTABLE = kmeans.java
#INPUT_FILE = kmeans.txt
#OUTPUT_PATH = output
COMPILE:
	mkdir part2
	cp $(EXECUTABLE) part2/kmeans.java
	javac -d part2 -cp $(HADOOP_INSTALL_PATH) part2/kmeans.java
	jar -cvf part2/kmeans.jar -C part2/ .
run:
	$(HADOOP_INSTALL_PATH)/bin/hadoop fs -mkdir $(ID)
	$(HADOOP_INSTALL_PATH)/bin/hadoop fs -put part2/$(EXECUTABLE) $(ID)
	$(HADOOP_INSTALL_PATH)/bin/hadoop fs -put $(INPUT_FILE) $(ID)/input
	$(HADOOP_INSTALL_PATH)/bin/hadoop jar ./part2/kmeans.jar kmeans $(ID)/input $(ID)/output
	$(HADOOP_INSTALL_PATH)/bin/hadoop fs -get $(ID)/output/part-r-00000 $(OUTPUT_PATH)/$(ID).out

cleanfs:
	$(HADOOP_INSTALL_PATH)/bin/hadoop fs -rmr $(ID)
	rm $(OUTPUT_PATH)/$(ID).out
clean:
	rm -r part2/
