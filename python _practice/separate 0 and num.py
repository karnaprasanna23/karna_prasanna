print("-------------separate zeros and numbers-------- ")  

l = [0, 3, 4, 0, 5, 0, 7]
s = []
p = []
for i in l:
    if i == 0:
        s.append(i)
    else:
        p.append(i)
print(p+s)        # here we can change the zeros and numbers 

print("------another method----------")

l = [0, 3, 4, 0, 5, 0, 7]
for i in l:
    if i == 0:
        l.remove(i)
        l.append(i)
print(l)

