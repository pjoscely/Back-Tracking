'''
https://math.stackexchange.com/questions/339387/how-to-solve-5x5-grid-with-16-diagonals
The link inspired the randomized solution below. Not the fastest, 
but nonetheless an amusing way to find solutions.
Try the puzzle here: http://dm.compsciclub.ru/app/quiz-n-diagonals 
'''
import random        


#displays the grid
def printGrid(grid):
    for i in range(len(grid)):
        print()
        for j in range(len(grid)):
            print(grid[i][j],end=' ')
        print()
    print()
      
'''
Given a list of moves, randomly return one move from the list
'''

def randomMove(moves):
    random.shuffle(moves)
    temp = moves.pop()
    return temp
   
'''
Counts the number of +1, -1 in a grid
'''
def getNumDiag(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if(grid[i][j] == 1 or grid[i][j] == -1):
                count+=1
    return count
    

'''
Returns a  list of possible moves for a cell with row = i and col = j 
based on the 8 neighbors of the cell
 0 ,  +1  ,   -1   represent empty cell ,  \  ,  /

The cells sharing an edge with a cell with a ±1 cannot contain a ∓1.

If a cell contains a 1, the adjacent cells to the top-left 
and bottom-right cannot also contain a 1.

If a cell contains a -1, the adjacent cells to the bottom-left 
and top-right cannot also contain a -1.

Here, cells containing a "1" have a diagonal running top-left to bottom-right, 
and cells containing a "-1" have a diagonal running the other way.
 
Cells containing _ do not have a diagonal at all.
'''
def getMoves(grid,i,j):
    #All moves are intially possible
    moves = [0, 1, -1]#All moves are intially possible
    
    #Check west and remove 
    if j - 1>=0:
        if(grid[i][j-1] == 1):
            if -1 in moves:
                moves.remove(-1)
        if(grid[i][j-1] == -1):
            if 1 in moves:
                moves.remove(1)
    
    #Check north and remove 
    if i - 1>=0:
        if(grid[i-1][j] == 1):
            if -1 in moves:
                moves.remove(-1)
        if(grid[i-1][j] == -1):
            if 1 in moves:
                moves.remove(1)
                
    #Check west north west and remove 
    if i - 1 >=0 and j -1 >=0:
        if(grid[i-1][j-1] == 1):
            if 1 in moves:
                moves.remove(1)
                
    #Check east north east and remove 
    if ((i -1 >=0) and (j+1 < len(grid))):
        if(grid[i-1][j+1] == -1):
            if -1 in moves:
                moves.remove(-1)
    
    return moves
    
'''
Randomly updates an grid and returns this updated grid 
'''

def fillGrid(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            moves = getMoves(grid,i,j)
            grid[i][j] =randomMove(moves)
    return grid  

#run until a solution is found and then display
size = 5
while(True):
    #intialize grid
    grid = [[0 for i in range(size)] for j in range(size)]
    temp = fillGrid(grid)
    if(getNumDiag(temp) == 16):
        print(printGrid(temp))

    
'''
Two solutions found after a few minutes
-1 0 1 1 1 

-1 0 1 0 0 

-1 -1 0 -1 -1 

0 0 1 0 -1 

1 1 1 0 -1 



-1 -1 -1 0 1 

0 0 -1 0 1 

1 1 0 1 1 

1 0 -1 0 0 

1 0 -1 -1 -1 


''' 