print("-----------reverse string--------------")
s = "hello"
rev = ""
for i in range(len(s)-1,-1,-1):
    rev = rev+s[i] 
    print(rev)
print("-------------another method-----------------")
rev2 = ""
for i in s:
    rev2 = i + rev2
print(rev2)


s = "malayalam"
i = 0
j =  len(s)-1
p = True
while(i<j):
    if s[i] != s[j]:
        p = False
        break
    i += i
    j -= j
if p ==True:
    print("palindrome")
else:
    print("not")
        
print("-------reverse number-----------")
 
n = str(int(15432))
print(n[::2])
     
print("----------another method-----------")
    
n = 12345
rev = 0
while(n):
    rem =n % 10
    rev = rev * 10 + rem
    n = n//10
print(rev)