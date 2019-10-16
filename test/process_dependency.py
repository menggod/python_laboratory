path = "dependency"
# 传入要读的文件路径

file = open(path, "r", encoding="utf-8", errors="ignore")


def process_depend():
    depend_map = {}
    while True:
        depend_text = file.readline()  # 表示一次读取一行
        if not depend_text:
            # 读到数据最后跳出，结束循环。数据的最后也就是读不到数据了，mystr为空的时候
            break
        # depend_map.update(depend_text, depend_text)
        depend_map[depend_text[13]] = depend_text
    sorted(depend_map.items(), key=lambda x: x[0])
    print(depend_map)


if __name__ == '__main__':
    process_depend()
