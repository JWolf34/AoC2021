import os

with open(os.path.abspath(os.path.join(os.path.dirname(__file__),"7.txt"))) as f:
    input = list(map(int,f.read().split(',')))


def part1():
    best_position = -1
    least_fuel = 0
    for i in range(0, len(input)):
        fuel_used = 0
        for j in range(0, len(input)):
            fuel_used += abs(input[j] - i)
        if best_position == -1:
            best_position = i
            least_fuel = fuel_used
        elif fuel_used < least_fuel:
            best_position = i
            least_fuel = fuel_used
    print("Horizonatl position that costs the least fuel: {}".format(best_position))
    

def part2():
    pass



if __name__ == '__main__':
    part1()
    part2()