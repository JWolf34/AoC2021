import os


with open(os.path.abspath(os.path.join(os.path.dirname(__file__),"2.txt"))) as f:
    input = f.read().splitlines()
    input = [direction.split() for direction in input]


def part1():
    horizontal = 0
    depth = 0

    for direction in input:
        if direction[0] == 'forward':
            horizontal += int(direction[1])
        if direction[0] == 'down':
            depth += int(direction[1])
        if direction[0] == 'up':
            depth -= int(direction[1])

    print('Final Horizontal Distance: {}'.format(horizontal))
    print('Final Depth: {}'.format(depth))
    print('Multiplied: {}'.format(horizontal*depth))
        


def part2():
    horizontal = 0
    depth = 0
    aim = 0

    for direction in input:
        if direction[0] == 'forward':
            horizontal += int(direction[1])
            depth += aim * int(direction[1])
        if direction[0] == 'down':
            aim += int(direction[1])
        if direction[0] == 'up':
            aim -= int(direction[1])

    print('Final Horizontal Distance: {}'.format(horizontal))
    print('Final Depth: {}'.format(depth))
    print('Multiplied: {}'.format(horizontal*depth))



if __name__ == "__main__":
    part1()
    print('-----------------------------')
    part2()
