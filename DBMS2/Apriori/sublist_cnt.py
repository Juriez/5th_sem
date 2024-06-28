ls = [3,4,6,5,1,4,2,1,4,2,5,1,4,5]
ls2 = [2,5,1,4,5,6]
als = [ls, ls2]

sls = [1,4]
cnt = 0

for j in range(0, len(als)):
    nls = als[j]
    for i in range(0, len(nls)):
        
        if ls[i:len(sls)+i] == sls:
            print(ls[i:len(sls)+i]) 
            cnt += 1
        
print(cnt)
   