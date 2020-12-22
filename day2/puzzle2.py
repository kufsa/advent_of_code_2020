


if __name__ == '__main__':
    source_file = open('input', 'r').readlines()
    valid_passwords = []
    for line in source_file:
        counter, char, password = line.replace(':', '').split()
        pos1, pos2 = counter.split('-')
        pos1, pos2 = int(pos1) - 1, int(pos2) - 1

        if (password[pos1] == char and password[pos2] != char) \
                or (password[pos1] != char and password[pos2] == char):
            valid_passwords.append(password)

    print(len(valid_passwords))


