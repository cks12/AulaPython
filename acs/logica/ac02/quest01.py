n1,n2 = 10, 5

if n1%n2>1:
    print(True)

    if 3+5/n2>4:
        print(True)
        print(n1)
else:
    print(False)
    if n1/n2>1:
        print(True)
        n2=n1+5
    else:
        print(False)

        n1=n2=5

if 2+n1/2*3>=18:
    print(True)
    n2=n2%n1
else:
    print(False)
    n1=n1%n2

print(n1 + n2)