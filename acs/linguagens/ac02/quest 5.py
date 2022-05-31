i,f = int(input()), int(input())
c = f-i + 1
b = 0
for cont in range(c):
    y = cont + i
    if (y%4==0 and y%100!=0) or (y%400==0):
        print(y)
        b +=1 

s = f"bissextos: {b}"
print(s)