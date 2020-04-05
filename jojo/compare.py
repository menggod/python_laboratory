import filecmp
import os


def diff_file():
    path = "process_list"
    path_end = 'process_end_list/'
    file_old_list = os.listdir(path)
    file_new_list = os.listdir(path_end)

    for index in range(0, len(file_old_list) - 1):
        # print(index)
        result = filecmp.cmp(file_old_list[index], file_new_list[index])
        print(result)


if __name__ == '__main__':
    diff_file()
