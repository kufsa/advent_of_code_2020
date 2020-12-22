

def char_in_str(c, s):
    counter = 0
    for i in s:
        if c == i:
            counter += 1
    return counter

if __name__ == '__main__':
    source_file = open('input', 'r').readlines()
    valid_passwords = []
    for line in source_file:
        counter, char, password = line.replace(':', '').split()
        c_min, c_max = counter.split('-')

        cis = char_in_str(char, password)
        if cis >= int(c_min) and cis <= int(c_max):
            valid_passwords.append(password)

    print(len(valid_passwords))


