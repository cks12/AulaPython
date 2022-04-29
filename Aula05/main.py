import os
from time import sleep

def clear ():
    os.system('cls' if os.name == 'nt' else 'clear')


def inputFloat(txt: str) -> float:
    userInput = input(txt)
    try:
        return float(userInput)
    except: 
        print("Digite um valor numerico")
        return inputFloat(txt)

def choiceAOptionInArray(arr = []) -> str or int or float or any: 
    for index, element in enumerate(arr):
        string = "[{}]. {}".format(index,element)
        print(string)
    
    try:
        choice = inputFloat("> Por favor escolha uma opção: ")
        return arr[int(choice)]
    except:
        print("> Por favor escolha uma opção valida!!!")
        return choiceAOptionInArray(arr = arr)

def nextInSeconds(time: float, next: staticmethod, text: str = '' ):
    print(text)
    for i in range(time):
        print("{}.".format(i))
        sleep(1)
    next()


def aulaPart1():
    valor_string = "Exemplo"
    print("> Aula Parte 1")
    print(f"{valor_string: <15}Alinhado a esquerda")
    print(f"{valor_string: >15} Alinhado a direita")
    print(f"{valor_string: ^15} Alinhado ao centro\n")

def aulaPart2():
    clear()
    sabor = "Chocolate"
    print("\n","> Aula Parte 2")
    total = 19.0
    string = f"{sabor: <15} {total:.2f}"
    print(string)


def aulaPart3():
    clear()
    print("\n","> Aula Parte 2")
    linhas = { 
        "Classica":9.90,
        "Premium":11.90,
        "Recheado":13.90
    }
    payment = ["Dinheiro", "Pix", "Outro"]
    discount = 2

    initialString = '''
{e}
Gerealdão desistiu de rivia e decidiu abrir uma loja de doces
Então seja bem vindo a FUCKIN LOJA DE DONUTS DO GERALDÂO!!!!
Nossos Donouts estão custando
{e}    
'''.format(e="."*50)
    print(initialString)

    calculator = []
    calculatorWithDiscount = []
    for index, element in enumerate(linhas):
        const = linhas[element]
        print("> Da linha: {}, que custa {} você vai querer quantos ?".format(element,const))
        inputUser = inputFloat("> ")
        value = const * inputUser 
        if inputUser%4 == 0 and value != 0 :
            print("AAAAA")
            calculatorWithDiscount.append(discount*inputUser)
        calculator.append(value)
    
    valueWithoutDiscount = sum(calculator)
    valueWithDiscount = sum(calculatorWithDiscount, valueWithoutDiscount)
    if valueWithDiscount >= 0:
        print("> Valor com desconto: {n}\n> Valor sem desconto: {n2}".format(n = valueWithoutDiscount,n2=valueWithDiscount))
        print("> Desconto valido apenas para pix ou dinheiro")
    else:
        print("> Seu pedido vai ao todo custar uns: {}".format(valueWithDiscount))
    
    print("> Escolha uma forma de pagameno!")
    sleep(1)
    choice = choiceAOptionInArray(payment)
    if choice != "Outro" or valueWithDiscount == 0:
        return print("> Você paga {}".format(valueWithoutDiscount))
    return print("> Você paga {}".format(valueWithDiscount))
if __name__ == "__main__":
    clear()
    aulaPart1()
    nextInSeconds(time=5, next=aulaPart2, text="Proxima parte")
    nextInSeconds(time=5, next=aulaPart3, text="Proxima parte")