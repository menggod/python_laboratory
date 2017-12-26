
def maskify(cc):
    if len(cc) <= 4:
        return cc
    else:
        index = len(cc) - 4
        return (index * "#" + (cc[index:]))




