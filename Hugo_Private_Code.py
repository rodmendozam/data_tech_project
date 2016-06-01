import sys
import math
import timeit
import random
import time
import operator

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