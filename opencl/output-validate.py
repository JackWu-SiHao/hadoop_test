import os
import sys

# python output-validate.py part1/part2

def validate(answer_file):
    ANSWER_PATH = "/home/shwu/hw6/" + answer_file
    SCORE_PATH = "/home/shwu/hw6/score/" + answer_file + ".score"
    # xxx.out.score
    OUTPUT_ERROR_FILE = "/home/shwu/hw6/output-error.out"
    OUTPUT_PATH = "/home/shwu/hw6/output/"
    file_score = open(SCORE_PATH, "w")
    file_ans = open(ANSWER_PATH, "r")
    file_ids = open("/home/shwu/hw6/studentID.txt", "r")
    output_error_file = open(OUTPUT_ERROR_FILE, "w")
    ans_lines = [(((line.strip()).replace("\t", "")).replace(" ", ""))
                 for line in file_ans]

    ids = [line.strip() for line in file_id]
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
            file_score.write(SCORE)
            number_fail += 1
            file_id_ans.close()
            continue

        # if len(ans_lines) != len(ans_id_lines):
        #     ERROR_MES = ids[x] + ": " + "Wrong answer(length)\n"
        #     output_error_file.write(ERROR_MES)
        #     file_score.write(SCORE)
        #     number_fail += 1
        # else:
        for y in xrange(0, len(ans_id_lines)):
            if ans_id_lines[y] not in ans_lines:
                # print ans_id_lines[y]
                ERROR_MES = "Wrong answer: " + ans_id_lines[y]
                SCORE = ids[x] + ": 0 :" + ERROR_MES + "\n"
                # output_error_file.write(ERROR_MES + "\n")
                file_score.write(SCORE)
                file_id_ans.close()
                break
        # succeed run
        if y == (len(ans_id_lines) - 1):
            SCORE = ids[x] + ": 100\n"
            file_score.write(SCORE)
        file_id_ans.close()

    print "Success:{0}".format(number_success)
    print "Fails:{0}".format(number_fail)
    file_ans.close()
    file_id.close()
    output_error_file.close()
    output_correct_file.close()
    file_score.close()

def main():

if __name__ == '__main__':
    main()
