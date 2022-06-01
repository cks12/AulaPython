t1,t2 = input(), input()
t1,t2 = int(t1), int(t2)

def t(i):
    i = int(i)
    for c in range(10):
        c += 1
        s = f"{i} x {c} = {c*i}"
        print(s)
    print('-'*10)

if t1 > t2:
    print("Nenhuma tabuada no intervalo!")

for num in range(t1, t2+1):
    t(num)
