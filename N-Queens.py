#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 20:23:45 2019

@author: joscelynec

N-Queens Problem: Given a chess board having  cells, 
we need to place  queens in such a way that no queen 
is attacked by any other queen. A queen can attack horizontally, 
vertically and diagonally.

Solve with backtracking 
Adapted from
https://algorithms.tutorialhorizon.com/backtracking-n-queens-problem/

"""

def is_attacked( x, y, board, N):
    #checking for row and column
    for cell in board[x]:
        if cell == 1:
            return True
    for i in range(N):
        if board[i][y] == 1:
            return True
    #checking for diagonals
    for p in range(N):
        for q in range(N):
            if p+q == x+y and board[p][q] == 1:
                 return True
            if p-q == x-y and board[p][q] == 1:
                return True
    return False

            
def N_Queens(queen, board, N): #will place the Queens one at a time, for column wise
     if(queen==N): #we have solved the problem
         return True
     for row in range(N):
         if not is_attacked(row, queen, board, N):
             board[row][queen] = 1  #place the queen
             if(N_Queens(queen+1, board,  N)): #look ahead and solve next queen
                 return True
             #well things didn't workout, so undo what we did
             board [row][queen]=0 #Backtrack
     #still haven't found a solution
     return False
         
#Test Code
bd = [[0,0,0,1],
      [0,0,0,0],
      [0,0,0,0],
      [0,0,0,0]]
print("Queens placed at (3,0)")
print("Positions and attack status")

for p in range(4):
    for q in range(4):
        print("(",p,q,") is attacked",is_attacked(p, q, bd, 4))
        
        
print("Place 4 Queens")
bd = [[0,0,0,0],
      [0,0,0,0],
      [0,0,0,0],
      [0,0,0,0]]
N_Queens(0,bd,4)
for row in bd:
    print(row)
    
print("Place 8 Queens")    
bd = [[0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0]]
N_Queens(0,bd,8)
for row in bd:
    print(row)
"""    
Queens placed at (3,0)
Positions and attack status
( 0 0 ) is attacked True
( 0 1 ) is attacked True
( 0 2 ) is attacked True
( 0 3 ) is attacked True
( 1 0 ) is attacked False
( 1 1 ) is attacked False
( 1 2 ) is attacked True
( 1 3 ) is attacked True
( 2 0 ) is attacked False
( 2 1 ) is attacked True
( 2 2 ) is attacked False
( 2 3 ) is attacked True
( 3 0 ) is attacked True
( 3 1 ) is attacked False
( 3 2 ) is attacked False
( 3 3 ) is attacked True
Place 4 Queens
[0, 0, 1, 0]
[1, 0, 0, 0]
[0, 0, 0, 1]
[0, 1, 0, 0]
Place 8 Queens
[1, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 1, 0]
[0, 0, 0, 0, 1, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 1]
[0, 1, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 1, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 1, 0, 0]
[0, 0, 1, 0, 0, 0, 0, 0]
"""
