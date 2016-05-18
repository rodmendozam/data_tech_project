import sys




def earliest_arrival_time(src, x, t_start, t_end ):
    dict = initDict(src,sys.maxsize)
    dict[x] = t_start
    # f = open('dataset/out.epinions')
    f = open(src)
    for line in iter(f):
        u, v, alpha, t = line.split()
        u, v, alpha, t = str(u), str(v), int(alpha), int(t)

        if (t+alpha) <= t_end and t >= int(dict[u]):
            if t+alpha < int(dict[v]):
                dict[v] = t + alpha
        elif t >= t_end:
            break
    return dict

def latest_depature_time(src, x, t_start, t_end ):
    dict = initDict(src,-sys.maxsize)
    dict[x] = t_end
    # f = open('dataset/out.epinions')
    f = open(src)
    for line in reversed(list(f)):
        u, v, alpha, t = line.split()
        u, v, alpha, t = str(u), str(v), int(alpha), int(t)
        if int(t) >= int(t_start):
            if (t+alpha) <= int(dict[v]):
                if t > int(dict[u]):
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


if __name__ == "__main__":
    src = 'dataset/test.csv'
    print(latest_depature_time(src,'4',0,sys.maxsize))
    # f = open('dataset/out.epinions')

    #result = earliest_arrival_time(dict, '1', 0, sys.maxsize)
    #print(result)




# print(dict)


# Read file
# f = open('dataset/out.epinions')
# for line in iter(f):
#     u, v, alpha, t = line.split()
#     print(u)
#     break
# f.close()