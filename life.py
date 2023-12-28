import random
import time

def createBoard(x, y):
    res = [[0]*x] * y
    return res

def setRandomBoard(board):
    res = []
    for row in board:
        line = list(map(lambda x: random.randrange(2), row))
        res.append(line)
    return res

def printBoard(board):
    print("-" * len(board[0]))
    for row in board:
        prettyRow  = prettyPrintRow(row)
        print(prettyRow)
    print("-" * len(row))
    print("\n")

def prettyPrintRow(row):
    res = "|"
    for cell in row:
        if cell == 0:
            res += " "
        else:
            res += "#"
    res += "|"
    return res

def nextState(board):
    newBoard = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
    #live with 0-1 neighbours = dead
    #live with 2-3 neighbours = live
    #live with >3 live neighbours = dead
    #dead with 3 live neighbours = live
    for x in range(0,len(board)):
        for y in range(0,len(board[0])):
            live = board[x][y] == 1
            newCell = None
            neighbours = getNeighbours(x,y, board)

            if not live:
                if neighbours == 3:
                    newCell = 1
                else: 
                    newCell = 0
            else:
                if neighbours <= 1:
                    newCell = 0
                elif neighbours <= 3:
                    newCell = 1
                else:
                    newCell = 0
            newBoard[x][y] = newCell
    return newBoard

def getNeighbours(x, y, board): 
    neighbours = 0
    xStart = 0 if x == 0 else x-1
    xEnd = x+1 if x == len(board)-1 else x+2
    yStart = 0 if y == 0 else y-1
    yEnd = y+1 if y == len(board[0])-1 else y+2

    if x == 0:
        xStart = x

    for row in range(xStart, xEnd):
        for col in range(yStart, yEnd):
            neighbours += board[row][col]
    if neighbours != 0:
        neighbours -= board[x][y] 
    return neighbours


def gameOfLife(x, y):
    board = setRandomBoard(createBoard(x,y))
    printBoard(board)
    while True:
        board = nextState(board)
        printBoard(board)
        time.sleep(3)



if __name__ == "__main__":
    gameOfLife(40,20)
