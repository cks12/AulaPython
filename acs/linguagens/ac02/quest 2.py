alf = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
i = int(input())

if 1 <= i <= 26:
    for c in range(i):
        s = f'{alf[c]}'*int(c + 1)
        print(s)