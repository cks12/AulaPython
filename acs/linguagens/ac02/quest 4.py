dv, vp = int(input()), int(input())
pg, rest= dv//vp,dv%vp
def printPg(pag,af):
    s = f"pagamento: {pag}\nantes = {dv}\ndepois = {dv - af}\n-----"
    print(s)
    return dv-af
for i in range(pg): 
    dv = printPg(i+1,vp)
if rest != 0:
    dv = printPg(pg+1, rest)