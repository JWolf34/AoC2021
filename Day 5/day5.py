import os


with open(os.path.abspath(os.path.join(os.path.dirname(__file__),"5.txt"))) as f:
    input = f.read().splitlines()

coordinates = []
for line in input:
    coord1, coord2 = line.split('->')
    coordinates.append(((tuple(map(int, coord1.split(',')))), (tuple(map(int, coord2.split(','))))))
    
def part1():
    vent_map = []

    for i in range (0, 1000):
        vent_row = []
        for j in range (0, 1000):
            vent_row.append(0)
        vent_map.append(vent_row)

    vent = open('vent.txt', 'w')
    vent.write(' '.join(str(c) for c in vent_map))
    vent.close()
    
    for coords in coordinates:
        x1 = coords[0][0]
        y1 = coords[0][1]

        x2 = coords[1][0]
        y2 = coords [1][1]


        if (x1 == x2):
            if y1 > y2:
                y1, y2 = y2, y1
            for y in range (y1, y2+1):
                vent_map[x1][y] += 1
        if (y1 == y2):
            if x1 > x2:
                x1, x2 = x2, x1
            for x in range(x1, x2+1):
                vent_map[x][y1] += 1



    num_overlap = 0

    for i in range (0, len(vent_map)):
        for j in range (0, len(vent_map[i])):
            if vent_map[i][j] >= 2:
                num_overlap += 1

    print("Number of overlapping points: {}".format(num_overlap))


def part2():
    vent_map = []

    for i in range (0, 1000):
        vent_row = []
        for j in range (0, 1000):
            vent_row.append(0)
        vent_map.append(vent_row)

    vent = open('vent.txt', 'w')
    vent.write(' '.join(str(c) for c in vent_map))
    vent.close()
    
    for coords in coordinates:
        x1 = coords[0][0]
        y1 = coords[0][1]

        x2 = coords[1][0]
        y2 = coords [1][1]

        if (x1 == x2):
            if y1 > y2:
                y1, y2 = y2, y1
            for y in range (y1, y2+1):
                vent_map[x1][y] += 1
        elif (y1 == y2):
            if x1 > x2:
                x1, x2 = x2, x1
            for x in range(x1, x2+1):
                vent_map[x][y1] += 1

        else:
            dx = abs(x2-x1)
            dy = abs(y2-y1)

            yslope = 0
            if y1 < y2:
                yslope = 1
            else:
                yslope = -1

            xslope = 0
            if x1 < x2:
                xslope = 1
            else:
                xslope = -1
        
            x = x1
            y = y1
            for i in range(0, dx + 1):
                vent_map[x][y] += 1

                x += xslope
                y += yslope 
        
        
    num_overlap = 0

    for i in range (0, len(vent_map)):
        for j in range (0, len(vent_map[i])):
            if vent_map[i][j] >= 2:
                num_overlap += 1

    print("Number of overlapping points: {}".format(num_overlap))


if __name__ == '__main__':
    #part1()
    part2()