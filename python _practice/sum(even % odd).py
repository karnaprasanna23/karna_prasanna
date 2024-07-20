l = [1,2,3,4,5,6]
s = 0
p = 0
for i in l:
    if i % 2 == 0:
       s +=i           # it prints sum of even numbers
    elif i % 2 != 0:
        p += i         # it prints sum of odd numbers
print(s/p)             # it prints divison of both even and odd


