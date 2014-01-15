import zipfile
import rarfile
import os.path

def extractZipFile(zip_file, has_sub_sub_dir):
	fp = open(zip_file, 'rb')
	fz = zipfile.ZipFile(fp)
	if has_sub_sub_dir:
		fz.extractall(path="..")
	else:
		fz.extractall()
	fp.close()

def extractRarFile(rar_file, has_sub_sub_dir):
	rf = rarfile.RarFile(rar_file)
	if has_sub_sub_dir:
		rf.extractall(path="..")
	else:
		rf.extractall()

def main():
	format_error_file = open("/home/shwu/hw4-formatError/formatErrorID", "w")
	for files in os.listdir("."):
		files.strip()
		if os.path.isdir(files):
			os.chdir(files)
			# |--- HW4_ALL
			# |		|
			# |		| --- files
			# |				|
			# |		 		| --- sub_files(DIR or zip or rar file)
			# |						|
			# |						| --- sub_sub_file(zip or rar file)
			for sub_file in os.listdir("."):
				if sub_file.endswith((".zip", "_files")):
					extractZipFile(sub_file, False)
				elif sub_file.endswith((".rar", "_files")):
					extractRarFile(sub_file, False)
				else:
					FORMAT_ERROR_MES = files + ": format error\n"
					format_error_file.write(FORMAT_ERROR_MES)
					if os.path.isdir(sub_file):
						os.chdir(sub_file)
						for sub_sub_file in os.listdir("."):
							if sub_sub_file.endswith((".zip", "_files")):
								extractZipFile(sub_sub_file, True)
							elif sub_sub_file.endswith((".rar", "_files")):
								extractRarFile(sub_sub_file, True)
							else:
								pass
						os.chdir("..")
			os.chdir("..")
	format_error_file.close()

if __name__ == '__main__':
	main()
