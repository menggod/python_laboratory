import collections


def process_map():
    test_map = {'b': 4, 'q': 5, 'a': 2}
    test_map = sorted(test_map.items(), key=lambda x:x[1])
    print(test_map)


if __name__ == '__main__':
    process_map()
