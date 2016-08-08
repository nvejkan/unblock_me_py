from item_v6 import *

def continue_node(fname):
    global nodes
    from ast import literal_eval
    fin = open(fname)
    board_list = []
    count = 1
    for i in fin:
        if count > 1:
            tup = i.split('||')
            #(node.state.blocks,node.parent.blocks,node.operator,node.depth)
            state = Board()
            state.blocks = literal_eval(tup[0])
            parent = Board()
            parent.blocks = literal_eval(tup[1])
            operator = literal_eval(tup[2])
            depth = literal_eval(tup[3])

            nodes.append((state,parent,operator,depth))
        else:
            pass
        count = count + 1

nodes = []
continue_node('test30_nodes.log')
