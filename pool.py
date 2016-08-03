# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 20:55:07 2016

@author: nattawutvejkanchana
"""

import multiprocessing as mp
import random
import string

random.seed(123)

# Define an output queue
output = mp.Queue()

# define a example function
def rand_string(length, output):
    """ Generates a random string of numbers, lower- and uppercase chars. """
    rand_str = ''.join(random.choice(
                        string.ascii_lowercase
                        + string.ascii_uppercase
                        + string.digits)
                   for i in range(length))
    output.put(rand_str)

# Setup a list of processes that we want to run
processes = [mp.Process(target=rand_string, args=(5, output)) for x in range(4)]

# Run processes
for p in processes:
    p.start()

# Exit the completed processes
for p in processes:
    p.join()

# Get process results from the output queue
results = [output.get() for p in processes]

print(results)


def cube(x):
    return x**3

pool = mp.Pool(processes=4)
results = [pool.apply(cube, args=(x,)) for x in range(1,7)]
print(results)

import time


def cube_a_b(a,b):
    return a**b

for i in [1,2,3,4,5,6,7,8]:
    start_time = time.time()
    pool = mp.Pool(processes=i)
    results = [pool.apply(cube_a_b, args=(x,x+5,)) for x in range(1,30000)]
    #print(results)
    
    elapsed_time = time.time() - start_time
    print(i," processes time:",elapsed_time)