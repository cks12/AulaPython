from mimetypes import init
import os, time

class verfy:
    def __init__(self, matriz, size) -> None:
        self.matriz = matriz
        self.size = size

    def __verfy__(self, arr: list):
        for i in range(len(arr)):
            __fristElement__ = arr[i][0]
            __tempArr__ = []
            for element in arr[i]:
                __tempArr__.append((__fristElement__ == element))
            listVerfy = sum(__tempArr__)
            print(listVerfy, len(arr[i]))
            if(listVerfy == len(self.matriz[i])):
                return True, __fristElement__
        return False, ""

    def verfy(self):
        colum = []
        line = []
        for lineIndex in range(self.size):
            __tempColum__ = []
            __tempLine__ = []
            for columIndex in range(self.size):
                __colum__ = self.matriz[columIndex][lineIndex]
                __line__ = self.matriz[lineIndex][columIndex]
                __tempLine__.append(__line__)
                __tempColum__.append(__colum__)
            colum.append(__tempColum__)
            line.append(__tempLine__)
            return self.__verfy__(__tempColum__) or self.verfy(__tempLine__)

class JogoDaVelha(verfy):
    def __init__(self, size):
        self.matriz = []
        self.turn = 0
        self.size = size
        super().__init__(self.matriz, self.size)
    def createGame(self):
        __letters__ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 
        for lines in range(self.size):
            letter = __letters__[lines]
            letter = letter.upper()
            temp = []
            for i in range(self.size):
                temp.append(f"{letter}{i}")
            self.matriz.append(temp)
    def clear(self):
        os.system("cls" if os.name=="nt" else "clear")

    def printGame(self):
        self.clear()
        print("Turno:",self.turn)
        for line in range(3):
            l = self.matriz[line]
            print(*l)

    def change(self, cord: str, element: str):
        line = 0
        for i,e in enumerate(self.matriz):
            if cord in e: 
                line = i 
        try: 
            col = self.matriz[line].index(cord)
            self.matriz[line][col] = element
            self.turn += 1
        except:
            print("> Por favor digite uma casa livre ou valida")
            time.sleep(2)
    
    def vitory(self):
        return self.verfy()

class Game(JogoDaVelha):
    def __init__(self, playes) -> None:
        self.playes = playes
        super().__init__(3)
        self.createGame()
    def start(self):
        while True:
            victory = self.vitory()
            if victory[0]:
                print("> O vencedor foi....")
                print(victory[1])
                break
            for player in self.playes:
                self.printGame()
                print(victory)
                user = input(f"> Digite uma casa para trocar por {player}: ")
                self.change(user, player)
                
if __name__ == "__main__":
    game = Game(["X","O"])
    game.start()
    print("> Jogo da velha iniciado !!!")