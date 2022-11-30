import os

with open(os.path.abspath(os.path.join(os.path.dirname(__file__),"input.txt"))) as f:
    input = f.readlines()


def part1():
    legend = {
        2 : "1",
        4 : "4",
        3 : "7",
        8 : "8"
    }

    outputs = []
    for i in range(0, len(input)):
        outputs.append(input[i].split('|')[1].split())
    
    num_easy_digits = 0
    for j in outputs:
        for k in j:
            if len(k) in legend.keys():
                num_easy_digits += 1

    print(num_easy_digits)


def part2():
    pass


if __name__ == '__main__':
    part1()
    part2()