from ntpath import join
import time, random, os

class Console:
    def clear(self) -> None:
        os.system("cls" if os.name == "nt" else "clear")
    def inputNumber (self, txt: str) -> int:
        userInput = input(txt)
        try:
            return int(userInput)
        except:
            print("> digite apenas números.")
            return self.inputNumber(txt)

    def choiceInArray(self, ops: list) -> any:
        __ops__ = '\n'.join(f"[{i}]. {e}" for i,e in enumerate(ops))
        string = f"{__ops__} \nFaça sua escolha: "
        __userChoice__ = self.inputNumber(string)
        try:
            return ops[__userChoice__]
        except:
            print("> Escolha uma opção valida!")
            return self.choiceInArray(ops)

class Jokenpo: 
    def __init__(self) -> None:
        self.gameModes = ["Player vs Player", "Player vs I.A"]
        self.opsChoices = ["Pedra", "Papel", "Tesoura"]

    def start(self) -> None:
        choice = console.choiceInArray(self.ops)
        print(f"Okay, vamos prosseguir com: {choice}")
    def __game__ (self) -> None:
        pass
    def __verfy__(self) -> None:
        pass

if __name__ == "__main__":
    global console

    console = Console()
    jokenpo = Jokenpo()
    console.clear()

    initial = f'''
{f"-" * 100}
Super Games 3000, por favor selecione um jogo:  
{f"-" * 100} 
'''
    print(initial)
    jokenpo.start()