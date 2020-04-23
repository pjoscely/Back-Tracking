#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 13:42:45 2020

@author: joscelynec
"""
#Driver function to kick off the recursion

def solveLatinSquare(board):
    return solveLatinSquareCell(0, 0, board)

"""
This function chooses a placement for the cell at (row, col)
and continues solving based on the rules we define.

The strategy:
We will start at row 0.
We will place distinct values 1, 2, 3, ..., n every column in that row.
When we reach the last column we move to the next row.
If this is past the last row( row == board.length) we are done.
A Latin Square has been generated.
"""
def solveLatinSquareCell(row, col, board):

#Have we finished placements in all columns for 3the row we are working on?
    if (col == len(board)):
#Yes. Reset to col 0 and advance the row by 1. We will work on the next row

        col = 0
        row += 1

#Have we completed placements in all rows? If so then we are done.
#If not, drop through to the logic below and keep solving things.
        if (row == len(board)):
            return True; # Entire board has been filled without conflict.


#Try all values 1 through n in the cell at (row, col).
#Recurse on the placement if it doesn't break the constraints of the Latin Square.
    for val in range(1, len(board)+1):

#Apply constraints. We will only add the value to the cell if
#adding it won't cause us to .

        if (canPlaceValue(board, row, col, val)):
            board[row][col] = val
            if (solveLatinSquareCell(row, col + 1, board)):#recurse with our VALID placement
                return True;    

#Undo assignment to this cell. No values worked in it meaning that
#previous states put us in a position we cannot solve from. Hence,
#we backtrack by returning "false" to our caller.

    board[row][col] = 0
    return False #No valid placement was found, this path is faulty, return false 



#Will the placement at (row, col) break the Latin Square properties?

def canPlaceValue(board, row, col, valToPlace):
    #Check column constraint. For each row, we do a check on column "col"
    for element in board:
        if (valToPlace == element[col]):
            return False;
    
    #Check row constraint. For each column in row "row", we do a check.
    for i in range(len(board)): 
        if (valToPlace == board[row][i]): 
            return False;
    
    
    return True
   
bd = [[0,0],
      [0,0]]
print(solveLatinSquare(bd))
print(bd)

bd1 = [[0,0,0,0],
      [0,0,0,0],
      [0,0,0,0],
      [0,0,0,0]]
print(solveLatinSquare(bd1))
print(bd1)

#This produces a permuted Latin Square 
bd2 = [[7,9,0,0,0,0,0,0,3],
       [0,0,0,0,0,0,0,6,0],
       [8,0,1,0,0,4,0,0,2],
       [0,0,5,0,0,0,0,0,0],
       [3,0,0,1,0,0,0,0,0],
       [0,4,0,0,0,6,2,0,9],
       [2,0,0,0,3,0,0,0,6],
       [0,3,0,6,0,5,4,2,1],
       [0,0,0,0,0,0,0,0,0]]
print(solveLatinSquare(bd2))
print(bd2)


#Takes some time to ruu
'''
a = [x[:] for x in [[0] * 15] * 15]
print(solveLatinSquare(a))
print(a)
'''

'''
True
[[1, 2], 
[2, 1]]

True
[[1, 2, 3, 4], 
[2, 1, 4, 3], 
[3, 4, 1, 2], 
[4, 3, 2, 1]]

True
[[1, 2, 4, 5, 6, 7, 9, 3, 8], 
[4, 1, 2, 3, 5, 9, 6, 8, 7], 
[5, 6, 3, 7, 4, 8, 1, 9, 2], 
[6, 7, 1, 2, 9, 3, 8, 4, 5], 
[7, 5, 6, 9, 8, 2, 3, 1, 4], 
[3, 8, 5, 4, 7, 1, 2, 6, 9], 
[2, 3, 9, 8, 1, 4, 7, 5, 6], 
[9, 4, 8, 1, 2, 6, 5, 7, 3], 
[8, 9, 7, 6, 3, 5, 4, 2, 1]]

#Five minutes for an obvious Latin Square
True
[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 
[2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 15, 13], 
[3, 4, 1, 2, 7, 8, 5, 6, 11, 12, 9, 10, 15, 13, 14], 
[4, 3, 2, 1, 8, 7, 6, 5, 12, 13, 14, 15, 9, 10, 11], 
[5, 6, 7, 8, 1, 2, 3, 4, 13, 11, 15, 14, 10, 9, 12], 
[6, 5, 8, 7, 2, 1, 4, 3, 14, 15, 10, 13, 11, 12, 9], 
[7, 8, 5, 6, 3, 4, 1, 2, 15, 14, 13, 9, 12, 11, 10], 
[8, 9, 10, 11, 12, 13, 14, 15, 1, 2, 3, 4, 5, 6, 7], 
[9, 7, 11, 10, 13, 12, 15, 14, 2, 1, 4, 3, 6, 5, 8], 
[10, 11, 6, 9, 14, 15, 12, 13, 3, 4, 1, 2, 7, 8, 5], 
[11, 10, 9, 5, 15, 14, 13, 12, 4, 3, 2, 1, 8, 7, 6], 
[12, 13, 14, 15, 4, 9, 10, 11, 5, 6, 7, 8, 1, 2, 3], 
[13, 12, 15, 14, 9, 3, 11, 10, 6, 5, 8, 7, 2, 1, 4], 
[14, 15, 12, 13, 10, 11, 2, 9, 7, 8, 5, 6, 3, 4, 1], 
[15, 14, 13, 12, 11, 10, 9, 1, 8, 7, 6, 5, 4, 3, 2]]

'''






