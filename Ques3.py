t = int(input())


def gKey2(values):
    return values[2]


def gKey0(values):
    return values[0]


l1 = []
l2 = []

for i in range(t):
    n = int(input())
    l1.clear()
    for x in range(n):
        l2 = []
        l2 = [int(y) for y in input().split(" ")]
        l2.append(x)
        l1.append(l2)
    l1.sort(key=gKey0)

    j_var = -1
    c_var = -1
    flag = True
    for y in l1:
        t_g = y[0]
        t_h = y[1]
        if c_var == -1:
            c_var = t_h
            y.append('C')
        elif t_g >= c_var:
            c_var = t_h
            y.append('C')
        elif t_g < c_var and t_g >= j_var:
            j_var = t_h
            y.append('J')
        elif t_g < c_var and t_g < j_var:
            flag = False
            break
    if flag == False:
        str = "IMPOSSIBLE"
    else:
        str = ""
        l1.sort(key = gKey2)
        str = str.join([y[3] for y in l1])
    print("Case #{}: {}".format(i+1,str))