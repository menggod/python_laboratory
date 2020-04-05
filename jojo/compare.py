import filecmp
import os


def diff_file():
    path = "compare/"
    path_end = 'process_end_list/'
    file_old_list = os.listdir(path)
    file_new_list = os.listdir(path_end)

    for index in range(0, len(file_old_list)):
        # print(index)
        file_string = open(path + "/" + file_old_list[index], "r", encoding="utf-8",
                           errors="ignore")
        sequence = file_string.read()
        sequence = sequence.replace("\n", "")

        file_string1 = open(path + "/" + file_new_list[index], "r", encoding="utf-8",
                            errors="ignore")
        sequence1 = file_string1.read()
        sequence1 = sequence.replace("\n", "")

        print(index, sequence == sequence1)


if __name__ == '__main__':
    diff_file()
