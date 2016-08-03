# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 20:52:53 2016

@author: nattawutvejkanchana
"""
import pandas as pd
class Board:
    def __init__(self,size=6):
        self.rt = 'r{0}' #row_text
        self.ct = 'c{0}' #col_text
        self.board_size = size
        self.board = self.init_board()
        self.blocks = {}
        self.exit = (2,5) #the exit door
        
        
        
    def init_board(self):
        zero_row = [ 0 for i in range(self.board_size) ]
        data = {}
        for i in range(self.board_size):
            data[self.ct.format(i)] = zero_row
        
        return pd.DataFrame( data, columns=[ self.ct.format(i) for i in range(self.board_size) ]\
                                    ,index = [ self.rt.format(i) for i in range(self.board_size) ] )
                                    
    def get_end_pos(self,block,start):
        if block.direction == 'down':
            end = (start[0]+block.size-1 , start[1]) #a tuple of (row,col)
        else:#right
            end = (start[0] , start[1]+block.size-1)#a tuple of (row,col)
        return end
        
    def place_block(self,block,start):
        #check validity
        end = self.get_end_pos(block,start)
        
        if  self.chk_start_end_pos(start,end) \
            and self.is_empty(start,end) \
            : #valid
            
            #print(start,end)
            self.blocks[block.name] = (block,start,end)
            #print(self.blocks)
            self.update_board(block.name,start,end)
            
            return True
        else:
            return False
            
    def chk_start_end_pos(self,start,end):
        return not (start[0] < 0 or start[0] > self.board_size - 1 \
                or start[1] < 0 or start[1] > self.board_size - 1 \
                or end[0] < 0 or end[0] > self.board_size - 1 \
                or end[1] < 0 or end[1] > self.board_size - 1)
    def is_empty(self,start,end,name=0):
        
        return ((self.board.loc[ self.rt.format(start[0]) : self.rt.format(end[0])
                                ,self.ct.format(start[1]):self.ct.format(end[1]) ].astype('str') == '0')\
                |\
               (self.board.loc[ self.rt.format(start[0]) : self.rt.format(end[0])
                                ,self.ct.format(start[1]):self.ct.format(end[1]) ].astype('str')  == name)).all().all()
        
        '''
        print(self.rt.format(start[0]), self.rt.format(end[0]),self.ct.format(start[1]),self.ct.format(end[1]))
        return ((self.board.loc[ self.rt.format(start[0]) : self.rt.format(end[0])
                                ,self.ct.format(start[1]):self.ct.format(end[1]) ] == 0)\
                |\
               (self.board.loc[ self.rt.format(start[0]) : self.rt.format(end[0])
                                ,self.ct.format(start[1]):self.ct.format(end[1]) ] == name)).all().all()
        '''
    def update_board(self,name,start,end):
        #[0] = row
        #[1] = col
    
        #print(start,end)
        #print(self.board.loc[ self.rt.format(start[0]) : self.rt.format(end[0]) ,self.ct.format(start[1]):self.ct.format(end[1]) ])
        self.board.loc[ self.rt.format(start[0]) : self.rt.format(end[0]) \
                        ,self.ct.format(start[1]):self.ct.format(end[1]) ] = name
        #print(self.board)
                        
    def clear_pos(self,block,start,end):
        
        self.update_board(0,start,end)
    
    def move(self,block,start,move_direction,allow_direction):
        
        old_start = start
        old_end = self.get_end_pos(block,start)        
        
        if move_direction == 'up':
            start = (start[0]-1,start[1])# row - 1
        elif move_direction == 'down':
            start = (start[0]+1,start[1])# row + 1
        elif move_direction == 'right':
            start = (start[0],start[1]+1)# col + 1
        else: #left
            start = (start[0],start[1]-1)# col - 1
        
        end = self.get_end_pos(block,start)
        
        if block.direction == allow_direction and self.chk_start_end_pos(start,end) \
            and self.is_empty(start,end,block.name) :
            self.clear_pos(block,old_start,old_end)
            return self.place_block(block,start)
        else:
            return False
        
    def move_down(self,block,start):
        '''
        old_start = start
        old_end = self.get_end_pos(block,start)
        start = (start[0]+1,start[1])
        end = self.get_end_pos(block,start)
        if block.direction == 'down' and self.chk_start_end_pos(start,end) \
            and self.is_empty(start,end,block.name) :
            self.clear_pos(block,old_start,old_end)
            return self.place_block(block,start) # row + 1
        else:
            return False
        '''
        return self.move(block,start,'down','down')
            
    def move_up(self,block,start):
        return self.move(block,start,'up','down')
            
    def move_right(self,block,start):
        return self.move(block,start,'right','right')
        
    def move_left(self,block,start):
        return self.move(block,start,'left','right')
    
        
class Block:
    def __init__(self,name,size,direction):
        self.name = name
        self.size = size
        self.direction = direction #down or right
        '''
        self.start = start #a tuple of (row,col)
        if self.direction == 'down':
            
            self.end = (start[0]+size-1 , start[1]) #a tuple of (row,col)
        else:#right
            self.end = (start[0] , start[1]+size-1)#a tuple of (row,col)
        '''


