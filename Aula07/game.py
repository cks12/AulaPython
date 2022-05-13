import sys, time, threading, random, os
t = int(os.getenv('t'))

def Game():
    space = "*"*100
    string = f'''
{space}

{f"Bem vindo a porra desse jogo dos infernos!!!":>70}

{space}'''
    print(string)
    n = random.randrange(0,10)
    sys.stdout.write(f"> O pc gerou um numero de 0 a 10, qual é o número ? \n Vc tem {t} segundos pra acertar!!! \n")
    userInput = readline()
    print("> Vc perdeu!" if userInput != n else print("> Vc ganhou"))
    readline()


def readline():
    userInput = sys.stdin.readline(30)
    return userInput

Game()