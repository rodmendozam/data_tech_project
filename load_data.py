import sys




def earliest_arrival_time(dict, x, t_start, t_end ):
    dict[x] = t_start
    # f = open('dataset/out.epinions')
    f = open('dataset/test.csv')
    for line in iter(f):
        u, v, alpha, t = line.split()
        u, v, alpha, t = str(u), str(v), int(alpha), int(t)

        if (t+alpha) <= t_end and t >= int(dict[u]):
            if t+alpha < int(dict[v]):
                dict[v] = t + alpha
        elif t >= t_end:
            break
    return dict


if __name__ == "__main__":

    # f = open('dataset/out.epinions')
    f = open('dataset/test.csv')
    dict = {}
    for line in iter(f):
        u, v, alpha, t = line.split()
        dict[u] = sys.maxsize
        dict[v] = sys.maxsize
    f.close()


    result = earliest_arrival_time(dict, '1', 0, sys.maxsize)
    print(result)




# print(dict)


# Read file
# f = open('dataset/out.epinions')
# for line in iter(f):
#     u, v, alpha, t = line.split()
#     print(u)
#     break
# f.close()