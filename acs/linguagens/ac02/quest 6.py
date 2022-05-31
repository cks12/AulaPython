i,f = int(input()), int(input())
p = 0
def test (n):
    m = 0
    for count in range (2,n):
        if(n % count == 0):
            m += 1
    return m == 0

for e in range(i,f):
    e += 1
    if test(e):
        print(e)
        p+=1
s = f"primos: {p}"
print(s)