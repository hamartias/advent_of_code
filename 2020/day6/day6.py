def make_groups():
    groups = []
    letters = ""
    with open("input.txt") as f:
        for line in f:
            if line == "\n":
                groups.append(letters)
                letters = ""
            else:
                letters += line
    groups.append(letters)
    return groups

def get_common(group):
    unique = set(group)
    if '\n' in unique: unique.remove('\n')
    items = group.split('\n')[:-1]
    common = []
    for u in unique:
        ok = True
        for e in items:
            if u not in e:
                ok = False
        if ok: common.append(u)
    return common


if __name__ == "__main__":
    groups = make_groups()
    common = [get_common(g) for g in groups]
    print(sum(map(len, common)))
