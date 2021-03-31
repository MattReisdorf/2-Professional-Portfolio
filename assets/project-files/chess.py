# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 11:40:20 2020

@author: Matthew
"""

def getBoard(filename):
    file = open(filename , "r")
    board = []
    for line in file:
        row = []
        for cell in line:
            if cell != "\n":
                row.append(cell)
        board.append(row)
    file.close()
    return board

board = getBoard("chess-copy.txt")


def bishopAttack(board, rowstart, colstart):
    
    row , col = rowstart-1 , colstart-1
    while row >= 0 and col >= 0:
        if board[row][col] == "k":
            return True
        elif board[row][col] != ".":
            break
        row -= 1
        col -= 1
        
    row , col = rowstart-1 , colstart+1
    while row >= 0 and col < 8:
        if board[row][col] == "k":
            return True
        elif board[row][col] != ".":
            break
        row -= 1
        col += 1
        
    row , col = rowstart+1 , colstart-1
    while row < 8 and col >= 0:
        if board[row][col] == "k":
            return True
        elif board[row][col] != ".":
            break
        row += 1
        col -= 1
        
    row , col = rowstart+1 , colstart+1
    while row < 8 and col < 8:
        if board[row][col] == "k":
            return True
        elif board[row][col] != ".":
            break
        row += 1
        col += 1
        
    return False

def rookAttack(board, rowstart, colstart):
    
    row , col = rowstart-1 , colstart
    while row >= 0:
        if board[row][col] == "k":
            return True
        elif board[row][col] != ".":
            break
        row -= 1
    
    row , col = rowstart+1 , colstart
    while row < 8:
        if board[row][col] == "k":
            return True
        elif board[row][col] != ".":
            break
        row += 1
        
    row , col = rowstart , colstart-1
    while col >= 0:
        if board[row][col] == "k":
            return True
        elif board[row][col] != ".":
            break
        col -= 1
        
    row , col = rowstart , colstart+1
    while col < 8:
        if board[row][col] == "k":
            return True
        elif board[row][col] != ".":
            break
        col += 1
    
    return False

def queenAttack(board, rowstart, colstart):
    
    # Combined Rook and Bishop #
    
    row , col = rowstart-1 , colstart-1
    while row >= 0 and col >= 0:
        if board[row][col] == "k":
            return True
        elif board[row][col] != ".":
            break
        row -= 1
        col -= 1
        
    row , col = rowstart-1 , colstart+1
    while row >= 0 and col < 8:
        if board[row][col] == "k":
            return True
        elif board[row][col] != ".":
            break
        row -= 1
        col += 1
        
    row , col = rowstart+1 , colstart-1
    while row < 8 and col >= 0:
        if board[row][col] == "k":
            return True
        elif board[row][col] != ".":
            break
        row += 1
        col -= 1
        
    row , col = rowstart+1 , colstart+1
    while row < 8 and col < 8:
        if board[row][col] == "k":
            return True
        elif board[row][col] != ".":
            break
        row += 1
        col += 1

    row , col = rowstart-1 , colstart
    while row >= 0:
        if board[row][col] == "k":
            return True
        elif board[row][col] != ".":
            break
        row -= 1
    
    row , col = rowstart+1 , colstart
    while row < 8:
        if board[row][col] == "k":
            return True
        elif board[row][col] != ".":
            break
        row += 1
        
    row , col = rowstart , colstart-1
    while col >= 0:
        if board[row][col] == "k":
            return True
        elif board[row][col] != ".":
            break
        col -= 1
        
    row , col = rowstart , colstart+1
    while col < 8:
        if board[row][col] == "k":
            return True
        elif board[row][col] != ".":
            break
        col += 1
    
    return False

def kNightAttack(board, rowstart, colstart):
    
    row , col = rowstart-2, colstart-1
    if board[row][col] == "k":
        return True
    elif board[row][col] != ".":
        return False
    
    row , col = rowstart-2, colstart+1
    if board[row][col] == "k":
        return True
    elif board[row][col] != ".":
        return False
    
    row , col = rowstart-1, colstart-2
    if board[row][col] == "k":
        return True
    elif board[row][col] != ".":
        return False
    
    row , col = rowstart-1, colstart+2
    if board[row][col] == "k":
        return True
    elif board[row][col] != ".":
        return False
    
    row , col = rowstart-1, colstart-2
    if board[row][col] == "k":
        return True
    elif board[row][col] != ".":
        return False
    
    row , col = rowstart+1, colstart-2
    if board[row][col] == "k":
        return True
    elif board[row][col] != ".":
        return False
    
    row , col = rowstart+1, colstart+2
    if board[row][col] == "k":
        return True
    elif board[row][col] != ".":
        return False
    
    row , col = rowstart+2, colstart-1
    if board[row][col] == "k":
        return True
    elif board[row][col] != ".":
        return False
    
    row , col = rowstart+2, colstart+1
    if board[row][col] == "k":
        return True
    elif board[row][col] != ".":
        return False
    
def pawnAttack(board, rowstart, colstart):
    
    row , col = rowstart-1, colstart-1
    if board[row][col] == "k":
        return True
    
    elif board[row][col] != "k":
        return False
    
    row , col = rowstart-1, colstart+1
    if board[row][col] == "k":
        return True
    
    elif board[row][col] != "k":
        return False
       
def kingAttack(board, rowstart, colstart):
    
    row , col = rowstart , colstart
    for ri in [-1,0,1]:
        for ci in [-1,0,1]:
            if board[row+ri][col+ci] == "k":
                return True
            elif board[row+ri][col+ci] != ".":
                return False
            
            
            
bkcheck = False


for row in range(8):
    for col in range(8):
        piece = board[row][col]
        if piece == "P":
            if pawnAttack(board, row, col):
                bkcheck = True
        elif piece == "R":
            if rookAttack(board, row, col):
                bkcheck = True
        elif piece == "N":
            if kNightAttack(board, row, col):
                bkcheck = True
        elif piece == "B":
            if bishopAttack(board, row, col):
                bkcheck = True
        elif piece == "Q":
            if queenAttack(board, row, col):
                bkcheck = True
        elif piece == "K":
            if kingAttack(board, row, col):
                bkcheck = True
        

if bkcheck:
    print("The Black King is in Check")
else:
    print("The Black King is not in Check")
        


    