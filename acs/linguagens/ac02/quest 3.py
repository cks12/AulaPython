rs,vc = 0,0 
while True:
    i = float(input())
    if i == -1:
        break
    vc += i
    rs += i *2.5
s = f"VC$ {vc:.2f}\nR$ {rs:.2f}"
print(s)