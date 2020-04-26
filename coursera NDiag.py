'''
Backtracking Algorithm to solve the NDiagonals Puzzle
Adapted from https://github.com/mattcollier/diagonals#sample-output

Try the puzzle here: http://dm.compsciclub.ru/app/quiz-n-diagonals 

'''
#Ultility displays the grid
def printGrid(grid):
    for i in range(len(grid)):
        print()
        for j in range(len(grid)):
            print(grid[i][j],end=' ')
        print()
    print()
    
'''
Use the following encoding
 _  ,  +1  ,   -1   represent empty cell ,  \  ,  /

The cells sharing an edge with a cell with a ±1 cannot contain a ∓1.

If a cell contains a 1, the adjacent cells to the top-left 
and bottom-right cannot also contain a 1.

If a cell contains a -1, the adjacent cells to the bottom-left 
and top-right cannot also contain a -1.

'''

#Check 4 directions: West, West North West, North, Eest North East
def check_neighbors(row, col, value):
    global grid

    # check West
    if(col > 0):
        W = grid[row][col - 1]
        if (W != 0 and W != value):
            return False
    # check WNW, N, ENE
    if row > 0:
        # check North 
        N = grid[row - 1][col];
        if (N != 0 and N != value):
            return False

        # check North West North cannot be -1
        if (value == 1 and col > 0):
            NWN = grid[row - 1][col -1];
            if (NWN != 0 and NWN != -1):
                return False

        # check East North East cannot be +1
        if (value == -1 and col < size - 1):
            ENE = grid[row - 1][col + 1]
            if (ENE != 0 and ENE != 1):
                return False

    return True

'''
Backtrack until reminaing diagonals equals 0
'''

def extend(row, col, remainingDiags):
    global size
    global grid
    global ct

    if remainingDiags == 0:
        ct+=1
        print('Solution:',ct)
        printGrid(grid)
        return

    if row == size:
        return

    nextRow = row
    nextCol = col + 1
    if nextCol == size:
        nextRow += 1
        nextCol = 0

    # putting -1 first here optimizes for the known solution
    # -1 is /, 1 is \, 0 is blank cell
    for diagonalType in [1, -1, 0]:
        # zero (blank cell) always works, no need to test
        if diagonalType == 0:
            grid[row][col] = diagonalType
            extend(nextRow, nextCol, remainingDiags)
        else:
            if check_neighbors(row, col, diagonalType):
                # the diagonal works, put it in
                grid[row][col] = diagonalType
                extend(nextRow, nextCol, remainingDiags - 1)


# setup a grid size X size
size = 5
ct = 0

grid = [[0 for i in range(size)] for j in range(size)]

extend(0, 0, 16)

'''
Solution: 1

-1 -1 -1 0 1 

0 0 -1 0 1 

1 1 0 1 1 

1 0 -1 0 0 

1 0 -1 -1 -1 

Solution: 2

-1 0 1 1 1 

-1 0 1 0 0 

-1 -1 0 -1 -1 

0 0 1 0 -1 

1 1 1 0 -1 
'''




