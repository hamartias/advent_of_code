
testf = "test_input.txt"
realf = "input.txt"

def load_program(filename):
    program = []
    with open(filename) as f:
        for l in f:
            program.append(l.rstrip().lstrip())
    return program

def parse_arg(arg):
    sign = -1 if arg[0] == '-' else 1
    val = int(arg[1:])
    return sign * val

def eval_program(program):
    program = [l.split(" ") for l in program]
    visited = set()
    acc = 0
    ip = 0
    while ip < len(program):
        if ip in visited:
            return acc, True
            break
        instr, arg = program[ip]
        visited.add(ip)
        if instr == "nop":
            ip += 1
        elif instr == "acc":
            acc += parse_arg(arg)
            ip += 1
        elif instr == "jmp":
            ip += parse_arg(arg)
    return acc, False

def generate_candidate_programs(program):
    candidates = []
    for i, l in enumerate(program):
        instr, val = l.split(" ")
        if instr == "jmp":
            copy = [l for l in program]
            copy[i] = "nop " + val
            candidates.append(copy)
        elif instr == "nop":
            copy = [l for l in program]
            copy[i] = "jmp " + val
            candidates.append(copy)
    return candidates

def main():
    p = load_program(realf)
    candidates = generate_candidate_programs(p)
    for c in candidates:
        acc, looped = eval_program(c)
        if not looped:
            print(acc)

if __name__ == "__main__":
    main()
