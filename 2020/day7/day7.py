
def parse_contain_list(contain_list):
    cl = contain_list.split(" ")
    cl = [e for e in cl if e != '']
    i = 0
    output = []
    while i < len(cl):
        output.append( (int(cl[i]), cl[i+1] + " " + cl[i+2]))
        i+=3
    return output

def parse_rule(line):
    line = line.rstrip()
    line = line.replace("bags", "bag")
    line = line.replace("bag", "")
    line = line.replace(",", "")
    line = line.replace(".", "")
    line = line.replace("no other", "")
    relation = line.split("contain")
    for i, e in enumerate(relation):
        relation[i] = e.lstrip().rstrip()
    relation[1] = parse_contain_list(relation[1])
    return relation

def parse_rules(filename):
    rules = []
    with open(filename) as f:
        for line in f:
            rules.append(parse_rule(line))
    return rules

def rule_contains(rule, bag_type):
    for contained in rule[1]:
        if contained[1] == bag_type:
            return True
    return False

def how_many_could_contain(bag_type, rules):
    type_stack = [bag_type]
    seen = set([bag_type])
    endpoints = set()
    while type_stack:
        this_type = type_stack.pop(0)
        found = False
        for rule in rules:
            if rule[0] not in seen and rule_contains(rule, this_type):
                type_stack.append(rule[0])
                found = True
        if this_type != bag_type:
            endpoints.add(this_type)
        seen.add(this_type)
    return len(endpoints)

def count_leaf_bags(start_type, rules):
    rulemap = {r[0]: r[1] for r in rules}

    def _inner(btype):
        if not rulemap[btype]:
            return 0

        print("counting, ", btype)
        count = 0
        for ingredient in rulemap[btype]:
            rec_count = _inner(ingredient[1])
            print("multiple of ", ingredient[0], "from ", btype)
            count += ingredient[0] * rec_count + ingredient[0]
        print("count was, ", count)
        return count

    return _inner(start_type)

def main():
    rules = parse_rules("input.txt")
    ans = how_many_could_contain("shiny gold", rules)
    ans2 = count_leaf_bags("shiny gold", rules)
    print(ans2)

if __name__ == "__main__":
    main()

