ID = 0156049
CPP = g++
CC = gcc
#INPUT_FILE = input
#OUTPUT_PATH = .
kmeans.jar : Kmeans.java 
	mkdir MyJava2
	javac -classpath /usr/lib/hadoop/hadoop-*-core.jar -d MyJava2 Kmeans.java	
	jar -cvf kmeans.jar -C MyJava2 .
	$(CC) ks.c -o ks
	./ks $(INPUT_FILE)
	
run:
	hadoop fs -mkdir $(ID)
	hadoop fs -put tmpout $(ID)/tmpout
	rm tmpout
	hadoop jar kmeans.jar Kmeans $(ID)/tmpout $(ID)/output
	hadoop fs -get $(ID)/output  $(OUTPUT_PATH)/$(ID).out
clean:
	rm -r MyJava2
	rm kmeans.jar
	hadoop fs -rmr $(ID)
	rm ks
	rm -r $(OUTPUT_PATH)/$(ID).out
