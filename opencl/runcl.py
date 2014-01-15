import os
import sys
import subprocess


def start_action():
import os
import subprocess
import sys

def start_action(action):
	_COMPILE = "compile"
	_RUN	 = "run"

	if action == _COMPILE:
		# TODO
		_COMPILE_ERROR_PATH = ""
		file_compile_error = open(_COMPILE_ERROR_PATH, "w")

	elif action == _RUN:
		_RUN_ERROR_PATH = ""
		file_run_error = open(_RUN_ERROR_PATH, "w")

	else:
		pass

	for files in os.listdir("."):
		files.strip()
		if os.path.isdir(files):
			os.chdir(files)
			for sub_file in os.listdir("."):
				if os.path.isdir(sub_file):
					os.chdir(sub_file)
					if action == _COMPILE:
						if not subprocess.call(["g++", "-lOpenCL", "histogram.cpp", "-o", "histogram"]):
							# correct running
							pass
						else:
							_COMPILE_ERROR_MES = files + "\n"
							file_compile_error.write(_COMPILE_ERROR_MES)
					elif action == _RUN:
						# TODO: input path
						subprocess.call(["cp", "", "input"])
						if not subprocess.call(["./histogram"]):
							# run correct
							pass
						else:
							_RUN_ERROR_MES = files + "\n"
							file_run_error.write(_RUN_ERROR_MES)
					else:
						pass
					os.chdir("..")
			os.chdir("..")

	if file_compile_error is not None:
		file_compile_error.close()
	if file_run_error is not None:
		file_run_error.close()

# python runcl.py run/compile
def main():
	action = sys.argv[1]
    start_action(action)

if __name__ == '__main__':
    main()
