import sys
import math
import timeit
import random
import time
import operator
from Hugo_Private_Code import *
from Advaita_Private_Code import *
from Rodrigo_Private_Code import *

def earliest_arrival_time(dict, x, t_start, t_end, f):
    timeStart = time.time()
    dict[x] = t_start
    for line in iter(f):
        u, v, alpha, t = line.split()
        u, v, alpha, t = str(u), str(v), float(alpha), float(t)

        if (t+alpha) <= t_end and t >= float(dict[u]):
            if t+alpha < float(dict[v]):
                dict[v] = t + alpha
        elif t >= t_end:
            break
    return time.time() - timeStart

def earliest_arrival_time_xuan(dict, x, t_start, t_end, f):
    timeStart = time.time()
    dict[x] = t_start
    return time.time() - timeStart

def latest_depature_time(dict, x, t_start, t_end, f):
    timeStart = time.time()
    # dict = initDict(src,-math.inf)
    dict[x] = t_end
    # f = open('dataset/out.epinions')
    # f = open(src)
    for line in reversed(list(f)):
        u, v, alpha, t = line.split()
        u, v, alpha, t = str(u), str(v), float(alpha), float(t)
        if float(t) >= float(t_start):
            if (t+alpha) <= float(dict[v]):
                if t > float(dict[u]):
                    dict[u] = t
        else:
            break
    return time.time() - timeStart

def initDict(src, value):
    f = open(src)
    dict = {}
    for line in iter(f):
        u, v, alpha, t = line.split()
        dict[u] = value
        dict[v] = value
    f.close()
    return dict

def makeAdjacencyList(src):
    f = open(src)
    dict = {}
    for line in iter(f):
        u, v, alpha, t = line.split()
        if u not in dict:
            dict[u] = set()
        dict[u].add(v)
    return dict




#def wrapper(func, *args, **kwargs):
#    def wrapped():
#        return func(*args, **kwargs)
#    return wrapped

#def timeAlgorithm(wrappedAlgorithm, iterations):
#    print(timeit.timeit(wrappedAlgorithm, number=iterations) / iterations)





def select_100_random(src):
    graph = initDict(src,sys.maxsize)
    result  = []
    for i in range(0, 100):
        result.append( random.choice(list(graph.keys())) )
    return result

def runExperiments(nodes, db, f):
    total = 0
    for node in nodes:
        total += latest_depature_time(db.copy(), node,0, math.inf, f)
        f.seek(0)
    return float(total) / float(len(nodes))

if __name__ == "__main__":
    src = 'dataset/test.csv'
    #src = 'dataset/out.epinions'
    db = initDict(src,-math.inf)
    f = open(src)
    dict = makeAdjacencyList(src)
    nodes = select_top_10_degree(dict)
    print(computerUFJ('1', dict))
    print(runExperiments(nodes, db, f))
    f.close()

    # #select 100 random nodes
    # data_epinions = 'dataset/out.epinions'
    # select_100_random(data_epinions)
    #
    #
    # # src = 'dataset/test.csv'
    # # print(latest_depature_time(src,'4',0,sys.maxsize))
    # # f = open('dataset/out.epinions')
    #
    # # src = 'dataset/test.csv'
    # src = 'dataset/out.epinions'
    # iterations = 100
    # wrapped = wrapper(latest_depature_time, src,'4',0,math.inf)
    # timeAlgorithm(wrapped, iterations)
    #
    #
    # #print(latest_depature_time(src,'4',0,math.inf))
    # # f = open('dataset/out.epinions')
    #
    # #result = earliest_arrival_time(dict, '1', 0, sys.maxsize)
    # #print(result)
    #
    #
    #


# print(dict)


# Read file
# f = open('dataset/out.epinions')
# for line in iter(f):
#     u, v, alpha, t = line.split()
#     print(u)
#     break
# f.close()
