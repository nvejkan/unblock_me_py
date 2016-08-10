from item_v6 import *
x = Board()
x.blocks = {'*': ((2, 1), (2, 2), 2, 'right'), 'H': ((1, 5), (2, 5), 2, 'down'), 'G': ((0, 4), (2, 4), 3, 'down'), 'C': ((0, 1), (1, 1), 2, 'down'), 'F': ((0, 3), (2, 3), 3, 'down'), 'E': ((5, 4), (5, 5), 2, 'right'), 'B': ((3, 2), (3, 3), 2, 'right'), 'A': ((0, 0), (1, 0), 2, 'down'), 'D': ((4, 4), (4, 5), 2, 'right')}
b_cy = Board()
b_cy.blocks = {'*': ((2, 0), (2, 1), 2, 'right'), 'H': ((3, 5), (4, 5), 2, 'down'), 'B': ((3, 0), (3, 1), 2, 'right'), 'D': ((4, 2), (4, 3), 2, 'right'), 'G': ((2, 4), (4, 4), 3, 'down'), 'F': ((1, 3), (3, 3), 3, 'down'), 'E': ((5, 4), (5, 5), 2, 'right'), 'A': ((0, 0), (1, 0), 2, 'down'), 'C': ((4, 1), (5, 1), 2, 'down')}
def acyclic_block(bx):
    all_pos = find_possible_board(bx)
    start,end,size,direct = bx.blocks.get('*')
    dict_i_s = {}
    free_move = {}
    s = set(bx.get_board().loc['r{0}'.format(start[0]),'c{0}'.format(int(end[1])+1):].astype('str'))
    
    if '0' in s: s.remove('0')
    cyclic = False
    dict_i_s['*'] = s
    blockees = []
    blockees.append('*')
    for blockee in blockees: # * F G
        print("blockee",blockee)
        for i in dict_i_s.get(blockee): # F G H || B E D ||
            start,end,size,direct = bx.blocks.get(i)
            blockee_start,blockee_end,blockee_size,blockee_direct = bx.blocks.get(blockee)
            pos = all_pos.get(i)[2]
            #print(pos)
            if blockee_direct == "right":
                blockee_way = blockee_start[0] #row
                # only pos that not block the parent
                pos = [ j for j in pos if not blockee_way in range(j[0][0],int(j[1][0])+1) ] #row
            else:
                blockee_way = blockee_start[1] #col
                pos = [ j for j in pos if not blockee_way in range(j[0][1],int(j[1][1])+1) ] #col
            #pos = [ j for j in pos if can_go(bx,i,direct,start,end,j[0],j[1]) ]
            blockers = set()
            for p in pos:
                des_start = p[0]
                des_end = p[1]

                '''
                #print(start,end)
                s_i = bx.get_board().loc['r{0}'.format(start[0]):'r{0}'.format(end[0])\
                                             ,'c{0}'.format(start[1]):'c{0}'.format(end[1])].astype('str')
                if direct == "right":
                    s_i = set(s_i.loc['r{0}'.format(start[0]),:])
                else:
                    s_i = set(s_i.loc[:,'c{0}'.format(start[1])])

                #print(i,s_i)
            
                if '0' in s_i: s_i.remove('0')
                if i in s_i: s_i.remove(i)
                print(i,start,end,s_i)
'''
                s_i = can_go(bx,i,direct,start,end,des_start,des_end)
                print(i,des_start,des_end,s_i)
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
                print(blockees)

            print("blockers",blockers)
            if '*' in blockers:
                cyclic = True
                return (False,None,None) # this is cyclic board
            
    #print(s)
    #print(all_pos)
    print(free_move)
    print(dict_i_s)
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
    True,dict_i_s,free_move
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

def move_acyclic_board(bx,dict_i_s,free_move):
    pass
for b in [x,b_cy]:
    is_acyclic,dict_i_s,free_move = acyclic_block(b)
    #dict_i_s {'B': ((3, 0), (3, 1)), 'D': ((4, 0), (4, 1)), 'H': ((0, 5), (1, 5)), 'E': ((5, 0), (5, 1))}
    #free_move {'G': {'D', 'E'}, '*': {'G', 'H', 'F'}, 'F': {'B'}}
    if is_acyclic:
        move_acyclic_board(bx,dict_i_s,free_move)
