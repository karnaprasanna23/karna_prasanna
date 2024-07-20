# print count of list
a=[9,2,7,1,5,2,9,7,5]
d={}
for i in a:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)




    
