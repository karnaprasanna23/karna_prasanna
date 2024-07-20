s = "As Soon As Possible" 
s1 = ""  
s = s.split()                            
print(s)
s1=s
s2 = ""
for i in s1:
    s2= s2 + i[0]
print(s2)

print("----------------first letters ---------")

s = input()
# s2 = ""
# for i in s.split(" "):
s3 = s[0].upper()
for i in range(len(s)-1):
    if s[i]== " " or s[i]== "-":
        s3+=s[i+1].upper
print(s3)


    
print("------------- 2 powers ----")
    
n = int(input())
print(2**(n-1))


