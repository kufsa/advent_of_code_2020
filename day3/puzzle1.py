


if __name__ == '__main__':

    source_file = open('input', 'r').readlines()
    x = 0

    trees = 0

    for line in source_file:
        line = line.strip()

        mod_char = x % len(line)
        if line[mod_char] == '#':
            trees += 1

        x += 3

    print('Trees passed: ', trees)
