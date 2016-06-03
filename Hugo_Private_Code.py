import sys
import math
import timeit
import random
import time
import operator
import heapq

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

def computerUFJ(s, adjl):
    pq = []
    d = {}
    open = {}
    father = {}
    for key in adjl:
        father[key] = None
        open[key] = True
        if (str(key) != s):
            d[key] = math.inf
        else:
            d[key] = 0
            d2 = 0
            node = key
            father2 = None
            entry = [d2, father2, node]
            heapq.heappush(pq, entry)
    while pq != []:
        root = heapq.heappop(pq)
        rootNode = root[2]
        open[rootNode] = False
        for neighbour in adjl[rootNode]:
            if open[neighbour]:
                print('Placeholder to not make it crash')
                #Rodrigo continue step c) from i) here

    return pq