#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 05:35:00 2019
@author: joscelynec

Adapted from:
https://www.youtube.com/watch?v=JzONv5kaPJM&list=PLiQ766zSC5jM2OKVr8sooOuGgZkvnOCTI&index=16
https://github.com/bephrem1/backtobackswe/blob/master/Dynamic%20Programming%2C%20Recursion%2C%20%26%20Backtracking/sudokuSolver.java
"""
import math


#Driver function to kick off the recursion

def solveSudoku(board):
    return solveSudokuCell(0, 0, board)


"""
This function chooses a placement for the cell at (row, col)
and continues solving based on the rules we define.
  
Our strategy:
We will start at row 0.
We will solve every column in that row.
When we reach the last column we move to the next row.
If this is past the last row( row == board.length) we are done.
The whole board has been solved.
"""
def solveSudokuCell(row, col, board):

#Have we finished placements in all columns for 3the row we are working on?
    if (col == len(board)):
#Yes. Reset to col 0 and advance the row by 1. We will work on the next row

        col = 0
        row += 1

#Have we completed placements in all rows? If so then we are done.
#If not, drop through to the logic below and keep solving things.
        if (row == len(board)):
            return True; # Entire board has been filled without conflict.



#Skip non-empty entries. They already have a value in them.
    if (board[row][col] != 0):
        return solveSudokuCell(row, col + 1, board)

#Try all values 1 through 9 in the cell at (row, col).
#Recurse on the placement if it doesn't break the constraints of Sudoku.
    for val in range(1, len(board)+1):

#Apply constraints. We will only add the value to the cell if
#adding it won't cause us to break sudoku rules.

        if (canPlaceValue(board, row, col, val)):
            board[row][col] = val
            if (solveSudokuCell(row, col + 1, board)):#recurse with our VALID placement
                return True;
        

#Undo assignment to this cell. No values worked in it meaning that
#previous states put us in a position we cannot solve from. Hence,
#we backtrack by returning "false" to our caller.

    board[row][col] = 0
    return False #No valid placement was found, this path is faulty, return false


#Will the placement at (row, col) break the Sudoku properties?

def canPlaceValue(board, row, col, valToPlace):

#Check column constraint. For each row, we do a check on column "col"
    for element in board:
        if (valToPlace == element[col]):
            return False;
    
#Check row constraint. For each column in row "row", we do a check.
    for i in range(len(board)): 
        if (valToPlace == board[row][i]): 
            return False;

#Check region constraints.
    regionSize = (int)(math.sqrt(len(board))) #gives us the size of a sub-box

    I = row // regionSize;
    J = col // regionSize;


#This multiplication takes us to the EXACT top left of the sub-box. We keep the (row, col)
#of these values because it is important. It lets us traverse the sub-box with our double for loop.

    topLeftOfSubBoxRow = regionSize * I #the row of the top left of the block
    topLeftOfSubBoxCol = regionSize * J # the column of the tol left of the block

    for i in range(regionSize):
        for j in range(regionSize):

#i and j just define our offsets from topLeftOfBlockRow
#and topLeftOfBlockCol respectively
            if (valToPlace == board[topLeftOfSubBoxRow + i][topLeftOfSubBoxCol + j]):
                return False;
    return True #placement is valid


bd = [[0,0,0,4],
      [0,1,3,0],
      [0,2,4,0],
      [1,0,0,0]]
solveSudoku(bd)
print(bd)

bd1 = [[7,9,0,0,0,0,0,0,3],
       [0,0,0,0,0,0,0,6,0],
       [8,0,1,0,0,4,0,0,2],
       [0,0,5,0,0,0,0,0,0],
       [3,0,0,1,0,0,0,0,0],
       [0,4,0,0,0,6,2,0,9],
       [2,0,0,0,3,0,0,0,6],
       [0,3,0,6,0,5,4,2,1],
       [0,0,0,0,0,0,0,0,0]]
solveSudoku(bd1)
print(bd1)
"""
[[2, 3, 1, 4], 
[4, 1, 3, 2], 
[3, 2, 4, 1], 
[1, 4, 2, 3]]

[[7, 9, 2, 5, 6, 8, 1, 4, 3], 
 [4, 5, 3, 2, 1, 9, 8, 6, 7], 
 [8, 6, 1, 3, 7, 4, 9, 5, 2], 
 [6, 2, 5, 8, 9, 3, 7, 1, 4], 
 [3, 7, 9, 1, 4, 2, 6, 8, 5], 
 [1, 4, 8, 7, 5, 6, 2, 3, 9], 
 [2, 8, 4, 9, 3, 1, 5, 7, 6], 
 [9, 3, 7, 6, 8, 5, 4, 2, 1], 
 [5, 1, 6, 4, 2, 7, 3, 9, 8]]
"""