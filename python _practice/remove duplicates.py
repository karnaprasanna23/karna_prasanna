print("---------------remove duplicates-----------")
l = [1, 5, 2, 1, 6, 2, 2]
s = []
for i in l.copy():
    if i in s:
        l.remove(i)
    else:
        s.append(i)
print(l)


print("------------ another method----------------")
k = []
for i in l:
    if i not in k:
        k.append(i)
print(k)