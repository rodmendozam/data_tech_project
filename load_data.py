import sys

#store in a dictonary the nodes
def init_graph():
    f = open('dataset/out.epinions')
    dict = {}
    for line in iter(f):
        u, v, alpha, t = line.split()
        dict[u] = sys.maxsize
        dict[v] = sys.maxsize
    f.close()


def earliest_arrival_time(dict, x, t_start, t_end ):
    dict[x] = t_start
    f = open('dataset/out.epinions')
    for line in iter(f):
        u, v, alpha, t = line.split()
        u, v = str(u), str(v)

        if (int(t) + int(alpha)) <= t_end and int(t) >= int(dict[u]):
            if t+alpha < dict[v]:
                dict[v] = t + alpha
        elif t >= t_end:
            break
    return dict


if __name__ == "__main__":

    f = open('dataset/out.epinions')
    dict = {}
    for line in iter(f):
        u, v, alpha, t = line.split()
        dict[u] = sys.maxsize
        dict[v] = sys.maxsize
    f.close()

    result = earliest_arrival_time(dict, '23', 0, sys.maxsize)

    print(result)




# print(dict)


# Read file
# f = open('dataset/out.epinions')
# for line in iter(f):
#     u, v, alpha, t = line.split()
#     print(u)
#     break
# f.close()