a, b = map(int,input().split())
b -= 45
if (b<0):
    if a == 0 :
        b += 60
        a = 23
    else:
        b += 60
        a -= 1

print (a ,b)