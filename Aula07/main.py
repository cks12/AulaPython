inputNum = int(input())

def loop_par(num):
    counter = 1
    numList = []
    numCounter = num
    if numCounter % 2 != 0:
        numCounter += 1
        counter = 0
    counter_loop = counter + 5
    while counter < counter_loop:
        numList.append(numCounter + 2 * counter)
        counter += 1
    return numList

iterator = 0
while iterator < inputNum:
    print(f"lista dos pares do número {iterator}: {loop_par(iterator)}")
    iterator += 1
       
