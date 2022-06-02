nts, out, alns, cng = [], [], input(), 0
alns = int(alns)

for i in range(0,alns):
    temp = input()
    temp = float(temp)
    nts.append(temp)

for i in range(0, alns):
    temp = input()
    temp = float(temp)
    nt = nts[i]

    if nt < 10 and temp == 10:
        cng+=1
        nt += 2 if nt < 9 and temp == 10 else 1

    out.append(nt)

print(f"NOTAS ALTERADAS: {cng}")

for index, o in enumerate(out):
    original, final = nts[index], o
    string = f"{'*' if final != original else '-'}({index + 1:0>3}) original: {original:0^5} | final: {final:0^5}"
    print(string)