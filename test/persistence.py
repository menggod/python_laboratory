count = 0


def persistence(n):
    global count
    if type(n) == int:
        if len(str(n)) == 1:
            print(count)
            # return count
        else:
            count += 1
            product = 1
            for x in str(n):
                product *= int(x)
            persistence(product)
    return count

print(persistence(999))
