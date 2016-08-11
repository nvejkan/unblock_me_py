from item_v6 import *
dg = {}
dg[3] = [(('*',2,'right'),(2,0)),(('A',2,'down'),(0,0)),(('B',2,'right'),(0,1))\
        ,(('C',2,'right'),(0,3)),(('D',2,'down'),(1,2)),(('E',3,'down'),(2,3))\
        ,(('F',3,'down'),(2,4)),(('G',3,'right'),(4,0))]
dg[4] = [(('*',2,'right'),(2,0)),(('A',2,'down'),(0,0)),(('B',2,'right'),(3,0))\
        ,(('C',2,'down'),(4,1)),(('D',2,'right'),(4,2)),(('E',2,'right'),(5,2))\
        ,(('F',3,'down'),(1,3)),(('G',3,'down'),(1,4))]
dg[5] = [(('*',2,'right'),(2,0)),(('A',3,'down'),(0,2)),(('B',2,'right'),(4,0))\
        ,(('C',2,'down'),(3,1)),(('D',3,'right'),(3,2)),(('E',3,'down'),(3,5))\
        ,(('F',4,'down'),(1,2)),(('G',2,'down'),(4,4))]

def get_board_game(num):
    bx = Board()
    for i in dg.get(num):
        bx.place_block(i[0],i[1])

    return bx
