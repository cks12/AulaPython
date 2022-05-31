cp = []
l = 0
def userInput() -> None:
    ui = input()
    ui = ui.split(" ")
    return ui

ui = userInput()

if ui:
    cp = ui

while l >= 0:
    ui = userInput()

    if ui[0] == "adicionar":
        s = f"{ui[1]}"
        cp.append(s)
    
    if ui[0] == "remover":
        try:
            cp.remove(ui[1])
        except:
            s = f"código {ui[1]} não encontrado"
            print(s)

    if ui[0] == "exibir":
        cp.sort(key = int)
        print(*cp)

    if ui[0] == "encerrar":
        cp.sort(key = int)
        print(*cp)
        break

    l+=1