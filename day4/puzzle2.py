from dataclasses import dataclass, field
from typing import Optional

import re


required_values = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])


@dataclass
class Passport:
    byr: int
    iyr: int
    eyr: int
    hgt: int
    hcl: str
    ecl: str
    pid: str  # yes it's an in but we de re matching on it...
    cid: Optional[int] = 0

    hgt_unit:str = field(init=False)

    def __post_init__(self):
        self.byr = int(self.byr)
        self.iyr = int(self.iyr)
        self.eyr = int(self.eyr)
        # self.pid = int(self.pid)

        if self.hgt[-2:] in ('cm', 'in'):
            self.hgt_unit = self.hgt[-2:]
            self.hgt = int(self.hgt[:-2])
        else:
            raise AttributeError('Height not valid')




def validate_passport(passport):

    try:
        passport = Passport(**passport)
    except Exception as e:
        print(e)
        return False

    hair_color_re = re.compile('\\#[0-9a-f]{6}')
    pid_re = re.compile('^\d{9}$')

    if passport.byr < 1920 or passport.byr > 2002:
        print('wrong bry', passport.byr)
        return False
    elif passport.iyr < 2010 or passport.iyr > 2020:
        print('wrong iyr')
        return False
    elif passport.eyr < 2020 or passport.eyr > 2030:
        print('wrong eyr')
        return False
    elif passport.hgt_unit == 'cm' and (passport.hgt < 150 or passport.hgt > 193):
        print('wrong cm height')
        return False
    elif passport.hgt_unit == 'in' and (passport.hgt < 59 or passport.hgt > 76):
        print('wrong in height')
        return False
    elif not hair_color_re.match(passport.hcl):
        print('wrong haircolor', passport.hcl)
        return False
    elif passport.ecl not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
        print('wrong ecl')
        return False
    elif not pid_re.match(passport.pid):
        print('wrong pid')
        return False

    return True


if __name__ == '__main__':
    source_file = open('input', 'r').readlines()
    passports = []

    passport = {}
    for line in source_file:
        items = line.strip().split()
        if len(line) == 1:
            if validate_passport(passport):
                passports.append(passport)
            passport = {}

        for item in items:
            k, v = item.split(':')
            passport[k] = v


    print(len(passports))

