import sys, time, threading, random, os, subprocess
t = 2
os.environ["t"] = str(t)

def counterTime():
    for i in range(t):
        time.sleep(1)
        print(f"> Faltam {i} secs...")


def createGame():
    try:
        subprocess.call("python game.py", timeout=t, creationflags=subprocess.CREATE_NEW_CONSOLE)
    except:
        print("")


def init():
    counterTimeTreading = threading.Thread(target=counterTime)
    GameTreading = threading.Thread(target=createGame)
    GameTreading.start()
    counterTimeTreading.start()

init()