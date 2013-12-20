import subprocess
import os

def main():
	STUDENT_ID_PATH = "/home/shwu/Dropbox/Shwu/Master/PPC-Hadoop/testcase/studentID.txt"
	file_id             = open(STUDENT_ID_PATH, "r")
	ids = [line.strip() for line in file_id]
	os.chdir("/opt/hadoop/")
	for x in xrange(0, len(ids)):
		subprocess.call(["bin/hadoop", "fs", "-rmr", ids[x]])
	os.chdir("/home/shwu/hw4-output/")
	subprocess.call(["rm", "-rf", "*"])
if __name__ == '__main__':
	main()
