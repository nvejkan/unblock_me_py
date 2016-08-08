# -*- coding: utf-8 -*-
"""
WORK!!!
"""

from item_v6 import *
from pandas.util.testing import assert_frame_equal
import time

board_list = []
start_time = time.time()
nodes = []
opened_node = []
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
    global board_list,nodes,opened_node
    if len(nodes) == 0:
        #nodes = []
    
	# Create the queue with the root node in it.
        nodes.append( create_node( start, None, None,0) ) #node.state = board
    count = 1
    while True:
        # We've run out of states, no solution.
        if len( nodes ) == 0:
            print("NO nodes left!")
            return None
		# take the node from the front of the queue
        node = nodes.pop(0)
        opened_node.append(node)
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
        if count == 10:
            print("Limit Reach!")

            #save boards
            of = open("test30_board.log","w")
            of.write("BOARD_LIST:{0}\n".format(len(board_list)))
            for x in board_list:
                
                of.write(str(x))
                of.write('\n')
            
            of.close()

            #save nodes
            node_left_file = open("test30_nodes_left.log","w")
            node_left_file.write("NODES:{0}\n".format(len(nodes)))
            
            all_node_f = open("test30_all_nodes.log","w")

            opened_node_f = open("test30_opened_nodes.log","w")
            
            for node in nodes:
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
                
                node_left_file.write("{0}\n".format(id(node)))

                all_node_f.write("{0}||{1}||{2}||{3}||{4}\n".format(id(node),node.state.blocks,id(node.parent),node.operator,node.depth))
                

            for node in opened_node:
                opened_node_f.write("{0}\n".format(id(node)))
                
                all_node_f.write("{0}||{1}||{2}||{3}||{4}\n".format(id(node),node.state.blocks,id(node.parent),node.operator,node.depth))

                
            
            node_left_file.close()
            all_node_f.close()
            opened_node_f.close()
            break
        else:
            count = count + 1
            
        print("node expand:{0} board_list: {1} time: {2}".format(count,len(board_list),time.time()-start_time))

def create_node( state, parent, operator, depth ):
    return Node( state, parent, operator, depth )

def board_already_found(bx_blocks):
    global board_list
    for i in board_list:
        if i == bx_blocks:
            return True
    return False

def expand_node( node, nodes ):
    global board_list
    """Returns a list of expanded nodes"""
    size = node.state.board_size
    bx = Board(size) # hard copy of the node
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
                if not board_already_found(new_board.blocks):
                    expanded_nodes.append( create_node( new_board, node, (i,count*"u"), node.depth + 1 ) )
                    board_list.append(new_board.blocks)
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
                if not board_already_found(new_board.blocks):
                    expanded_nodes.append( create_node( new_board, node, (i,count*"d"), node.depth + 1 ) )
                    board_list.append(new_board.blocks)
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
                if not board_already_found(new_board.blocks):
                    expanded_nodes.append( create_node( new_board, node, (i,count*"l"), node.depth + 1 ) )
                    board_list.append(new_board.blocks)
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
                if not board_already_found(new_board.blocks):
                    expanded_nodes.append( create_node( new_board, node, (i,count*"r"), node.depth + 1 ) )
                    board_list.append(new_board.blocks)
                count = count + 1
            else:
                break
            #print(i,"moved", bx.get_board())
        #clear b
                
    #print(expanded_nodes)
    return expanded_nodes

def continue_board_list(fname):
    global board_list
    from ast import literal_eval
    fin = open(fname)
    board_list = []
    count = 1
    for i in fin:
        if count > 1:
            board_list.append(literal_eval(i))
        else:
            pass
        count = count + 1

    fin.close()
def continue_node(fname_all_node,fname_left_node,fname_opened):
    global nodes,opened_node
    from ast import literal_eval

    #all nodes
    all_node = {} # all_node[id] = Node
    node_parent = {}
    fin = open(fname_all_node)
    for i in fin:
        tup = i.strip().split('||')
        #print(tup)
        #(id(node),node.state.blocks,id(node.parent),node.operator,node.depth))
        node_id = literal_eval(tup[0]) 
        state = Board()
        state.blocks = literal_eval(tup[1])
        parent = None # init parent as None
        parent_id = literal_eval(tup[2])
        operator = literal_eval(tup[3])
        depth = literal_eval(tup[4])
        
        node_parent[node_id] = parent_id
        all_node[node_id] = create_node( state, parent, operator, depth )
    fin.close()

    #fix parents
    for node_id in node_parent.keys():
        parent_id = node_parent.get(node_id)
        node = all_node.get(node_id)
        parent_node = all_node.get(parent_id)
        node.parent = parent_node

    #left nodes
    fin = open(fname_left_node)
    count = 1
    for i in fin:
        if count > 1:
            #(id(node))
            node_id = literal_eval(i.strip())
            node = all_node.get(node_id)
            nodes.append(node)
        else:
            pass
        count = count + 1
    fin.close()

    #opened
    fin = open(fname_opened)
    for i in fin:
        #(id(node))
        node_id = literal_eval(i.strip())
        node = all_node.get(node_id)
        opened_node.append(node)
    fin.close()
    
if __name__ == "__main__":
    #run_game(b1)
    b1 = Board()
    
    b1.place_block(('*',2,'right'),(2,0))
    
    b1.place_block(('A',2,'down'),(0,0))
    
    b1.place_block(('B',2,'right'),(3,0))
    
    b1.place_block(('C',2,'down'),(4,1))
    
    b1.place_block(('D',2,'right'),(4,2))
    
    b1.place_block(('E',2,'right'),(5,2))
    
    b1.place_block(('F',3,'down'),(1,3))
    
    b1.place_block(('G',3,'down'),(1,4))
    
    b1.place_block(('H',2,'down'),(1,5))
    
    print(b1.get_board())
    continue_board_list("test30_board.log")
    continue_node("test30_all_nodes.log","test30_nodes_left.log","test30_opened_nodes.log")
    moves = bfs(b1)

    print('*********ENDED**************')     

    
