import os
from posixpath import split

class Board:
    def __init__ (self, board_data):
        self.data = list(map(int, board_data.replace('\n', ' ').split()))
        self.visited = []
        for i in range(0, 5):
            self.visited.append(['']*5)


with open(os.path.abspath(os.path.join(os.path.dirname(__file__),"4.txt"))) as f:
    input = f.read().split('\n\n')



def part1():
    numbers = list(map(int, input[0].split(',')))
    
    boards = [Board(board_data) for board_data in input[1:]]

    for number in numbers:
        for board in boards:
            if number in board.data:
                index = board.data.index(number)
                row = index // 5
                col = index % 5 - 1
                board.visited[index // 5][index % 5] = 'x'
                has_bingo = check_for_bingo(board, index)
                if(has_bingo):
                    print('Bingo! Index = {}'.format(index))
                    print(board.visited)
                    exit()

def check_for_bingo(board, index):
    row = index // 5
    col = index % 5 - 1

    if col == -1:
        col = 0

    has_bingo = False
    
    # Check row for bingo
    if '' not in board.visited[row]:
        has_bingo = True
        return has_bingo


    for r in range (0, row):
        if board.visited[r][col] == '':
            has_bingo = False
            return has_bingo
        else:
            has_bingo = True
    
    return has_bingo


def part2():
    pass


if __name__ == '__main__':
    part1()
    part2()
