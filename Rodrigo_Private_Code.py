from collections import defaultdict
import sys
import math
import timeit
import random
import time
import operator
import heapq
import itertools

pq = []                         # list of entries arranged in a heap
entry_finder = {}               # mapping of tasks to entries
REMOVED = '<removed-task>'      # placeholder for a removed task
counter = itertools.count()     # unique sequence count

def add_task(task, priority=0):
    'Add a new task or update the priority of an existing task'
    if task in entry_finder:
        remove_task(task)
    count = next(counter)
    entry = [priority, count, task]
    entry_finder[task] = entry
    heapq.heappush(pq, entry)

def remove_task(task):
    'Mark an existing task as REMOVED.  Raise KeyError if not found.'
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED

def pop_task():
    'Remove and return the lowest priority task. Raise KeyError if empty.'
    while pq:
        priority, count, task = heapq.heappop(pq)
        if task is not REMOVED:
            del entry_finder[task]
            return task
    raise KeyError('pop from an empty priority queue')



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
    # pq = [] #priority quee min-heap
    timeStart = time.time()
    d = {}
    open = {}
    open[s] = True
    d[s] = True
    father = {}
    for key in adjl:
        father[key] = None
        open[key] = True
        if (str(key) != s):
            d[key] = math.inf
        else:
            d[key] = 0
            # d2 = 0 #depth

            # father2 = None # ?
            # entry = [d2, father2, node]
            # entry = [d2, key]
            # heapq.heappush(pq, entry)
            add_task(key, 0)
    while pq:
        rootNode = pop_task()
        open[rootNode] = False

        if rootNode not in adjl:
            continue

        for neighbour in adjl[rootNode]:
            if neighbour[0] not in open:
               open[neighbour[0]] = True
            if neighbour[0] not in d:
                d[neighbour[0]] = math.inf
            if open[neighbour[0]]:
                f_score, nb_element_cost = f_value(adjl, rootNode, neighbour[0], d[rootNode], t_start, t_end)

                #RELAX
                if f_score + nb_element_cost  < d[neighbour[0]]:
                    d[neighbour[0]] = f_score + nb_element_cost
                    father[neighbour[0]] = rootNode

                #Update heap
                add_task(neighbour[0], d[neighbour[0]])

    return time.time() - timeStart

def f_value(adj, x, v, i, t_start, t_end):
    #cost is traversal cost
    min = math.inf
    cost = None
    for nb in adj[x]:
        if nb[0] == v and min > float(nb[2]) and t_start <= float(nb[2]) and float(nb[2]) <= t_end and \
                        t_start <= float(nb[2]) + float(nb[1]) and float(nb[2]) + float(nb[1]) <= t_end:
            min = float(nb[2])
            cost = float(nb[1])
    return min, cost

def computerUFJ_latest(s, adjl, t_start, t_end):
    # pq = [] #priority quee min-heap
    d = {}
    open = {}
    open[s] = True
    d[s] = True
    father = {}
    for key in adjl:
        father[key] = None
        open[key] = True
        if (str(key) != s):
            d[key] = math.inf
        else:
            d[key] = 0
            # d2 = 0 #depth

            # father2 = None # ?
            # entry = [d2, father2, node]
            # entry = [d2, key]
            # heapq.heappush(pq, entry)
            add_task(key, 0)
    while pq:
        rootNode = pop_task()
        open[rootNode] = False

        if rootNode not in adjl:
            continue

        for neighbour in adjl[rootNode]:
            if neighbour[0] not in open:
               open[neighbour[0]] = True
            if neighbour[0] not in d:
                d[neighbour[0]] = math.inf
            if open[neighbour[0]]:
                f_score, nb_element_cost = f_value(adjl, rootNode, neighbour[0], d[rootNode], t_start, t_end)

                #RELAX
                if f_score + nb_element_cost  < d[neighbour[0]]:
                    d[neighbour[0]] = f_score + nb_element_cost
                    father[neighbour[0]] = rootNode

                #Update heap
                add_task(neighbour[0], d[neighbour[0]])

    return d, father

def initDict(src, value):
    f = open(src)
    dict = {}
    for line in iter(f):
        u, v, alpha, t = line.split()
        dict[u] = value
        dict[v] = value
    f.close()
    return dict

def earliest_arrival_time(dict, x, t_start, t_end, f):
    # timeStart = time.time()
    dict[x] = t_start
    for line in iter(f):
        u, v, alpha, t = line.split()
        u, v, alpha, t = str(u), str(v), float(alpha), float(t)
        if (t+alpha) <= t_end and t >= float(dict[u]): #tstart instead of dict u?
            if t+alpha < float(dict[v]):
                dict[v] = t + alpha
        elif t >= t_end:
            break
    # return time.time() - timeStart
    return dict

def fastest_path_one_pass(x, t_start, t_end, file_src):
    lv = defaultdict(list) #init dict key is node value is a list (s,a) Lv
    f = initDict(file_src, math.inf)
    f[x] = 0
    edge_stream = open(file_src)
    for edge in iter(edge_stream): #for each edge (u, v, t, alpha) in the file
        u, v, alpha, t = edge.split()
        alpha, t = float(alpha), float(t)
        if t >= t_start and t+alpha <= t_end:
            if u == x:
                if [t,t] not in lv[x]:
                    lv[x].append([t,t])
            su_prime, au_prime = get_max_au(lv, u, t)
            sv, av = su_prime, t+alpha
            sv_in_Lv = False # if sv in lv[v]
            for x in lv[v]: #we could speed this section using bisect sort from python
                if x[0] == sv:
                    x[1] = av
                    sv_in_Lv = True
                    break
            if not sv_in_Lv:
                lv[v].append([sv, av])
            remove_dominated_elements(lv) #Remove dominated elements in Lv
            if av - sv < f[v]:
                f[v] = av - sv
        else:
            break
    edge_stream.close()
    return f

def get_max_au(dict_lv, u, t):
    max = [-math.inf, -math.inf]
    for element in dict_lv[u]:
        if max[1] < element[1] and element[1] <= t:
            max = element
    return max

def remove_dominated_elements(dict):
    for node in dict:
        dominated = []
        for path in dict[node]:
            for path2 in dict[node]:
                pass


if __name__ == "__main__":
    fastest_path_one_pass('A', 0, math.inf, 'dataset/test_earliest.csv')

    #update test
    lv = defaultdict(list)
    lv['A'].append([3,3])
    lv['A'].append([2,2])
    lv['A'].append([1,5])
    lv['B'].append([1,1])
    sv = 1
    av = 99
    print(lv['A'])
    for x in lv['A']:
        if x[0] == sv:
            x[1] = av
    print(lv.items())




    # print(get_max_au(lv, 'A', 10))

    # lv = defaultdict(list)
    # lv['A'].append(1)
    # lv['A'].append([1,1])
    # my_elements = lv['A']
    # print(my_elements)
    # print(lv.items())








    #earliest test
    # earliest_src_file = 'dataset/test_earliest.csv'
    # f = open(earliest_src_file)
    # db = initDict(earliest_src_file, math.inf)
    # # print(db)
    # print(earliest_arrival_time(db, 'A', 0, math.inf, f))
    # f.close()


    #test numpy

    # import numpy as np
    # my_array = np.empty(841372, dtype=object)
    # line = '1 2 1 567897'
    # a, b, c, d = line.split()
    # np.put(my_array, [0], a)
    # print(my_array)


    #test for latest on Xuan
    # my_adj = makeAdjacencyList('dataset/ufj_test.csv')
    # dd, ff = computerUFJ_latest('A', my_adj, 0, math.inf)
    # print(dd)
    # print('Father section')
    # print(ff)
    # print(f_value(my_adj, 'A', 'B', 0, 0, math.inf))

























