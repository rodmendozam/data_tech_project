from collections import Counter
import sys
import math
import timeit
import random
import time
import operator
import numpy as np
import pandas
# from Hugo_Private_Code import *
# from Advaita_Private_Code import *
# from Rodrigo_Private_Code import *

def earliest_arrival_time(dict, x, t_start, t_end, f):
    count = 0
    for line in iter(f):
        count +=1
    # print('Facebook has', count)

    listje = np.empty(count, dtype=object)
    f.seek(0)
    #print("hello")
    timeStart = time.time()
    count = 0
    for line in iter(f):
        #listje = np.append(listje, line)
        np.put(listje, [count], line)
        count += 1
    # f.close()
    timeStart = time.time()
    dict[x] = t_start
    #print(listje)
    totalTime = 0
    for line in listje:
        u, v, alpha, t = line.split()
        u, v, alpha, t = u, v, float(alpha), float(t)
        timeStart = time.time()
        if (t+alpha) <= t_end and t >= dict[u]:
            if t+alpha < dict[v]:
                dict[v] = t + alpha
        elif t >= t_end:
            break
        totalTime += time.time() - timeStart
    return totalTime
    #print(dict)
    #return dict

def earliest_arrival_time_xuan(dict, x, t_start, t_end, f):
    timeStart = time.time()
    dict[x] = t_start
    return time.time() - timeStart

def latest_depature_time(dict, x, t_start, t_end, f):
    # timeStart = time.time()
    # dict = initDict(src,-math.inf)
    dict[x] = t_end
    # f = open('dataset/out.epinions')
    # f = open(src)
    totalTime = 0
    for line in reversed(list(f)):
        u, v, alpha, t = line.split()
        u, v, alpha, t = str(u), str(v), float(alpha), float(t)
        timeStart = time.time()
        if float(t) >= float(t_start):
            if (t+alpha) <= float(dict[v]):
                if t > float(dict[u]):
                    dict[u] = t
        else:
            break
        totalTime += time.time() - timeStart
    return totalTime

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
        entry = (v, alpha,t)
        dict[u].add(entry)
    return dict



def select_top_10_degree_collection(src):
    f = open(src)
    list = []
    for line in iter(f):
        u, v, alpha, t = line.split()
        u, v, alpha, t = str(u), str(v), float(alpha), float(t)
        list.append(v)
    my = Counter(list)
    xy = my.most_common(10)
    f.close()
    return [x[0] for x in xy]

#def wrapper(func, *args, **kwargs):
#    def wrapped():
#        return func(*args, **kwargs)
#    return wrapped

#def timeAlgorithm(wrappedAlgorithm, iterations):
#    print(timeit.timeit(wrappedAlgorithm, number=iterations) / iterations)





def select_100_random(src):
    graph = initDict(src, math.inf)
    result  = []
    for i in range(0, 100):
        result.append( random.choice(list(graph.keys())) )
    return result

def runExperiments(nodes, db, f):
    total = 0
    for node in nodes:
        total += latest_depature_time(db.copy(), node,0, math.inf, f)
        # total += earliest_arrival_time(db.copy(), node, 0, math.inf, f)
        f.seek(0)
    return float(total) / float(len(nodes))

def select_top_10_degree(dist):
    adjl = dist.copy()
    for key in adjl:
        adjl[key] = len(adjl[key])
    sorted_adjl = sorted(adjl.items(), key=operator.itemgetter(1), reverse=True)
    top10 = []
    for i in range (0,10):
        if len(sorted_adjl) >= i + 1:
            top10.append(sorted_adjl[i][0])
    return top10

if __name__ == "__main__":
    #existing files
    src_test = 'dataset/test.csv'
    src_epinions = 'dataset/out.epinions'
    src_facebook = 'datasets_sorted/facebook_sort.txt'
    src_flickr = 'dataset/out.flickr'


    src = src_facebook
    f = open(src)
    db = initDict(src, -math.inf)
    # my_nodes = select_100_random(src_test)
    my_nodes = select_top_10_degree_collection(src)
    print(my_nodes)
    print(runExperiments(my_nodes, db, f))
    f.close()

        #random source

    # runExperiments()


    # dict = makeAdjacencyList(src)
    # print(earliest_arrival_time(db, '111212',0, math.inf, f))
    # #print(earliest_arrival_time(db, '1',0, math.inf, f))
    # adjl = makeAdjacencyList(src)
    # print(computerUFJ('A', adjl, 0, math.inf))
    #print(dict)
    #nodes = select_top_10_degree(dict)
    #print(computerUFJ('1', dict))
    #print(runExperiments(nodes, db, f))
    # f.close()

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
