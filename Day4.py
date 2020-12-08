def isvalid(passport):
    byr_valid = 1920 <= int(passport['byr']) <= 2002
    iyr_valid = 2010 <= int(passport['iyr']) <= 2020
    eyr_valid = 2020 <= int(passport['eyr']) <= 2030

    hgt_valid = False
    if passport['hgt'][-2:] == 'in':
        hgt_valid = 59 <= int(passport['hgt'][:-2]) <= 76
    elif passport['hgt'][-2:] == 'cm':
        hgt_valid = 120 <= int(passport['hgt'][:-2]) <= 193

    valid_char = '1234567890abcdef'

    hcl_valid = False
    if passport['hcl'][0] == '#':
        hcl_valid = True
        for char in passport['hcl'][-1:]:
            if char not in valid_char:
                hcl_valid = False
                break

    if passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        ecl_valid = True
    else:
        ecl_valid = False
    pid_valid = False
    if len(passport['pid']) == 9:
        try:
            int(passport['pid'])
            pid_valid =True
        except ValueError:
            pid_valid = False

    return byr_valid and iyr_valid and eyr_valid and hgt_valid and hcl_valid and ecl_valid and pid_valid


keys1 = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
keys2 = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
keys1.sort()
keys2.sort()
with open('Day4.txt', 'r') as fp:
    data = fp.read()

data = data.split('\n\n')
data = [d.replace('\n', ' ').split(' ') for d in data]
c = 0
valid = 0
for d in data:
    passport = dict([f.split(':') for f in d])
    passport_keys = list(passport.keys())
    passport_keys.sort()
    if passport_keys == keys1 or passport_keys == keys2:
        if isvalid(passport):
            valid += 1

print(valid)