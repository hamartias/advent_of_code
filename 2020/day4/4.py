

def make_passport_dict(l):
    l = [tuple(s.split(":")) for s in l]
    d = {e[0]: e[1] for e in l}
    return d

required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

valid_rules = {
"byr": lambda x: len(x) == 4 and 1920 <= int(x) <= 2002,
"iyr": lambda x: len(x) == 4 and 2010 <= int(x) <= 2020,
"eyr": lambda x: len(x) == 4 and 2020 <= int(x) <= 2030,
"hgt": lambda x: check_hgt(x),
"hcl": lambda x: check_hcl(x),
"ecl": lambda x: check_ecl(x),
"pid": lambda x: check_pid(x),
}

def check_hgt(x):
    if len(x) < 2:
        return False
    end = x[len(x)-2::]
    if end == "cm":
        num = int(x[:-2])
        if 150 <= num <= 193:
            return True
        return False
    elif end == "in":
        num = int(x[:-2])
        if 59 <= num <= 76:
            return True
        return False
    else:
        return False

def check_hcl(x):
    res = x[0] == "#" and len(x) == 7
    for c in x[1:]:
        ok = (c in "0123456789") or (c in "abcdef")
        res = res and ok
    return res

def check_ecl(x):
    return x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def check_pid(x):
    res = len(x) == 9
    for c in x:
        if c not in "0123456789":
            return False
    return res

def is_valid_passport(p):
    for field in required:
        if field not in p:
            return False
        validation_check = valid_rules[field]
        if not validation_check(p[field]):
            print("failing on, %s: %s" % (field, p[field]))
            return False

    return True

def test_case(field, value):
    rule = valid_rules[field]
    got = rule(value)
    return got

def dumb_test():
    cases = [
            ("byr", "2002", True),
            ("byr", "2003", False),

            ("hgt", "60in", True),
            ("hgt", "190cm", True),
            ("hgt", "190in", False),
            ("hgt", "190", False),

            ("hcl", "#123abc", True),
            ("hgt", "#123abz", False),
            ("hgt", "123abc", False),

            ("ecl", "brn", True),
            ("ecl", "wat", False),

            ("pid", "000000001", True),
            ("pid", "0123456789", False)

    ]
    for c in cases:
        f, v, e = c
        if test_case(f, v) != e:
            print(c)

def main():
    with open("input.txt") as f:
        passport = []
        count = 0
        for l in f:
            if len(l) == 1:
                pdict = make_passport_dict(passport)
                if is_valid_passport(pdict):
                    print("valid: ", pdict)
                    count += 1
                passport = []
                continue
            else:
                passport += l.rstrip().split(" ")

        pdict = make_passport_dict(passport)
        if is_valid_passport(pdict):
            print("valid: ", pdict)
            count += 1
        passport = []
        print(count)

if __name__ == "__main__":
    main()
    #dumb_test()
