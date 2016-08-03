# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 21:29:21 2016

@author: nattawutvejkanchana
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 22:42:09 2016

@author: nattawutvejkanchana
"""

from item_v2 import *

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

#print(b1.board)

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
'''
def is_final_board(b):
    return ((b1.board.loc['r2',:].astype('str') == ['*','*','0','0','0','0']).all().all() \
        or (b1.board.loc['r2','c1':].astype('str') == ['*','*','0','0','0']).all().all()\
        or (b1.board.loc['r2','c2':].astype('str') == ['*','*','0','0']).all().all()\
        or (b1.board.loc['r2','c3':].astype('str') == ['*','*','0']).all().all()\
        or (b1.board.loc['r2','c4':].astype('str') == ['*','*']).all().all()).all()
        
        

def go_deep(b):
    this_stage_board = Board()
    this_stage_board.blocks = b.blocks.copy()
    #print('this_stage_board:',this_stage_board)
    #print(this_stage_board.get_board())
    board_list.append(this_stage_board)
    solution_found = False
    for i in b.blocks.keys():
        block = b.blocks[i][0]
        start = b.blocks[i][1]
        if solution_found == False :
            
            for j in [b.move_left,b.move_right,b.move_up,b.move_down]:
                if j(block,start):
                    #print('moved b:',b)
                    #print(b.get_board())
                    found_flag = False
                    for x in [b.get_board().astype('str') for b in board_list]:
                        if (x == b.get_board().astype('str')).all().all():
                            
                            print("b_list: ",board_list)
                            #print("x: ",x)
                            print(x)
                            print("b: ",b)
                            print(b.get_board())
                            found_flag = True
                            break
                    print('flag:',found_flag)
                    if not found_flag:
                        new_board = Board() #create new board obj
                        new_board.blocks = b.blocks.copy() #set the board
                        #b.blocks = this_stage_board.copy() #reset the board
                        
                        print(len(board_list))
                        #print('new_board:')
                        #print(new_board.get_board())
                        if is_final_board(new_board):
                            print('FINAL!')
                            print(new_board.get_board())
                            solution_found = True
                            return True
                        else:
                            #print('new_board:')
                            #print(new_board.get_board())
                            board_list.append(this_stage_board)
                            solution_found = go_deep(new_board)
                            print('BACK')
                            if solution_found:
                                return True
                            #print(new_board.board)
                            #board_list.append(new_board)
                    b.blocks = this_stage_board.blocks.copy() #reset the board
                    found_flag = False
                    #print("b_reset: ",b)
                    #print(b.get_board())
            b.blocks = this_stage_board.blocks.copy() #reset the board
            found_flag = False
        else:
            break
board_list = []
go_deep(b1)         
print('*********ENDED**************')           
  

    
