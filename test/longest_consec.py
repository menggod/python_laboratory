def longest_consec(strarr, k):
    if len(strarr) == 0 or k > len(strarr) or k <=0:
        return ""
    else:
        max_string = ""
        for index in range(len(strarr)):
            list_string = "".join(strarr[index:index + k]);
            if len(list_string) > len(max_string):
                max_string = list_string
        return max_string

print(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 2))