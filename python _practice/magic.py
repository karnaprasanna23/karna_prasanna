s = "PaanLea"
s1 = "rsnael"
i=0
j=0
s2=""
while(i<len(s) and j<len(s1)):
    s2+=s[i]+s1[j]
    i+=1
    j+=1
s2+=s[i:]+s1[j:]
print(s2)
