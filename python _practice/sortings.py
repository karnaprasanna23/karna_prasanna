def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
n = 5
print(fact(n))


print("-------------MERGE SORT--------------")

def merge(a,b):
    i = 0
    j = 0
    res = []
    while(i<len(a) and j<len(b)):
        if a[i]<b[j]:
           res.append(a[i])
           i+=1
        else:
            res.append(b[j])
            j+=1
    res+= a[i:]+b[j:]
    return res
def mergesort(arr):
    n = len(arr)//2
    if len(arr) <2:
         return arr 
    left = mergesort(arr[:n])  
    right = mergesort(arr[n:]) 
    return merge(left, right)
arr = [1,7,4,62,90]
print(mergesort(arr))

print("-------------QUICK SORT-------------")
         
def quicksort(arr): 
    if len(arr)<2:
        return arr
    left = []
    middle =[]
    right =[]
    pivot = arr[len(arr)//2]
    for i in arr:
        if i<pivot:
           left.append(i)  
        elif i==pivot:
           middle.append(i)
        else:
            right.append(i)
    return quicksort(left) +middle + quicksort(right)
arr = [2,4,5,2,8,3]
print(quicksort(arr))
 
 
print("---------------BINARY SEARCH------------")

def binarysearch(arr,target,left,right):
    mid = (left+right)//2
    if arr[mid]==target:
        return mid
    elif target>arr[mid]:
        return binarysearch(arr, target,mid+1,right)
    else:
        return binarysearch(arr,target,left,mid-1)
    return-1
arr = [3,8,12,23,33,45]
print(binarysearch(arr,33,0,len(arr)-1))
   