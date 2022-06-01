counter, cns, cnsOut = input(), [], []
counter = int(counter)

for i in range(0,counter):
    temp = input()
    temp = temp.split(";")
    temp[1] = int(temp[1])
    temp[2] = float(temp[2])
    cns.append(temp)

X,Y = input(), input()
X,Y = float(X),float(Y)

for cn in cns:
    subs, cpm, prem = cn[1], cn[2], cn[3]
    print(prem)
    count = cpm * X if prem == "sim" else cpm * Y
    temp = [cn[0],count]
    cnsOut.append(temp)

print(cnsOut)