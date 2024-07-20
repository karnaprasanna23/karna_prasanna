A= [[3, 7],[6, 4]]
B = [[4, 2],[8, 4]
]
f = True
r1 = len(A)
c1 = len(A[0])
r2 = len(B)
c2 = len(B[0])
if(r1 != r2 or c1 != c2):
    print("not equal")
else:
    for i in range(0, r1):
        for j in range(0, c1):
            if A([i][j] != B[i][j]):
                f = False
                break
        if(f):
            print("equal")
        else:
            print("not")
        