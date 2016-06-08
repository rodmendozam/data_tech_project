import sys
import math
import timeit
import random
import time
import operator
import heapq

class Element:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __lt__(self, other):
        return self.key < other.key

def search_in_heap_element(heap, element):
    #maybe stop also if element key is a above the other key since they are sorted less than O(n)
    for e in heap:
        if element.key == e.key:
            return True
    return False

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

def computerUFJ(s, adjl, t_start, t_end):
    pq = [] #heap
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
            if open[neighbour[0]]:
                f_score, nb_element_cost = f_value(adjl, rootNode, neighbour, d[rootNode], t_start, t_end)

                if f_score + nb_element_cost  < d[neighbour]:
                    d[neighbour] = f_score + nb_element_cost
                    father[neighbour] = rootNode

                # if not check if in the min heap


                print('Placeholder to not make it crash')
                #Rodrigo continue step c) from i) here

    return pq

def f_value(adj, x, v, i, t_start, t_end):
    min = math.inf
    cost = None
    for nb in adj[x]:
        if min > nb[2] and t_start >= float(nb[2]) and float(nb[2]) <= t_end and \
                        t_start >= float(nb[2]) + float(nb[1]) and float(nb[2]) + float(nb[1]) <= t_end:
            min = nb[2]
            cost = nb[1]
    return min, cost



if __name__ == "__main__":
    print(makeAdjacencyList('dataset/test.csv'))
    # my_adj_lst = makeAdjacencyList('dataset/test.csv')

    #search for an element by key example
    heap = []
    heapq.heappush(heap, Element('A', 1))
    heapq.heappush(heap, Element('B', 2))
    heapq.heappush(heap, Element('C', 3))
    print( search_in_heap_element(heap, Element('A', 1)) )
























