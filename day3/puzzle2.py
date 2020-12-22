


if __name__ == '__main__':

    source_file = open('input', 'r').readlines()

    trees = []
    slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]

    for mod_x, mod_y in slopes:
        x, y = 0, 0
        t = 0
        while y < len(source_file):
            line = source_file[y].strip()

            mod_char = x % len(line)
            if line[mod_char] == '#':
                t += 1

            x += mod_x
            y += mod_y
        trees.append(t)

    print('Trees passed: ', trees)

    mt = 1
    for t in trees:
        mt = mt * t
    print('total: ', mt)
