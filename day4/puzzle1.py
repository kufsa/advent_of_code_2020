

if __name__ == '__main__':
    source_file = open('input', 'r').readlines()
    required_values = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
    passports = []

    passport = {}
    for line in source_file:
        items = line.strip().split()
        if len(line) == 1:
            actual_values = set([k for k in passport])
            print(actual_values)
            if required_values - actual_values == set():

                passports.append(passport)
            passport = {}

        for item in items:
            print(item)
            k, v = item.split(':')
            passport[k] = v


    print(len(passports))

