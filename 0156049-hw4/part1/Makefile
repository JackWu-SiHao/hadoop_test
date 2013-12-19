ID = 0156049
CPP = g++
CC = gcc
#INPUT_FILE = input
#OUTPUT_PATH = .
charcount.jar : CharCount.java 
	mkdir MyJava1
	javac -classpath /usr/lib/hadoop/hadoop-*-core.jar -d MyJava1 CharCount.java	
	jar -cvf charcount.jar -C MyJava1 .
	
run:
	hadoop fs -mkdir $(ID)
	hadoop fs -put $(INPUT_FILE) $(ID)/input
	hadoop jar charcount.jar CharCount $(ID)/input $(ID)/output
	hadoop fs -get $(ID)/output  $(OUTPUT_PATH)/$(ID).out
clean:
	rm -r MyJava1
	rm charcount.jar
	hadoop fs -rmr $(ID)
	rm -r $(OUTPUT_PATH)/$(ID).out
