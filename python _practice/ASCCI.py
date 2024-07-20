s = "yeezy"
s2 = ""
k = 7
for i in s:
    if i.isupper():
        s2+=chr((ord(i)+k-65)%26+65)
    elif i.islower():
        s2+=chr((ord(i)+k-97)%26+97)
    elif i.digit():
        s2+=chr((ord(i)+k-48)%10+48)
print(s2)  