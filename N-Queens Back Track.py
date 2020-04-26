#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 00:24:30 2020

@author: joscelynec
"""

'''
Backtracking Algorithm to solve the N-Queens Puzzle
Adapted from https://github.com/mattcollier/diagonals#sample-output

'''
#Ultility displays the grid
def printGrid():
    global grid
    for i in range(len(grid)):
        print()
        for j in range(len(grid)):
            print(grid[i][j],end=' ')
        print()
    print()
    

#Can Queen be placed at row, col
def canPlaceQueen(row, col):
    global grid
    #Check to the left 
    
    i = 0
    while(0<= col - i):
        if(grid[row][col - i] == 'Q'):
            return False
        i+=1
   #Check above 
    i = 0
    while(0<= row - i):
        if(grid[row-i][col] == 'Q'):
            return False
        i+=1
    #Check West North West 
    i = 0
    while(0<=row - i and 0<= col - i):
        if(grid[row - i][col - i] == 'Q'):
            return False
        i+=1
   #Check ENW 
    i = 0
    while(0<=row-i and col + i < len(grid)):
        if(grid[row-i][col+i] == 'Q'):
            return False
        i+=1  
    return True
    

'''
Backtrack until reminaingQueens equals 0
'''

def extend(row, col, remainingQueens):
    global size
    global grid
    global ct

    if remainingQueens == 0:
        ct+=1
        print('Solution:',ct)
        printGrid()
        return

    if row == size:
        return

    nextRow = row
    nextCol = col + 1
    if nextCol == size:
        nextRow += 1
        nextCol = 0
    
    for cell in ['_', 'Q']:
        # blank cell) always works, no need to test
        if cell == '_':
            grid[row][col] = cell
            extend(nextRow, nextCol, remainingQueens)
        else:
            if canPlaceQueen(row, col):
                # the diagonal works, put it in
                grid[row][col] = cell
                extend(nextRow, nextCol, remainingQueens - 1)

size = 4
ct = 0
# setup a chessboard of  size X size 
grid = [['_' for i in range(size)] for j in range(size)]

extend(0, 0, size)
'''
Solution: 1

_ _ Q _ 

Q _ _ _ 

_ _ _ Q 

_ Q _ _ 

Solution: 2

_ Q _ _ 

_ _ _ Q 

Q _ _ _ 

_ _ Q _ 
'''
