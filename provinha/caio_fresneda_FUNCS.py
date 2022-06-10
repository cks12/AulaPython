def Q1(arr: list) -> list:
    global var_4
    arrTuples = []
    for element in arr:
        try:
            element[2] = float(element[2])
            element[3] = float(element[3])
        except:
            print("Erro na conversão dos numeros")
        temp = tuple(element)
        arrTuples.append(temp)
    var_4 = arrTuples
    return arrTuples


def Q2(arr: list) -> list:
    global var_5
    def _keySort_(e):
        return e[0]
    temp = arr.copy()
    temp.sort(key=_keySort_)
    var_5 = temp
    return temp

def Q3 (arr: list) -> list:
    global var_9
    newList = []
    for element in arr:
        price, size = element[3], element[2]
        m2Price = price / size
        if m2Price <= 10000:
            tempString = "compra no ato"
        elif m2Price > 14000:
            tempString = "não compra"
        else:
            tempString = "avaliar"
        newList.append(tempString)
    var_9 = newList
    return newList