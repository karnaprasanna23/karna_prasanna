p = [1,1,1,4,3,2]
s = 5
k=s
c = 0
for i in p:
    if s>=p[i]:
        s-=i
        c+=1
    else:
         c+=p.index(i)*2+1
         s=k
         s=s-i
print(c) 
 
 
l = [[1,2],[2,5],[4,3]]   