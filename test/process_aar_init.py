import linecache

path = "aar_init_script.gradle"

local_output = "repository(url: \"file://${outputDir}/outputs/repo\")"

nexus_output = """ repository(url: "http://192.168.15.43:8081/repository/APP-Release/") {
                   authentication(userName: 'admin', password: 'admin123')
                }"""
is_local = False


# 传入要读的文件路径
def process_aar_init():
    file = open(path, "r", encoding="utf-8", errors="ignore")

    lines = file.readlines()
    # index = 0
    # for line in file:
    #     index += 1
    # pass

    # print(linecache.count())
    # print(lines)
    for line in lines:
        if local_output == line.strip():
            print(local_output)
            if not is_local:
                line.replace(line.strip(), nexus_output)
        if nexus_output == line.strip():
            if is_local:
                line.replace(line.strip(),local_output)

    print(lines)
    with open("aar_init_script_new.grade", "w") as f:
        for item in lines:
            f.writelines(item)
        f.close()


if __name__ == '__main__':
    process_aar_init()
