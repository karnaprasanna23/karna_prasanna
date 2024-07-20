n = input()
s= list(map(int,input().split()))
c = 0                                      # for this outputs values will be [ 1 3 2 4 2 
for i in s:                                 #                                 5 3 2 5 1]
    if s.count(i)==1:                        # then it prints the distinct nums
        print(i,"is distinct number")
        c+=1
print("total distinct numbers are",c)
