def fibonacci(n):
    a = 0
    b = 1
    f=[0,1]
    for _ in range(n-2):
        c = a+b
        a = b
        b = c
        f.append(c)
    return(f)
    
n = int(input())
print(fibonacci(n))
print(sum(fibonacci(n)))