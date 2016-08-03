# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 22:42:09 2016

@author: nattawutvejkanchana
"""

from item import *

b1 = Board()

i_star = Block('*',2,'right') #this is the red one
b1.place_block(i_star,(2,0))

i1 = Block('A',2,'down')
b1.place_block(i1,(0,0))

i2 = Block('B',2,'right')
b1.place_block(i2,(0,1))

i3 = Block('C',2,'right')
b1.place_block(i3,(0,3))

i4 = Block('D',2,'down')
b1.place_block(i4,(1,2))

i5 = Block('E',3,'down')
b1.place_block(i5,(2,3))

i6 = Block('F',3,'down')
b1.place_block(i6,(2,4))

i7 = Block('G',3,'right')
b1.place_block(i7,(4,0))

i9 = Block('X',2,'down')
b1.place_block(i9,(5,0))

print(b1.board)

'''
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
         
b1.move_up(b1.blocks['E'][0],b1.blocks['E'][1])         

def create_new_board(this_stage_board,b1):
    global b1
    new_board_obj = Board() #create new board obj
    new_board.board = b1.board.copy() #set the board
    b1.board = this_stage_board.copy() #reset the board
    return new_board_obj
'''
g = {}
g[b1] = set()

this_stage_board = b1.board.copy()
for i in b1.blocks.keys():
    block = b1.blocks[i][0]
    start = b1.blocks[i][1]
    
    for j in [b1.move_up,b1.move_down,b1.move_left,b1.move_right]:
        if j(block,start):
            new_board = Board() #create new board obj
            new_board.board = b1.board.copy() #set the board
            b1.board = this_stage_board.copy() #reset the board
            g[b1].add(new_board)
            
def go_deep(b):
    
