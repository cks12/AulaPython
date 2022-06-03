import os
class JogoDaVelha:
    def __init__(self, size):
        self.matriz = []
        self.turn = 0
        self.size = size

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
    
    def vitory(self):
        v = False
        col = self.matriz[0][0]
        for line in range(self.size):
            if self.matriz[line][0] == self.matriz[line][1] and self.matriz[line][0] == self.matriz[line][2]:
                return not v
            for coluns in range(self.size):
                if(self.matriz[line][coluns] != col):
                    break
                coluns
        return v

if __name__ == "__main__":
    print("> Jogo da velha iniciado !!!")
    JogoDaVelha = JogoDaVelha(3)
    JogoDaVelha.createGame()
    JogoDaVelha.printGame()
    while True:
        if JogoDaVelha.vitory():
            print("Parabén, vc venceu!")
            break
        user1 = input("> Digite uma casa para trocar por X: ")
        JogoDaVelha.change(user1, "X")
        JogoDaVelha.printGame()
        user2 = input("> Digite uma casa para trocar por O: ")
        JogoDaVelha.change(user2, "O")
        JogoDaVelha.printGame()