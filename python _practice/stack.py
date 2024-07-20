print("-----------stack----------")
        
s = [3,1,2,0,4,0,0,3,0]
stack = []
for i in s:
    if i != 0:
        stack.append(i) 
    else:
        print(stack.pop())
        
        