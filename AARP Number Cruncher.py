#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: joscelynec

The March 2020 AARP magazine featured a simple sudoku type puzzle where a 3 by 3 grid is to filled 
in the digits 1,2,3,…,9. Digits are to be used only once and need satisfy 
3 arithmetic row conditions and 3 arithmetic column conditions.

If the grid is represented by a 9-element array as follows:

x[0][0], x[0][1], x[0][2]
x[1][0], x[1][1], x[1][2]
x[2][0], x[2][1], x[2][2]

then the 6 conditions are

Rows
(x[0][0]+x[0][1])*x[0][2] == 24
x[1][0]+ x[1][1]+x[1][2] == 17
(x[2][0]-x[2][1])*x[2][2] == 27

Columns
(x[0][0]]+x[1][1][0])*x[2][0] == 44 
(x[0][1]*x[1][1])-x[2][1] == 20
(x[2]*x[5])+x[8] == 25 

this puzzle has the unique solution

5, 7, 2
6, 3, 8
4, 1, 9

The code below adapts a Backtrack Sudoku solver to solve the puzzle

******* A Disclaimer ********
Puzzles like this are often prescribed for the aging (me) to help maintain mental acuity. 
Personally, when I am able, I would rather code a program to solve a puzzle as opposed 
to actually solving it unless the puzzle is a crossword or like. The endless repetitive solving 
of word finds, sudoku, and similiar seem a bit pointless, though it could very well be they 
are more effective at preventing dementia than programming a solution.

"""

#Driver function to kick off the recursion
import time 
start_time = time.clock()

def solveAARP(bd):
    return solveAARPCell(0, 0, bd)

"""
This function chooses a placement for the cell at (row, col)
and continues solving based on the rules we define.
  
Our strategy:
We will start at row 0.
We will solve every column in that row.
When we reach the last column we move to the next row.
If this is past the last row( row == bd.length) we are done.
The whole bd has been solved.
"""
def solveAARPCell(row, col, bd):


#Have we finished placements in all columns for 3the row we are working on?
    if (col == len(bd)):
#Yes. Reset to col 0 and advance the row by 1. We will work on the next row

        col = 0
        row += 1

#Have we completed placements in all rows? If so then we are done.
#If not, drop through to the logic below and keep solving things.
        if (row == len(bd)):
            return True; # Entire bd has been filled without conflict.

#Skip non-empty entries. They already have a value in them.
    if (bd[row][col] != 0):
        return solveAARPCell(row, col + 1, bd)

#Try all values 1 through 9 in the cell at (row, col).
#Recurse on the placement if it doesn't break the constraints.
    for val in range(1, 10):

#Apply constraints. We will only add the value to the cell if
#adding it won't cause us to break sudoku rules.

        if (canPlaceValue(bd, row, col, val)):
            bd[row][col] = val
            if (solveAARPCell(row, col + 1, bd)):#recurse with our VALID placement
                return True;
        
#Undo assignment to this cell. No values worked in it meaning that
#previous states put us in a position we cannot solve from. Hence,
#we backtrack by returning "false" to our caller.

    bd[row][col] = 0
    return False #No valid placement was found, this path is faulty, return false


#Will the placement at (row, col) break the puzzle 

def canPlaceValue(bd, row, col, valToPlace):
    #Check column constraint. For each row, we do a check on column "col"
    for element in bd:
        if (valToPlace == element[col]):
            return False;
    
#Check row constraint. For each column in row "row", we do a check.
    for i in range(len(bd)): 
        if (valToPlace == bd[row][i]): 
            return False;
        
#Check 3 row and 3 col constraints       
    if(row == 0 and col == 2 and (bd[0][0]+bd[0][1])*valToPlace != 24):
        return False
    if(row == 1 and col == 2 and bd[1][0] + bd[1][1] + valToPlace != 17):
        return False
    if(row == 2 and col == 0 and (bd[0][0] + bd[1][0])*valToPlace != 44):
        return False
    if(row == 2 and col == 1 and (bd[0][1]*bd[1][1]) - valToPlace != 20):
        return False
    if(row == 2 and col == 2 and  (bd[2][0]-bd[2][1])*valToPlace != 27):
        return False
    if(row == 2 and col == 2 and  (bd[0][2]*bd[1][2])+valToPlace != 25):
        return False
    return True

#Initialize board
bd = [[0,0,0],
      [0,0,0],
      [0,0,0]]
solveAARP(bd)
print(bd)
print(round(time.clock() - start_time,3),'secs')
'''
[[5, 7, 2], [6, 3, 8], [4, 1, 9]]
0.012 secs
'''
