import os
import sys

# python output-validate.py part1/part2


def main():
    part1_or_2 = sys.argv[1]
    ANSWER_PATH = "/home/shwu/Dropbox/Shwu/Master/PPC-Hadoop/testcase/{0}.out".format(
        part1_or_2)
    STUDENT_ID_PATH = "/home/shwu/Dropbox/Shwu/Master/PPC-Hadoop/testcase/studentID.txt"
    OUTPUT_PATH = "/home/shwu/hw4-output/"
    OUTPUT_CORRECT_FILE = "/home/shwu/hw4-outputCorrect/outputCorrectID-{0}".format(
        part1_or_2)
    OUTPUT_ERROR_FILE = "/home/shwu/hw4-outputError/outputErrorID-{0}".format(
        part1_or_2)
    SCORE_FILE = "/home/shwu/hw4-score/score-{}".format(part1_or_2)
    # /home/shwu/Dropbox/Shwu/Master/PPC-Hadoop/testcase/studentID.txt
    file_ans = open(ANSWER_PATH, "r")
    file_id = open(STUDENT_ID_PATH, "r")
    output_error_file = open(OUTPUT_ERROR_FILE, "w")
    output_correct_file = open(OUTPUT_CORRECT_FILE, "w")
    score_file = open(SCORE_FILE, "w")

    number_success = 0
    number_fail = 0

    ids = [line.strip() for line in file_id]
    ans_lines = [(((line.strip()).replace("\t", "")).replace(" ", ""))
                 for line in file_ans]
    for x in xrange(0, len(ids)):
        OUTPUT_FILE = OUTPUT_PATH + ids[x] + ".out"
        # default is 0
        try:
            file_id_ans = open(OUTPUT_FILE, "r")
            ans_id_lines = [(((line.strip()).replace("\t", "")).replace(" ", ""))
                            for line in file_id_ans]
        except Exception, e:
            ERROR_MES = "Ouput file not exist"
            SCORE = ids[x] + ": 0 :" + ERROR_MES + "\n"
            # output_error_file.write(ERROR_MES)
            score_file.write(SCORE)
            number_fail += 1
            file_id_ans.close()
            continue

        # if len(ans_lines) != len(ans_id_lines):
        #     ERROR_MES = ids[x] + ": " + "Wrong answer(length)\n"
        #     output_error_file.write(ERROR_MES)
        #     score_file.write(SCORE)
        #     number_fail += 1
        # else:
        for y in xrange(0, len(ans_id_lines)):
            if ans_id_lines[y] not in ans_lines:
                print ans_id_lines[y]
                ERROR_MES = "Wrong answer: " + ans_id_lines[y]
                SCORE = ids[x] + ": 0 :" + ERROR_MES + "\n"
                # output_error_file.write(ERROR_MES + "\n")
                score_file.write(SCORE)
                number_fail += 1
                file_id_ans.close()
                break
        # succeed run
        if y == (len(ans_id_lines) - 1):
            SCORE = ids[x] + ": 100\n"
            number_success += 1
            output_correct_file.write(ids[x] + "\n")
            score_file.write(SCORE)
        file_id_ans.close()

    print "Success:{0}".format(number_success)
    print "Fails:{0}".format(number_fail)
    file_ans.close()
    file_id.close()
    output_error_file.close()
    output_correct_file.close()
    score_file.close()

if __name__ == '__main__':
    main()
