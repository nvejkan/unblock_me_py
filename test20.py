# -*- coding: utf-8 -*-
"""
WORK!!!
"""

from item_v5 import *
from pandas.util.testing import assert_frame_equal

b1 = Board()


i_star = Block('*',2,'right') #this is the red one
b1.place_block(i_star,(2,0))

i1 = Block('A',2,'down')
#b1.place_block(i1,(0,0))

i2 = Block('B',2,'right')
b1.place_block(i2,(3,0))

i3 = Block('C',2,'down')
b1.place_block(i3,(4,1))

i4 = Block('D',2,'right')
b1.place_block(i4,(4,2))

i5 = Block('E',2,'right')
b1.place_block(i5,(5,2))

i6 = Block('F',3,'down')
b1.place_block(i6,(1,3))

i7 = Block('G',3,'down')
b1.place_block(i7,(1,4))

i9 = Block('H',2,'down')
b1.place_block(i9,(1,5))

print(b1.get_board())

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
        #print(4)
        #print((b.get_board().loc['r2',:].astype('str')))
        return (b.get_board().loc['r2','c0':].astype('str') == ['*','*','0','0']).all().all()\
            or (b.get_board().loc['r2','c1':].astype('str') == ['*','*','0']).all().all()\
            or (b.get_board().loc['r2','c2':].astype('str') == ['*','*']).all().all()
    else :
        #print(6)
        #print((b.get_board().loc['r2',:].astype('str')))
        return ((b.get_board().loc['r2',:].astype('str') == ['*','*','0','0','0','0']).all().all() \
        or (b.get_board().loc['r2','c1':].astype('str') == ['*','*','0','0','0']).all().all()\
        or (b.get_board().loc['r2','c2':].astype('str') == ['*','*','0','0']).all().all()\
        or (b.get_board().loc['r2','c3':].astype('str') == ['*','*','0']).all().all()\
        or (b.get_board().loc['r2','c4':].astype('str') == ['*','*']).all().all()).all()
        


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
                moved = b.move_up(block_name)  
            elif move == 2:
                moved = b.move_down(block_name) 
            elif move == 1:
                moved = b.move_left(block_name) 
            elif move == 3:
                moved = b.move_right(block_name) 
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
            print(count,moves)
            return moves				
        # Expand the node and add all the expansions to the front of the stack
        
        #board_list.append(node.state.get_board().copy())
        nodes.extend( expand_node( node, nodes ) )
        if count == 1000:
            print("Limit Reach!")
            '''for x in nodes:
                print("NODES:")
                print(x.state.get_board())
                print(x.state.blocks)'''
            of = open("test17.log","w")
            of.write("BOARD_LIST:{0}\n".format(len(board_list)))
            
            for x in board_list:
                
                of.write(str(x))
                of.write('\n')
            
            of.close()
            break
        
        else:
            count = count + 1
        if count%50 == 0:
            print("node count:",count)

def create_node( state, parent, operator, depth ):
    return Node( state, parent, operator, depth )

def board_already_found(bx):
    for i in board_list:
        '''
        print("bx")
        print(bx)
        print("i")
        print(i)
        #print("compare")
        #print(bx == i)
        '''
        '''
        if (bx.astype('str') == i.astype('str')).all().all():
            print("bx found")
            #print(bx)
            #print(i)
            return True
        print("bx not found")
        '''
        #print(bx)
        try:
            assert_frame_equal(bx, i)
            #print("bx found")
            #print(bx)
            #print(i)
            return True
        except:  # appeantly AssertionError doesn't catch all
            #print("bx not found")
            None
    #print("bx not found")    
    #print(bx)            
    return False

def expand_node( node, nodes ):
    """Returns a list of expanded nodes"""
    size = node.state.board_size
    bx = Board(size)
    bx.blocks = node.state.blocks.copy()
    expanded_nodes = []
    for i in bx.blocks.keys():
        
        count = 1
        while True:
            #print(i,"u" ,bx.get_board())
            #print(bx.move_up(block,start))
            moved = bx.move_up(i)
            #print(moved)
            if moved:
                new_board = Board(size) #create new board obj
                new_board.blocks = bx.blocks.copy() #set the blocks
                if not board_already_found(new_board.get_board().copy()):
                    expanded_nodes.append( create_node( new_board, node, (i,count*"u"), node.depth + 1 ) )
                    board_list.append(new_board.get_board().copy())
                count = count + 1
            else:
                break
            #print(i,"moved", bx.get_board())
        #clear bx
        bx.blocks = node.state.blocks.copy()
            
        count = 1
        while True:
            #print(i,"d", bx.get_board())
            #print(bx.move_down(block,start))
            moved = bx.move_down(i)
            #print(moved)
            if moved:
                new_board = Board(size) #create new board obj
                new_board.blocks = bx.blocks.copy() #set the blocks
                if not board_already_found(new_board.get_board().copy()):
                    expanded_nodes.append( create_node( new_board, node, (i,count*"d"), node.depth + 1 ) )
                    board_list.append(new_board.get_board().copy())
                count = count + 1
            else:
                break
        #clear bx
        bx.blocks = node.state.blocks.copy()
        
        count = 1
        while True:
            #print(i,"l", bx.get_board())
            #print(bx.move_left(block,start))
            moved = bx.move_left(i)
            #print(moved)
            if moved:
                new_board = Board(size) #create new board obj
                new_board.blocks = bx.blocks.copy() #set the blocks
                if not board_already_found(new_board.get_board().copy()):
                    expanded_nodes.append( create_node( new_board, node, (i,count*"l"), node.depth + 1 ) )
                    board_list.append(new_board.get_board().copy())
                count = count + 1
            else:
                break
            #print(i,"moved", bx.get_board())
        #clear bx
        bx.blocks = node.state.blocks.copy()
            
        count = 1
        while True:
            #print(i,"r", bx.get_board())
            #print(bx.move_right(block,start))
            moved = bx.move_right(i)
            #print(moved)
            if moved:
                new_board = Board(size) #create new board obj
                new_board.blocks = bx.blocks.copy() #set the blocks
                if not board_already_found(new_board.get_board().copy()):
                    expanded_nodes.append( create_node( new_board, node, (i,count*"r"), node.depth + 1 ) )
                    board_list.append(new_board.get_board().copy())
                count = count + 1
            else:
                break
            #print(i,"moved", bx.get_board())
        #clear bป
                
    #print(expanded_nodes)
    return expanded_nodes
    
#run_game(b1)
moves = bfs(b1)

print('*********ENDED**************')     

    
