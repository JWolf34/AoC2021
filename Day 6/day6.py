import os

with open(os.path.abspath(os.path.join(os.path.dirname(__file__),"6.txt"))) as f:
    input = list(map(int,f.read().split(',')))

fish = input

def part1():
    length_of_study = 80
    day = 0

    while day < length_of_study:
        new_fish = 0
        for i in range(0, len(fish)):
            if fish[i] == 0:
                new_fish += 1
                fish[i] = 6
            else:
                fish[i] -= 1

        for i in range(0, new_fish):
            fish.append(8)
    
        day += 1
        print(str(len(fish)) + " Day: {}".format(day))
    
    print()
    print('Total fish after {} days: {}'.format(length_of_study, len(fish)))




def part2():
    length_of_study = 256
    day = 0

    fish_ages = {}
    for i in range(0, 9):
        fish_ages[i] = fish.count(i)

    print(fish_ages)
    
    while day < length_of_study:
        new_fish = 0
        fish_0 = fish_ages[0]
        fish_ages[0] = 0

        for age in range(1, 9):
            fish_ages[age-1] = fish_ages[age]

        fish_ages[6] += fish_0

        fish_ages[8] = fish_0

        day += 1
        print(str(len(fish)) + " Day: {}".format(day, sum(fish_ages.values())))
    
    print()
    print('Total fish after {} days: {}'.format(length_of_study, sum(fish_ages.values())))


if __name__ == '__main__':
    #part1()
    part2()