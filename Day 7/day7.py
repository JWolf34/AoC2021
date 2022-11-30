import statistics
import os

with open(os.path.abspath(os.path.join(os.path.dirname(__file__),"input.txt"))) as f:
    input = f.read()


def part1():
    positions = [int(i) for i in input.split(',')]
    
    fuel_spent = 100000000
    
    for i in range (0, max(positions)):
        fuel_calculated = 0
        for p in positions:
            fuel_calculated += abs(p - i)
        fuel_spent = min(fuel_spent, fuel_calculated)
        
    print(fuel_spent)

def part2():
    positions = [int(i) for i in input.split(',')]
    
    fuel_spent = 100000000
    
    for i in range (0, max(positions)):
        fuel_calculated = 0
        for p in positions:
            n = abs(p-i)
            fuel_calculated += n*(n+1)/2
        fuel_spent = min(fuel_spent, fuel_calculated)

    print(fuel_spent)



if __name__ == '__main__':
    part2()