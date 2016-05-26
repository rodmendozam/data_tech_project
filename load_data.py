import sys
import math
import timeit
import random
import time
import operator

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

def select_100_random(src):
    graph = initDict(src,sys.maxsize)
    result  = []
    for i in range(0, 100):
        result.append( random.choice(list(graph.keys())) )
    return result

if __name__ == "__main__":
    src = 'dataset/test.csv'
    src = 'dataset/out.epinions'
    db = initDict(src,-math.inf)
    f = open(src)
    dict = makeAdjacencyList(src)
    print(select_top_10_degree(dict))
    print(latest_depature_time(db,'4',0,math.inf, f))
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
