l = [3, 7, 8, 5, 4]
target = 11
s = set()
for num in l:
    comp = target - num
    if comp in s:
        print(num,comp)
    s.add(num)
    
    
    
l = [3, 7, 8, 5, 4]
k = 11
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]+l[j]==k:
            print(l[i],l[j])
