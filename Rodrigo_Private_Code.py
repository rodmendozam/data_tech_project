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



if __name__ == "__main__":

    my_adj = makeAdjacencyList('dataset/ufj_test.csv')

    dd, ff = computerUFJ('A', my_adj, 0, math.inf)
    print(dd)
    print('Father section')
    print(ff)
    # print(f_value(my_adj, 'A', 'B', 0, 0, math.inf))


    # add_task( 'A', 3)
    # add_task( 'B', 1)
    # add_task( 'C', 2)
    # add_task( 'D', 1)
    # add_task( 'F', 0)
    # print(pq)
    #
    # add_task( 'C', 1)
    # print( pop_task() )
    # # print( pop_task() )
    # # print( pop_task() )
    # # print( pop_task() )
    #
    # print(pq)


    #
    # ordered = []
    # while pq:
    #     value = heapq.heappop(pq)
    #     ordered.append(pop_task())
    # print(ordered)


    #create adj lst
    # print(makeAdjacencyList('dataset/test.csv'))

    # my_adj = makeAdjacencyList('dataset/test.csv')
    #
    # for key in my_adj:
    #     print(type(key))


    # heap_test = []
    # heapq.heappush(heap_test, (1, ''))
    #
    #
    # # search for an element by key in a min heap
    # heap = []
    # heapq.heappush(heap, Element('B', 2))
    # heapq.heappush(heap, Element('C', []))
    # heapq.heappush(heap, Element('A', 1))
    # heapq.heappush(heap, Element('A', 22))
    #
    # # heapq.heapreplace(Element('A', 1),Element('A', 222))
    #
    # print( search_in_heap_element(heap, Element('A', 1)) )
    #
    # #print heap example
    # ordered = []
    # while heap:
    #     value = heapq.heappop(heap)
    #     ordered.append([value.key, value.value])
    # print(ordered)
























