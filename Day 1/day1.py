import os

with open(os.path.abspath(os.path.join(os.path.dirname(__file__),"input.txt"))) as f:
    input = list(map(int, f.read().splitlines()))

def part1():
    numIncreases = 0
    prevdepth = input[0]

    for depth in input:
        if (prevdepth < depth):
            numIncreases += 1
            print(("{} -> {} INCREASED").format(prevdepth, depth))
        else:
            print(("{} -> {} DECREASED").format(prevdepth, depth))
        prevdepth = depth

    print(numIncreases)

def part2():
    numIncreases = 0
    prevwindow = input[0] + input[1] + input[2]

    for i in range(0, len(input)):
        if (i + 3 >= len(input)+1):
            break
        window = input[i] + input[i+1] + input[i+2]
        if(prevwindow < window):
            numIncreases += 1
            print(("{} -> {} INCREASED").format(prevwindow, window))
        else:
            print(("{} -> {} DECREASED").format(prevwindow, window))
        prevwindow = window
    print(numIncreases)

if __name__ == "__main__":
    part1()
    part2()
