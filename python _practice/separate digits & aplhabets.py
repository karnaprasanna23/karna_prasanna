print("-----------seperate digits and alphabets-------------")

l = ['a',1,'c',7,'g',9]
l2 = []
l3 = []
for i in l:
    if str(i).isalpha():
        l2.append(i)
    else:
        l3.append(i)
print(sorted(l2))
print(sorted(l3))