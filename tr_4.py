
functions = []
f = open('results_4_4723.txt', 'r')
while True:
    # считываем строку
    functions = f.readlines()
   
f.close
#with open('results_4_4723.txt', 'r') as f:
    

def count_new(m, n, k):
    summa = 0
    count0 = 0
    count1 = 0
    if (k == 15):
        print(count0,"-", k, "-", count1)
    else :
        for i in range(m, n):
            a = functions[i][k]
            if a == 0:
                count0 += 1
            else:
                count1 += 1
        k +=1
        if count0 >= count1 :
            
            count_new (m, count0 + m, k)
            print (m, n, k)
        else:
            
            count_new (m + count0, n, k)
            print (m, n, k)
    z = [count0, count1]
    if max(z) != 0:
        print(max(z),z.index(max(z)))
    #return z       
    
count_new (0,len(functions),0)
