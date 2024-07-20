print("----------reverse two - two letters in a str---------")

s = ["jaksd","jdhf","kjdshfy","uewryff"]
r1 = s[:2][::-1]
r2 = s[2:][::-1]
print(r1,r2)


s = "prasanna"
s2=""
i=0
while(i<len(s)-1):
    s2 += s[i:i+2][::-1] + " "
    i+=2
print(s2)

# r2 = s2[2:4][::-1]
# r3 = s2[4:6][::-1]
# r4 = s2[6:8][::-1]
# print(r1,r2,r3,r4)
# m = r1,r2,r3,r4
# for i in m:
#     i = r1+r2+r3+r4
# print(i)
# n = i
# i="".join(i)
# print(i)
# r = i
# r=r.replace((' '),(''))
# print(r.replace(" ",""))