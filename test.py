with open('mn_4723.txt') as file1:
    functions = file1.readlines()

for k in range(0, 16):
    b = []
    c = 1

    for i in range(len(functions[k])):
        if i < len(functions[k]) - 1 and functions[k][i] == functions[k][i + 1]:
            c += 1
        else:
            if c > 0:
                b.append(c)
                c = 1
            else:
                c += 1
                b.append(c)
    print(b)

# ----------
