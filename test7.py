# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 20:35:44 2016

@author: nattawutvejkanchana
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 23:55:03 2016

@author: nattawutvejkanchana
"""

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

b1 = Board(4)

i_star = Block('*',2,'right') #this is the red one
b1.place_block(i_star,(2,0))

i1 = Block('A',2,'down')
b1.place_block(i1,(1,2))

i2 = Block('B',2,'right')
b1.place_block(i2,(0,1))

i3 = Block('C',2,'down')
b1.place_block(i3,(1,3))

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
    return (b.get_board().loc['r2','c0':].astype('str') == ['*','*','0','0']).all().all()\
        or (b.get_board().loc['r2','c1':].astype('str') == ['*','*','0']).all().all()\
        or (b.get_board().loc['r2','c2':].astype('str') == ['*','*']).all().all()
        

def go_deep(b):
    this_stage_board = Board(4)
    this_stage_board.blocks = b.blocks.copy()
    print('this_stage_board:',this_stage_board)
    print(this_stage_board.get_board())
    board_list.append(this_stage_board)
    solution_found = False
    for i in b.blocks.keys():
        block = b.blocks[i][0]
        start = b.blocks[i][1]
        if solution_found == False :
            
            for j in [b.move_left,b.move_right,b.move_up,b.move_down]:
                if j(block,start):
                    print('moved b:',b)
                    print(b.get_board())
                    found_flag = False
                    for x in board_list:
                        if (x.get_board().astype('str') == b.get_board().astype('str')).all().all():
                            
                            #print("b_list: ",board_list)
                            print("x: ",x)
                            print(x.get_board())
                            print("b: ",b)
                            print(b.get_board())
                            found_flag = True
                            break
                    print('flag:',found_flag)
                    if not found_flag:
                        new_board = Board(4) #create new board obj
                        new_board.blocks = b.blocks.copy() #set the board
                        #b.blocks = this_stage_board.copy() #reset the board
                        
                        print(board_list)
                        print('new_board:')
                        print(new_board.get_board())
                        if is_final_board(new_board):
                            print('FINAL!')
                            print(new_board.get_board())
                            solution_found = True
                            return True
                        else:
                            board_list.append(this_stage_board)
                            solution_found = go_deep(new_board)
                            print('BACK')
                            if solution_found:
                                return True
                            #print(new_board.board)
                            #board_list.append(new_board)
                    b.blocks = this_stage_board.blocks.copy() #reset the board
                    found_flag = False
                    print("b_reset: ",b)
                    print(b.get_board())
            b.blocks = this_stage_board.blocks.copy() #reset the board
            found_flag = False
        else:
            break
board_list = []
#go_deep(b1)  

def run_game(b):
    print(b.get_board())
    
    keys = b.blocks.keys()
    while(True):
        try:
            block_name = 'X'
            while block_name not in keys:
                block_name = (input("Pick {} :".format(keys)) ).upper()            
            move = int(input("up(num5),down(2),left(1),right(3) : "))
            if move == 5:
                moved = b.move_up(b.blocks[block_name][0],b1.blocks[block_name][1])  
            elif move == 2:
                moved = b.move_down(b.blocks[block_name][0],b1.blocks[block_name][1]) 
            elif move == 1:
                moved = b.move_left(b.blocks[block_name][0],b1.blocks[block_name][1]) 
            elif move == 3:
                moved = b.move_right(b.blocks[block_name][0],b1.blocks[block_name][1]) 
            else:
                print("incorrect move!")
            if moved == True:
                print("Moved")
                print(b.get_board())
                if is_final_board(b):
                    print("Solution found")
                    break
            
            moved = False
        except:
            None
        
run_game(b1)
    
print('*********ENDED**************')     

    
