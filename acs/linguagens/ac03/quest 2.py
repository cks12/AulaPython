t1,t2 = input(), input()

def t(i):
    i = int(i)
    for c in range(10):
        c += 1
        s = f"{i} x {c} = {c*i}"
        print(s)
    print('-'*10)

t(t1)
t(t2)