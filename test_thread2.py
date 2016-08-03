# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 00:33:34 2016

@author: nattawutvejkanchana
"""
'''
def multi_run_wrapper(args):
   return add(*args)
def add(x,y):
    return x+y
if __name__ == "__main__":
    from multiprocessing import Pool
    pool = Pool(4)
    results = pool.map(multi_run_wrapper,[(1,2),(2,3),(3,4)])
    print(results)
'''
from multiprocessing import Pool
def multi_run_wrapper(args):
   return in_l(*args)
def in_l(l,x):
    return x in l
if __name__ == "__main__":
    al = [i for i in range(0,10)]
    pool = Pool(4)
    results = pool.map(multi_run_wrapper,[(al[:3],2),(al[3:8],2),(al[8:],2)])
    print(results)