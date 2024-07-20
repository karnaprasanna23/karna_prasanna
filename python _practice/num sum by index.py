print("------index-----------")
l =[2,5,7,6,2]
target = 9                          # here by adding the numbers to equal the target then print their index nums
for i in range(len(l)):                             
    for j in range(i+1, len(l)):
        if l[i] + l[j] == target:
            print(i, j) 
            
            