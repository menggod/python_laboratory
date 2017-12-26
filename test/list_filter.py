def iq_test(numbers):
    # your code here
    numbers = numbers.split(" ")
    if len(numbers) >= 3:
        sum = 0
        for x in range(3):
            sum += int(numbers[x])
        if sum % 2 == 0:
            for number in numbers:
                if int(number) % 2 == 0:
                    return numbers.index(number)
        else:
            for number in numbers:
                if int(number) % 2 != 0:
                    return numbers.index(number)


temp = "2 4 7 8 10"
print(iq_test("2 4 7 8 10"))
# print(temp.split(" "))
