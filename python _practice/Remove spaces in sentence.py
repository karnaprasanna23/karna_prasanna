import math 
s = "have a nice day"
s = s.replace(" ","")
print(s)
rows = math.floor(math.sqrt(len(s)))
cols= math.ceil(math.sqrt(len(s)))
for _ in range(rows):
    for _ in range(cols):
        print(s[i],end="")
        i+=1
    print("")
    
    
    
    
