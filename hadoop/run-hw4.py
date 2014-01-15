import os
import sys
import subprocess


def start_action(part1_or_2, action):
    _MAKE = "make"
    _RUN = "run"
    _CLEANFS = "cleanfs"
    _CLEAN = "clean"
    _HOME = "/home/shwu/"
    _LOG_PATH = "{0}hw4-log".format(_HOME)
    if (action == _MAKE) or (action == _RUN):
        Error_path = "{0}hw4-{1}Error/{1}ErrorID-{2}".format(
            _HOME, action, part1_or_2)
        MAKE_OR_RUN_CORRECT_PATH = "{0}hw4-{1}Correct/{1}CorrectID-{2}".format(
            _HOME, action, part1_or_2)
        file_error = open(Error_path, "w")
        file_make_or_run_correct = open(MAKE_OR_RUN_CORRECT_PATH, "w")
    else:
        file_error = None
    file_log = open(_LOG_PATH, "w")
    format_error_file = open("/home/shwu/hw4-formatError/formatErrorID", "w")
    if action == "part1":
        subprocess.call(["cp", "/home/shwu/Dropbox/Shwu/Master/PPC-Hadoop/testcase/input-part1", "/home/shwu/hw4-input/input"])
    else:
        subprocess.call(["cp", "/home/shwu/Dropbox/Shwu/Master/PPC-Hadoop/testcase/input-part2", "/home/shwu/hw4-input/input"])

    for files in os.listdir("."):
        files.strip()
        if os.path.isdir(files):
            os.chdir(files)
            for sub_file in os.listdir("."):
     #        	if part1_or_2 not in os.listdir("."):
					# FORMAT_ERROR_MES = files + ": format error\n"
					# format_error_file.write(FORMAT_ERROR_MES)
					# continue

                if sub_file == part1_or_2:
                    os.chdir(sub_file)
                    ERROR_MES = files + ": " + action + " error\n"
                    CORRECT_MES = files + ": " + action + " correct\n"
                    if action == _MAKE:
                        if not subprocess.call([_MAKE]):
                            file_make_or_run_correct.write(CORRECT_MES)
                        else:
                            file_error.write(ERROR_MES)
                    elif action == _RUN:
                        if not subprocess.call([_MAKE, _RUN]):
                            file_make_or_run_correct.write(CORRECT_MES)
                        else:
                            file_error.write(ERROR_MES)
                    elif action == _CLEANFS:
                        subprocess.call([_MAKE, _CLEANFS])
                    elif action == _CLEAN:
                        subprocess.call([_MAKE, _CLEAN])
                    else:
                        raise "Command Error"
                    os.chdir("..")
                else:
                    # format wrong
                    pass
            os.chdir("..")

    if file_error is not None:
        file_error.close()
    file_log.close()
    format_error_file.close()


# python run-hw4.py part1/part2 make/run/clean
def main():
    part1_or_2 = sys.argv[1]
    action = sys.argv[2]
    start_action(part1_or_2, action)

if __name__ == '__main__':
    main()
