import os
from posixpath import split
from collections import OrderedDict

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
                col = index % 5 
                board.visited[index // 5][index % 5] = 'x'
                has_bingo = check_for_bingo(board, index)
                if(has_bingo):
                    print('Bingo! Index = {}'.format(index))
                    print(board.visited)
                    print("Sum unvisited: {}".format(sum_unvisited_number(board) * number))
                    exit()

def check_for_bingo(board, index):
    row = index // 5
    col = index % 5 

    has_bingo = False
    
    # Check row for bingo
    if '' not in board.visited[row]:
        has_bingo = True
        return has_bingo


    for r in range (0, len(board.visited)):
        if board.visited[r][col] == '':
            has_bingo = False
            return has_bingo
        else:
            has_bingo = True
    
    return has_bingo

def sum_unvisited_number(board):
    sum = 0

    for row in range(0, len(board.visited)):
        for col in range (0, len(board.visited[row])):
            if board.visited[row][col] == '':
                sum += board.data[row*5 + col]

    return sum


def part2():
    numbers = list(map(int, input[0].split(',')))
    
    boards = [Board(board_data) for board_data in input[1:]]

    winners = []
    scores = []

    for number in numbers:
        for board in boards:
            if number in board.data and board not in winners:
                index = board.data.index(number)
                row = index // 5
                col = index % 5 
                board.visited[index // 5][index % 5] = 'x'
                has_bingo = check_for_bingo(board, index)
                if(has_bingo):
                    print('Bingo! Index = {}'.format(index))
                    print(board.visited)
                    print("Sum unvisited: {}".format(sum_unvisited_number(board) * number))
                    winners.append(board)
                    scores.append(sum_unvisited_number(board) * number)
    
    print("----------------------------------------------")
    print("Sum of last board to win: {}".format(scores[-1]))


if __name__ == '__main__':
    #part1()
    part2()
