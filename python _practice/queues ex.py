print("-------------- example que -----------")
n = int(input())
s = ""
if(n % 3 ==0):
    s +="Pling"
if(n % 5 == 0):
    s +="Plang"
if(n % 7 == 0):
    s +="Plong"
if(n % 3!=0 and n %5 != 0 and n % 7 != 0):
    print(s)