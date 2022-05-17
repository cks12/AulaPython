import os 

class Console:
    def inputNumber(self,txt: str) -> float: 
        t = input(txt)
        try:
            return float(t)
        except: 
            print("> Por favor digite um número")
            return self.inputNumber(txt)

    def inputInArr(self, arr: list, **kwargs) -> any:
        i = input(f"\n> Digite uma opção {arr}: \n> ")
        i = i.lower()
        try:
            kwargs["err"]
            try:
                return arr[arr.index(i)],0
            except:
                return None, 1
        except:
            try:
                return arr[arr.index(i)],0
            except:
                print(f"> Opção não reconhecida")
                return self.inputInArr(arr), 1
        return None, 1 
    
    def clear(self):
        os.system("cls" if os.name=="nt" else "clear")
    
    def choiceExecInArray(self, arr: list) -> any:

        print("\n> Escolha uma opção a baixo: ")
        for i,e in enumerate(arr):
            string = "[{n}]. {e}".format(n = i, e = e["name"])
            print(string)
        userChoice = self.inputNumber("> Digite o número da opção: ")
        try:
            userChoice = int(userChoice)
            return arr[userChoice]
        except:
            return self.choiceInArray(arr)
    
    def Exit(self):
        exit(0)

class Calculator (Console):
    def __init__(self):
        super().__init__()
        
    def calc(self, x:float,y:float, op:str) -> float:
        try:
            if op == "+":
                return x + y
            if op == "-":
                return x - y
            if op == "/":
                return x / y
            if op == "*":
                return x * y
        except :
            print("> Deu erro na conta !!!")

    def calculadora (self):
        operators = ["+","-","*","/"]
        x, op, y = self.inputNumber("> Digite o primeiro numero: "), self.inputInArr(operators)[0], self.inputNumber("> Digite o segundo numero: ")
        result = self.calc(x, y, op)
        print(f"> O resultado de {x} {op} {y} é {result}")

def Departamento ():
    errs = 0
    while errs <= 2:
        ops = ["compras","vendas"]
        userInput = console.inputInArr(ops, err=True)
        if userInput[1] != 0:
            errs += userInput[1]
            print(f"> Você tem {errs} erros")
        
        if userInput[0] == "compras":
            print("> compras...")
            break
        
        if userInput[0] == "vendas":
            print("> vendas...")
            break

def listAll():
    functions = [
            {
                "name":"Calculadora",
                "function":Calculator().calculadora
            },
            {
                "name":"Departamento",
                "function":Departamento
            },
            {
                "name":"Listar todos os comandos",
                "function": listAll
            },
            {
                "name":"Sair",
                "function":Console().Exit
            },
        ]
    executer = console.choiceExecInArray(functions)
    executer["function"]()

if __name__ == "__main__":
    global console
    console = Console()
    console.clear()
    
    while True:
        listAll()