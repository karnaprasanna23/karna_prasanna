# print ("-------------leap year or not------------") 
n = int(input())
if(n%4==0 and n%100!=0) or n%400==0:
    print("leap")
else:
    print("not")
    
    

print("--------------which two numbers equal to target-------------")      
l =[2,5,7,6,2]
target = 9
for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i] + l[j] == target:           
            print(i, j) 