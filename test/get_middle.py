def get_middle(s):
    # your code here
    length = len(s)
    if length % 2 == 0:
        return s[length / 2 - 1:length / 2 + 1]
    else:
        return s[length / 2:length / 2 + 1]

    print(get_middle("32234"))
