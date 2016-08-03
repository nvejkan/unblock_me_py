# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 20:58:28 2016

@author: nattawutvejkanchana
"""

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


b1 = Board()


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
    if b.board_size == 4:
        return (b.get_board().loc['r2','c0':].astype('str') == ['*','*','0','0']).all().all()\
            or (b.get_board().loc['r2','c1':].astype('str') == ['*','*','0']).all().all()\
            or (b.get_board().loc['r2','c2':].astype('str') == ['*','*']).all().all()
    else :
        return ((b1.get_board().loc['r2',:].astype('str') == ['*','*','0','0','0','0']).all().all() \
        or (b1.get_board().loc['r2','c1':].astype('str') == ['*','*','0','0','0']).all().all()\
        or (b1.get_board().loc['r2','c2':].astype('str') == ['*','*','0','0']).all().all()\
        or (b1.get_board().loc['r2','c3':].astype('str') == ['*','*','0']).all().all()\
        or (b1.get_board().loc['r2','c4':].astype('str') == ['*','*']).all().all()).all()
        


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
        

class Node:
    def __init__( self, state, parent, operator,depth ):
		# Contains the state of the node
        self.state = state # board
		# Contains the node that generated this node
        self.parent = parent #board object
		# Contains the operation that generated this node from the parent
        self.operator = operator #(black_name , up_down_left_right)
        self.depth = depth
          
  
def bfs( start ):
    nodes = []
	# Create the queue with the root node in it.
    size = start.board_size
    start_board = Board(size)
    start_board.blocks = start.blocks.copy()
    nodes.append( create_node( start_board, None, None,0) ) #node.state = board
    count = 1
    while True:
        # We've run out of states, no solution.
        if len( nodes ) == 0: 
            return None
		# take the node from the front of the queue
        node = nodes.pop(0)
        if is_final_board(node.state):
            print("Solution found!")
            moves = []
            temp = node
            while True:
                 moves.insert(0, temp.operator)
                 if temp.depth == 1: 
                     break
                 temp = temp.parent
            return moves				
             # Expand the node and add all the expansions to the front of the stack
        nodes.extend( expand_node( node, nodes ) )
        if count == 100:
            print("Limit Reach!")
            '''for x in nodes:
                print("NODES:")
                print(x.state.get_board())
                print(x.state.blocks)'''
            print("BOARD_LIST:")
            for x in board_list:
                
                print(x)
            break
        else:
            count = count + 1

def create_node( state, parent, operator, depth ):
    return Node( state, parent, operator, depth )

def board_already_found(bx):
    for i in board_list:
        if (bx == i).all().all():
            return True
        return False

def expand_node( node, nodes ):
    """Returns a list of expanded nodes"""
    size = node.state.board_size
    expanded_nodes = []
    for i in node.state.blocks.keys():
        block = node.state.blocks[i][0]
        start = node.state.blocks[i][1]
        
        peek = node.state.move_up(block,start,True)
        if peek != False: #got peek blocks
            new_board = Board(size) #create new board obj
            new_board.blocks = peek #set the blocks
            expanded_nodes.append( create_node( new_board, node, (i,"u"), node.depth + 1 ) )
            #print(i,new_board.get_board())
            
        peek = node.state.move_down(block,start,True)
        if peek != False: #got peek blocks
            new_board = Board(size) #create new board obj
            new_board.blocks = peek #set the blocks
            expanded_nodes.append( create_node( new_board, node, (i,"d"), node.depth + 1 ) )
            #print(i,new_board.get_board())
        
        peek = node.state.move_left(block,start,True)
        if peek != False: #got peek blocks
            new_board = Board(size) #create new board obj
            new_board.blocks = peek #set the blocks
            expanded_nodes.append( create_node( new_board, node, (i,"l"), node.depth + 1 ) )
            #print(i,new_board.get_board())
            
        peek = node.state.move_right(block,start,True)
        if peek != False: #got peek blocks
            new_board = Board(size) #create new board obj
            new_board.blocks = peek #set the blocks
            expanded_nodes.append( create_node( new_board, node, (i,"r"), node.depth + 1 ) )
            #print(i,new_board.get_board())
    
    return expanded_nodes
    
#run_game(b1)
moves = bfs(b1)

print('*********ENDED**************')     

    
