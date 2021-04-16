tf1 = "test_input.txt"
real = "input.txt"

def check_LR_values():
    instrs = get_input(real)
    d = {i[0]: set() for i in instrs}
    for i in instrs:
        k, v = i[0], int(i[1:])
        d[k].add(v)
    print(d['L'], d['R'])

def get_input(filename):
    out = []
    with open(filename) as f:
        for l in f:
            out.append(l.rstrip())
    return out

# north -> increase y only
# south -> decrease y only
# east -> decrease x only
# west -> increase x only
# forward -> increase current direction only
#   being facing east
#   L - left - CCW
#   R - right - CW
#   90 is one change
class Ship:
    def __init__(self, use_waypoint=False):
        self.direction_coeffs= {
            "N": (0, 1),
            "S": (0, -1),
            "E": (1, 0),
            "W": (-1, 0),
        }
        self.directions = ["E", "N", "W", "S"]
        self.current_direction = 0
        self.position = (0, 0)
        self.use_waypoint = use_waypoint
        self.waypoint = (10, 1)


    def handle_instruction(self, instr_string):
        k, v = instr_string[0], int(instr_string[1:])
        if k == "F":
            self.forward(v)
        elif k == "L" or k == "R":
            self.change_direction(k, v)
        else:
            self.change_position(k, v)

    def forward(self, units):
        if self.use_waypoint:
            for i in range(units): self.move_to_waypoint()
        else:
            self.change_position(self.get_direction(), units)

    def get_direction(self):
        return self.directions[self.current_direction]

    def move_to_waypoint(self):
        cx, cy = self.position
        dx, dy = self.waypoint
        self.position = (cx + dx, cy + dy)

    def change_direction(self, direction, amount):
        if amount > 4:
            amount = (amount // 90) % 4
        if self.use_waypoint:
            for i in range(amount):
                self.rotate_waypoint(direction)
        else:
            sign = 1 if direction == "L" else -1
            self.current_direction = (4 + self.current_direction + sign*amount) % 4

    def rotate_waypoint(self, direction):
        x, y = self.waypoint
        if direction == "L":
            self.waypoint = (-y, x)
        elif direction == "R":
            self.waypoint = (y, -x)

    def change_position(self, direction, units):
        coeffs = self.direction_coeffs[direction]
        if self.use_waypoint:
            cx, cy = self.waypoint
            self.waypoint = (cx + coeffs[0]*units, cy + coeffs[1]*units)
        else:
            cx, cy = self.position
            self.position = (cx + coeffs[0]*units, cy + coeffs[1]*units)

def solve(wp = False):
    instructions = get_input(real)
    ship = Ship(use_waypoint=wp)
    for instr in instructions:
        ship.handle_instruction(instr)
    print(ship.position)
    print(sum(map(abs, list(ship.position))))

def main():
    solve(wp=True)


if __name__ == "__main__":
    main()
