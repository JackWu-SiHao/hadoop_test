import os
import sys
import subprocess
import time
import itertools


def start_action(action, input_file):
    _COMPILE = "compile"
    _RUN = "run"

    if action == _COMPILE:
        COMPILE_ERROR_PATH = "/home/shwu/hw6/compile-error.out"
        file_compile_error = open(COMPILE_ERROR_PATH, "w")

    elif action == _RUN:
        INPUT_FILE_PATH = "/home/shwu/hw6/" + input_file
        RUN_ERROR_PATH = "/home/shwu/hw6/run-error.out"
        RUN_TIME_PATH = "/home/shwu/hw6/run-time.out"
        file_run_error = open(RUN_ERROR_PATH, "w")
        file_run_time = open(RUN_TIME_PATH, "w")

    else:
        pass

    for files in os.listdir("."):
        files.strip()
        if os.path.isdir(files):
            os.chdir(files)
            if action == _COMPILE:
                if not subprocess.call(["g++", "-lOpenCL", "histogram.cpp", "-o", "histogram"]):
                    # correct running
                    pass
                else:
                    _COMPILE_ERROR_MES = files + " compile error\n"
                    file_compile_error.write(_COMPILE_ERROR_MES)
            elif action == _RUN:
                # TODO: add time
                subprocess.call(["cp", INPUT_FILE_PATH, "input"])
                tStart = time.time()
                if not subprocess.call(["./histogram"]):
                    tEnd = time.time()
                    dt = (tStart - tEnd)
                    _RUN_TIME_MES = files + ":" + dt + "\n"
                    OUTPUT_FILE = files + ".out"
                    OUTPUT_PATH = "/home/shwu/hw6/output/" + OUTPUT_FILE
                    file_run_time.write(_RUN_TIME_MES)
                    subprocess.call(["cp", OUTPUT_FILE, OUTPUT_PATH])
                else:
                    _RUN_ERROR_MES = files + "\n"
                    file_run_error.write(_RUN_ERROR_MES)
            else:
                pass
            os.chdir("..")

    if file_compile_error is not None:
        file_compile_error.close()
    if file_run_error is not None:
        file_run_error.close()

# python runcl.py run/compile input_file


def main():
    action = sys.argv[1]
    input_file = sys.argv[2] if sys.argv[2] is not None else None
    start_action(action, input_file)

if __name__ == '__main__':
    main()
