# -*- coding: utf-8 -*-
"""
WORK!!!
"""

from item_v6 import *
import time
import game_list

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
          
  
def bfs( start, limit ):
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
        
        is_acyclic,dict_i_s,free_move = acyclic_block(node.state)
        if is_final_board(node.state):
            print("Solution found!")
            moves = []
            temp = node
            while True:
                 moves.insert(0, temp.state.get_board())
                 if temp.depth == 1: 
                     break
                 temp = temp.parent
            #print(count,moves)
            return moves
        elif is_acyclic:
            print("Acyclic!")
            #print(node.state.get_board())
            #print(node.state.blocks)
            temp = Board()
            temp.blocks = node.state.blocks.copy()
            acyclic_moves = acyclic_solver(temp)
            if acyclic_moves != False:
                #print(acyclic_moves)
                print("Solution found!")
                acyclic_moves = [ j.get_board() for j in acyclic_moves]
                moves = []
                temp = node
                while True:
                    if temp.depth <= 1: 
                        break
                    moves.insert(0, temp.state.get_board())
                    temp = temp.parent
                #print(count,moves)
                #print(moves)
                moves.extend(acyclic_moves)
                return moves
        
        # Expand the node and add all the expansions to the front of the stack
        
        #board_list.append(node.state.get_board().copy())
        nodes.extend( expand_node( node, nodes ) )  
        if count == limit:
            print("Limit Reach!")

            #save boards
            of = open("board.log","w")
            of.write("BOARD_LIST:{0}\n".format(len(board_list)))
            for x in board_list:
                
                of.write(str(x))
                of.write('\n')
            
            of.close()

            #save nodes
            node_left_file = open("nodes_left.log","w")
            node_left_file.write("NODES:{0}\n".format(len(nodes)))
            
            all_node_f = open("all_nodes.log","w")

            opened_node_f = open("opened_nodes.log","w")
            
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
        if count % 1 == 0:
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
    
def acyclic_block(bx):
    all_pos = find_possible_board(bx)
    start,end,size,direct = bx.blocks.get('*')
    dict_i_s = {}
    free_move = {}
    s = set(bx.get_board().loc['r{0}'.format(start[0]),'c{0}'.format(int(end[1])+1):].astype('str'))
    
    if '0' in s: s.remove('0')
    dict_i_s['*'] = s
    blockees = []
    blockees.append('*')
    for blockee in blockees: # * F G
        #print("blockee",blockee)
        #print([sx for sx in [ dict_i_s.get(k) for k in dict_i_s.keys()] if blockee in sx])
        for i in dict_i_s.get(blockee): # F G H || B E D ||
            start,end,size,direct = bx.blocks.get(i)
            pos = all_pos.get(i)[2]
            
            if [sx for sx in [ dict_i_s.get(k) for k in dict_i_s.keys()] if blockee in sx] != []:
                loop_list = [sx for sx in [ dict_i_s.get(k) for k in dict_i_s.keys()] if blockee in sx][0]
            else:
                loop_list = [blockee]
                
            for test_bk in loop_list: #it shouldn't block anythings from the blockee class
                #print("test_bk",test_bk)
                blockee_start,blockee_end,blockee_size,blockee_direct = bx.blocks.get(test_bk)
                
                #print(pos)
                if blockee_direct == "right":
                    blockee_way = blockee_start[0] #row
                    # only pos that not block the parent
                    pos = [ j for j in pos if not blockee_way in range(j[0][0],int(j[1][0])+1) ] #row
                else:
                    blockee_way = blockee_start[1] #col
                    pos = [ j for j in pos if not blockee_way in range(j[0][1],int(j[1][1])+1) ] #col
            #pos = [ j for j in pos if can_go(bx,i,direct,start,end,j[0],j[1]) ]
            #print(i,pos)
            if pos == []: #out of move
                return (False,None,None) # this is cyclic board
            blockers = set()
            for p in pos:
                des_start = p[0]
                des_end = p[1]
                
                s_i = can_go(bx,i,direct,start,end,des_start,des_end)
                #print(i,des_start,des_end,s_i)
                if s_i == set(): # have some way without blocking
                    blockers = set()
                    free_move[i] = (des_start,des_end)
                    break
                else:
                    blockers = blockers.union(s_i)
                    
            if blockers != set():
                dict_i_s[i] = blockers
                #new_blockee = [ i for i in blockers if i not in blockees]
                #print("newb",new_blockee)
                blockees.append(i)
                #print(blockees)

            #print("blockers",blockers)
            if '*' in blockers:
                return (False,None,None) # this is cyclic board
            
    #print(s)
    #print(all_pos)
    #print(free_move)
    #print(dict_i_s)
    return (True,dict_i_s,free_move) #this is acyclic board 

def find_possible_board(b):
    all_pos = {}
    for name in b.blocks.keys():
        start,end,size,direct = b.blocks.get(name)
        pos_list = []
        if direct == "down":
            col = start[1]
            for start_pos in [(x,col) for x in range (0,6)] :
                end_pos = get_end_pos(direct,size, start_pos)
                #print(chk_start_end_pos(start_pos,end_pos,b.board_size))
                #print(start_pos,end_pos)
                #print(range(start_pos[0],end_pos[0]+1))
                if chk_start_end_pos(start_pos,end_pos,b.board_size) : # and not 2 in range(start_pos[0],end_pos[0]+1):
                    pos_list.append((start_pos,end_pos))
        else:
            row = start[0]
            for start_pos in [(row,y) for y in range (0,6)] :
                end_pos = get_end_pos(direct,size, start_pos)
                if chk_start_end_pos(start_pos,end_pos,b.board_size):
                    pos_list.append((start_pos,end_pos))
        all_pos[name] = (direct,size,pos_list)
    return all_pos

def chk_start_end_pos(start,end,board_size):
        return not (start[0] < 0 or start[0] > board_size - 1 \
                or start[1] < 0 or start[1] > board_size - 1 \
                or end[0] < 0 or end[0] > board_size - 1 \
                or end[1] < 0 or end[1] > board_size - 1)
def get_end_pos(direction,size,start):
    if direction == 'down':
        end = (start[0]+size-1 , start[1]) #a tuple of (row,col)
    else:#right
        end = (start[0] , start[1]+size-1)#a tuple of (row,col)
    return end

def can_go(bx,bname,direct,src_start,src_end,des_start,des_end):
    max_r = max([ i[0] for i in [src_start,src_end,des_start,des_end]])
    max_c = max([ i[1] for i in [src_start,src_end,des_start,des_end]])
    min_r = min([ i[0] for i in [src_start,src_end,des_start,des_end]])
    min_c = min([ i[1] for i in [src_start,src_end,des_start,des_end]])
    
    s_i = bx.get_board().loc['r{0}'.format(min_r):'r{0}'.format(max_r)\
                            ,'c{0}'.format(min_c):'c{0}'.format(max_c)].astype('str')
    if direct == "right":
        s_i = set(s_i.loc['r{0}'.format(min_r),:])
    else:
        s_i = set(s_i.loc[:,'c{0}'.format(min_c)])
    
    if '0' in s_i: s_i.remove('0')
    if bname in s_i: s_i.remove(bname)

    #print(bname,"CAN GO ",s_i)
    return s_i
    

#print(acyclic_block(x))
#print(acyclic_block(b_cy))

def move_acyclic_board(bx,dict_i_s,free_move,move_i):
    free_pos = free_move.get(move_i)
    if free_pos is not None:
        des_start = free_pos[0]
        des_end = free_pos[1]
        start,end,size,direct = bx.blocks.get(move_i)
        #delete move_i from blocks then place into new entry
        del bx.blocks[move_i]
        bx.blocks[move_i] = (des_start,des_end,size,direct)
        
        return bx
    else:
        #dict_i_s {'G': {'D', 'E'}, '*': {'G', 'H', 'F'}, 'F': {'B'}}
        blockers = dict_i_s.get(move_i)
        for j in  blockers:
            bx = move_acyclic_board(bx,dict_i_s,free_move,j) #move blockers first
        return bx
def acyclic_solver(b):
    moves = []
    while True:
        is_acyclic,dict_i_s,free_move = acyclic_block(b)
        #dict_i_s {'B': ((3, 0), (3, 1)), 'D': ((4, 0), (4, 1)), 'H': ((0, 5), (1, 5)), 'E': ((5, 0), (5, 1))}
        #free_move {'G': {'D', 'E'}, '*': {'G', 'H', 'F'}, 'F': {'B'}}
        if is_acyclic:
            b = move_acyclic_board(b,dict_i_s,free_move,'*') # start to move '*'
            #print(b.get_board())
            new_b = Board()
            new_b.blocks = b.blocks.copy()
            moves.append(new_b)
            if is_final_board(b):
                #print("Solution found")
                return moves
        else:
            #print("Cyclic")
            return False
if __name__ == "__main__":
    #run_game(b1)
    b1 = game_list.get_board_game(498)
    print(b1.get_board())
    
    
    #continue_board_list("board.log")
    #continue_node("all_nodes.log","nodes_left.log","opened_nodes.log")
    moves = bfs(b1,10000)
    if moves is not None:
        for i in moves:
            print(i)

    print('*********ENDED**************')     

    
