print("------------largest sum in array----------")

l = [1, -2, 4, 3, -6, 4]         #  by adding numbers we want largest sum 
s = 0         #sum
m = l[0]      #max
l2 = []
for i in l:
    s = s+i
    if s<0:
        s=0
    if s>m:
        m=s
        l2.append(i)
print(l2)
print(m)