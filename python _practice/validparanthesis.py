s = "[{()}]"
l = []
for i in s:
    if i =="[":
        l.append("]")
    elif i =="{":
        l.append("}")
    elif i =="(":
        l.append(")")
    else:
        if i==l[-1]:
            l.pop()
        else:
            break
if len(l)==0:
    print("valid")
else:
    print("not valid")
   
print("--------------postfix-----------------")  
   
s = "923*+" 
stack = []
for i in s:
    if i.isdigit():
       stack.append(int(i))
    else:
        x = stack.pop()
        y = stack.pop()
        if i =="*":
            stack.append(y*x)
        elif i == "+" :
            stack.append(y+x)  
print(stack[0])
        
print("--------------prefix----------------")      
        
# s = "+*765" 
# stack = []
# for i in s:
#     if i.isdigit():
#        stack.append(int(i))
#     else:
#         x = stack.pop()
#         y = stack.pop()
#         if i =="*":
#             stack.append(y*x)
#         elif i == "+" :
#             stack.append(y+x)  
# print(stack[0])     
    
    
s = "49142"
k = 3
i = 0
while(i+k <= len(s)):
    print(s[i:i+k])
    i+=1
    


        
