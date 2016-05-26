import sys
import math
import timeit

def earliest_arrival_time(src, x, t_start, t_end ):
    dict = initDict(src, math.inf)
    dict[x] = t_start
    # f = open('dataset/out.epinions')
    f = open(src)
    for line in iter(f):
        u, v, alpha, t = line.split()
        u, v, alpha, t = str(u), str(v), float(alpha), float(t)

        if (t+alpha) <= t_end and t >= float(dict[u]):
            if t+alpha < float(dict[v]):
                dict[v] = t + alpha
        elif t >= t_end:
            break
    return dict

def latest_depature_time(src, x, t_start, t_end ):
    dict = initDict(src,-math.inf)
    dict[x] = t_end
    # f = open('dataset/out.epinions')
    f = open(src)
    for line in reversed(list(f)):
        u, v, alpha, t = line.split()
        u, v, alpha, t = str(u), str(v), float(alpha), float(t)
        if float(t) >= float(t_start):
            if (t+alpha) <= float(dict[v]):
                if t > float(dict[u]):
                    dict[u] = t
        else:
            break
    return dict

def initDict(src, value):
    f = open(src)
    dict = {}
    for line in iter(f):
        u, v, alpha, t = line.split()
        dict[u] = value
        dict[v] = value
    f.close()
    return dict

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

def timeAlgorithm(wrappedAlgorithm, iterations):
    print(timeit.timeit(wrappedAlgorithm, number=iterations) / iterations)


if __name__ == "__main__":
    src = 'dataset/test.csv'
    src = 'dataset/out.epinions'
    iterations = 100
    wrapped = wrapper(latest_depature_time, src,'4',0,math.inf)
    timeAlgorithm(wrapped, iterations)
    #print(latest_depature_time(src,'4',0,math.inf))
    # f = open('dataset/out.epinions')

    #result = earliest_arrival_time(dict, '1', 0, math.inf)
    #print(result)




# print(dict)


# Read file
# f = open('dataset/out.epinions')
# for line in iter(f):
#     u, v, alpha, t = line.split()
#     print(u)
#     break
# f.close()