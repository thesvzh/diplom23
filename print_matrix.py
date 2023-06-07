from itertools import combinations

with open('mn_4723.txt') as file1:
    functions = file1.readlines()

def x8(x,y):
    d = {}
    for i in range(len(functions[0]) - 1):
        z = ''.join([functions[k][i] for k in x])
        if z in d:
            d[z] += ''.join([functions[k][i] for k in y]) + ' '
        else:
            d[z] = ''.join([functions[k][i] for k in y]) + ' '
    for k in d:
        d[k] = list(d[k].split())
    return d


def g(s):
    i = 0
    for elem in s:
        if elem == '0':
            i += 1
        else:
            break
    return i, len(s) - i

def zut2(x):

    if len(x) == 0:
        return False
    if len(x[0])==1:
        return True
    mini = 100000000000
    k = 0
    for i in range(len(x)):
        ed = [j for j in range(len(x[i])) if x[i][j]=='1']
        nul = [j for j in range(len(x[i])) if x[i][j]=='0']
        if abs(len(ed)-len(nul)) < mini:
            mini = abs(len(ed)-len(nul))
            k = i

            if len(nul)<=len(ed):
                minii = ed
            else:
                minii = nul
    return zut2([''.join([x[i][j] for j in minii]) for i in range(len(x)) if i != k])


num = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
xy = list(combinations(num,8))
x = [0, 2, 5, 6, 9, 10, 13, 15]
y = tuple(set(num) - set(x))
z = x8(x,y)
q = list(z.keys())
print(q)

xx8 = list(z.values())

with open("otus_0_2_5_6_9_10_13_15.txt", "w") as file:
    summTrue=0
    for k, zk in z.items():
        tr_m = [''.join([zk[stroka][stolb] for stroka in range(len(zk))]) for stolb in range(8)]
        file.write(str(tr_m))
        file.write('\n')
        tr_m = list(set(tr_m))
        tr_m.sort()
        if zut2(tr_m):
            summTrue += 1

    if summTrue == len(q):
        print("POBEDA",len(q), x)


