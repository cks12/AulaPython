import os 

db = {
    "discount":.15,
    "comboDiscount":.25,
    "price":5,
    "formasDePagamento":[
        "Dinheiro",
        "Pix",
        "Outro"
    ]
}

def clear ():
    os.system('cls' if os.name == 'nt' else 'clear')

def inputFloat(txt: str) -> float:
    userInput = input(txt)
    try:
        return float(userInput)
    except: 
        print("Digite um valor numerico")
        return inputFloat(txt)

def choiceAOption(arr = []) -> str or int or float or any: 
    for index, element in enumerate(arr):
        string = "[{}]. {}".format(index,element)
        print(string)
    
    try:
        choice = inputFloat("> Por favor escolha uma opção:")
        return arr[int(choice)]
    except:
        print("> Por favor escolha uma opção valida!!!")
        return choiceAOption(arr = arr)

def aulaPart1(qtn: float or int) -> float or int:
    valueTotal = qtn * db["price"]
    if qtn >= 4:
        string = "> Como você comprou mais de 4, um desconto de {v}% será aplicado ".format(v=db["discount"] * 100)
        print(string)
        return valueTotal - valueTotal * db["discount"]
    return valueTotal 

def aulaPart2(qtn: float or int) -> float or int:
    valueTotal = qtn * db["price"]
    string = "> Você esta comprando um pacote !!\n Você ira ganhar um desconto de {a}%".format( a=db["comboDiscount"] * 100)
    print(string)
    return valueTotal - valueTotal * db["comboDiscount"] 

if __name__ == "__main__":
    clear()
    print('''
{e}
Gerealdão desistiu de rivia e decidiu abrir uma loja de doces
Então seja bem vindo a FUCKIN LOJA DE DONUTS DO GERALDÂO!!!!
{e}    
'''.format(e="."*100))
    qnt = inputFloat("> Digite a quantidade: ")
    formasDePagamento = choiceAOption(db['formasDePagamento'])
    valueTotal = aulaPart2(qnt) if (formasDePagamento != "Outro") and (qnt%4 == 0) else aulaPart1(qnt)
    string = "> Você precisa pagar {}".format(valueTotal)
    print()