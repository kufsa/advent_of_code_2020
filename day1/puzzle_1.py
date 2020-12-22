


if __name__ == '__main__':
    source = open('input', 'r').readlines()
    while len(source) > 0:
        v1 = int(source.pop().strip())
        for v2 in source:
            v2 = int(v2)
            if v1 + v2 == 2020:
                print(v1 * v2)
                exit()

