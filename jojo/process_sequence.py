import os

Sequence_1 = "GCGCGCATGCC"
Sequence_2 = "GCTAGC"
Sequence_3 = "TCCGGAGGGTCGACCATAACTTCGTATAATGTATACTATACGAAGTTATCCTCGAGCGGTACC"


def process_list(isthird):
    path = "process_list"
    path_end = 'process_end_list/'
    file_list = os.listdir(path)

    for file in file_list:
        file_string = open(path + "/" + file, "r", encoding="utf-8", errors="ignore")
        sequence = file_string.read()

        sequence = sequence.replace("^^", "")
        sequence = sequence.replace("\n", "")

        if sequence.find(Sequence_1) > 0:
            sequence = sequence.split(Sequence_1, 1)
            if sequence[1].find(Sequence_2) > 0:
                sequence = sequence[1].split(Sequence_2, 1)

                # 这个是处理序列2的地方
                if not isthird:
                    file3 = file.replace(".seq", '-jojo.seq')
                    fp = open(path_end + file3, "w")
                    fp.write(sequence[0])
                    fp.close()

                if sequence[0].find(Sequence_3) > 0:
                    # 这个是处理序列3的地方
                    if isthird:
                        sequence = sequence[0].split(Sequence_3, 1)
                        file1 = file.replace(".seq", '-L.seq')
                        fp = open(path_end + file1, "w")
                        fp.write(sequence[0])
                        fp.close()

                        file2 = file.replace(".seq", '-H.seq')
                        fp = open(path_end + file2, "w")
                        fp.write(sequence[1])
                        fp.close()
                    pass

                else:
                    print(file + "没有找到特定序列3")
        else:
            print(file + "没有找到特定序列2")
    else:
        print(file + "没有找到特定序列1")


if __name__ == '__main__':

    # process_list(True)
    process_list(False)
    pass