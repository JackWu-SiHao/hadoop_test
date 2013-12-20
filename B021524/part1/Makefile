ID = B021524
CC = javac
#HADOOP_INSTALL_PATH = /hadoop/hadoop-1.0.1/lib/commons-cli-1.2.jar:/hadoop/hadoop-1.0.1/hadoop-core-1.0.1.jar
EXECUTABLE = charcount.java
#INPUT_FILE = charcount.txt
#OUTPUT_PATH = output
COMPILE:
	mkdir part1
	cp $(EXECUTABLE) part1/charcount.java
	javac -d part1 -cp $(HADOOP_INSTALL_PATH) part1/charcount.java
	jar -cvf part1/charcount.jar -C part1/ .
run :
	$(HADOOP_INSTALL_PATH)/bin/hadoop fs -mkdir $(ID)
	$(HADOOP_INSTALL_PATH)/bin/hadoop fs -put part1/$(EXECUTABLE) $(ID)
	$(HADOOP_INSTALL_PATH)/bin/hadoop fs -put $(INPUT_FILE) $(ID)/input
	$(HADOOP_INSTALL_PATH)/bin/hadoop jar ./part1/charcount.jar charcount $(ID)/input $(ID)/output
	$(HADOOP_INSTALL_PATH)/bin/hadoop fs -get $(ID)/output/part-r-00000 $(OUTPUT_PATH)/$(ID).out

cleanfs :
	$(HADOOP_INSTALL_PATH)/bin/hadoop fs -rmr $(ID)
	rm $(OUTPUT_PATH)/$(ID).out
clean :
	rm -r part1/
