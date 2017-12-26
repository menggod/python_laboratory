def find_it(seq):
    num_map = {}
    for num in seq:
        if num in num_map:
            num_map[num] = num_map.get(num) +1
        else:
            num_map[num] = 1
    for item in num_map.items():
        if item[1]%2!=0:
            return item[0]

print(find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]))
