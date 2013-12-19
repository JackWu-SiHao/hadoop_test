ID = 9755527
JC = javac
JAVAFILES = Kmeans.java
EXECUTABLE = kmeans.jar
#INPUT_FILE= Readme.txt
#OUTPUT_PATH= test

$(EXECUTABLE): $(JAVAFILES)
	mkdir -p $(ID)
	$(JC) -classpath /opt/hadoop/hadoop-core.jar -d $(ID) $(JAVAFILES)
	jar -cvf $(EXECUTABLE) -C $(ID) .

clean:
	rm -r $(ID)
	rm $(EXECUTABLE)
run:
	$(HADOOP_INSTALL_PATH)/bin/hadoop fs -mkdir $(ID)
	$(HADOOP_INSTALL_PATH)/bin/hadoop fs -put $(EXECUTABLE) $(ID)
	$(HADOOP_INSTALL_PATH)/bin/hadoop fs -put $(INPUT_FILE) $(ID)/input
	$(HADOOP_INSTALL_PATH)/bin/hadoop jar $(EXECUTABLE) Kmeans $(ID)/input $(ID)/output
	$(HADOOP_INSTALL_PATH)/bin/hadoop fs -get $(ID)/output/part-r-00000 $(OUTPUT_PATH)/$(ID).out
cleanfs:
	$(HADOOP_INSTALL_PATH)/bin/hadoop fs -rmr $(ID)
	rm $(OUTPUT_PATH)/$(ID).out
