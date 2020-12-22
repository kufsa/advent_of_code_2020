

if __name__ == '__main__':
    source1 = open('input', 'r').readlines()
    while len(source1) > 0:
        source2 = source1.copy()
        v1 = int(source1.pop().strip())
        while len(source2) > 0:
            v2 = int(source2.pop().strip())
            for v3 in source2:
                v3 = int(v3)
                if v1 + v2  + v3 == 2020:
                    print(v1 * v2 * v3)
                    exit()

