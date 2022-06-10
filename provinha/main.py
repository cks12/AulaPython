def Q1(arr: list) -> list:
    # [0] nome do comprador (str)
    # [1] bairro do imóvel (str)
    # [2] metragem (float)
    # [3] preço de venda int (int)
    arrTuples = []
    for element in arr:
        try:
            element[2] = float(element[2])
            element[3] = float(element[3])
        except:
            print("Erro na conversão dos numeros")
        temp = tuple(element)
        arrTuples.append(temp)
    return arrTuples


def Q2(arr: list) -> list:
    def _keySort_(e):
        return e[0]
    temp = arr.copy()
    temp.sort(key=_keySort_)
    return temp

def Q3 (arr: list) -> list:
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
    return newList
if __name__ == "__main__":
    global var_9
    global var_4
    global var_5
    entrada_prova=[['Agatha', 'Liberdade', 167.91, 1365276], ['Murilo', 'Se', 133.28, 1242436], ['Laura', 'Bela_Vista', 104.26, 1560042], ['Isis', 'Bom_Retiro', 82.53, 1231595], ['Isabelly', 'Bela_Vista', 96.68, 1636405], ['Esther', 'Republica', 194.59, 3081332], ['Lorena', 'Bela_Vista', 147.31, 2419714], ['Eloá', 'Republica', 67.02, 903027], ['Melissa', 'Bela_Vista', 112.38, 957028], ['Alícia', 'Bela_Vista', 24.19, 194656], ['Gustavo', 'Bela_Vista', 130.55, 2024177], ['Maria_Clara', 'Bom_Retiro', 81.58, 680621], ['Helena', 'Liberdade', 48.8, 503469], ['Beatriz', 'Bom_Retiro', 175.64, 2298776], ['Gael', 'Consolacao', 81.2, 1022957], ['Mariana', 'Liberdade', 32.84, 580479], ['Júlia', 'Bom_Retiro', 53.19, 792796], ['Isabella', 'Liberdade', 179.24, 1624631], ['Pedro_Henrique', 'Liberdade', 62.83, 516902], ['Guilherme', 'Se', 144.74, 2284141], ['Luiza', 'Bela_Vista', 50.08, 861776], ['Clara', 'Se', 77.96, 629527], ['Bryan', 'Republica', 45.36, 639258], ['Maria_Luiza', 'Se', 60.67, 976180], ['Noah', 'Republica', 83.26, 1254145], ['Benício', 'Consolacao', 145.52, 2239698], ['Rebeca', 'Bela_Vista', 191.96, 2314653], ['Ana_Luiza', 'Se', 152.2, 2414044], ['Joaquim', 'Bom_Retiro', 113.6, 1496680], ['Enzo', 'Se', 75.03, 691401], ['Felipe', 'Republica', 99.43, 1106357], ['João_Pedro', 'Se', 92.67, 1576409], ['Matheus', 'Consolacao', 32.16, 447602], ['Maitê', 'Liberdade', 121.22, 1264445], ['Enzo_Gabriel', 'Se', 171.28, 3034396], ['Lucca', 'Liberdade', 103.26, 1568312], ['Maria_Helena', 'Bela_Vista', 197.45, 2348865], ['Sarah', 'Bela_Vista', 52.05, 685706], ['Heitor', 'Se', 23.18, 309105], ['Maria_Alice', 'Se', 80.19, 1214878], ['Bento', 'Republica', 69.56, 755630], ['Lavínia', 'Republica', 186.77, 2301193], ['Rafael', 'Consolacao', 64.51, 809794], ['Arthur', 'Consolacao', 146.35, 2194079], ['Lorenzo', 'Se', 172.46, 2018644], ['Catarina', 'Liberdade', 190.81, 3248731]]

    var_4 = Q1(entrada_prova)
    var_5 = Q2(var_4)
    # var_9 = Q3(var_4)
    # var_7 = ' '.join(s for s in var_9)
    
    print("01).",var_4[17])
    print("02).",var_4[27])
    # print("03).",var_5[0])
    # print("04).",var_5[len(var_5)-1])
    # print("05).",var_7.count("avaliar"))
    # var_5 = Q2(var_4)
    # print(var_5[0])
    # var_9 = Q3(var_4)
    var_1=None
    var_2=None
    var_3=None
    # var_4=[('Agatha', 'Liberdade', 167.91, 1365276), ('Murilo', 'Se', 133.28, 1242436), ('Laura', 'Bela_Vista', 104.26, 1560042), ('Isis', 'Bom_Retiro', 82.53, 1231595), ('Isabelly', 'Bela_Vista', 96.68, 1636405), ('Esther', 'Republica', 194.59, 3081332), ('Lorena', 'Bela_Vista', 147.31, 2419714), ('Eloá', 'Republica', 67.02, 903027), ('Melissa', 'Bela_Vista', 112.38, 957028), ('Alícia', 'Bela_Vista', 24.19, 194656), ('Gustavo', 'Bela_Vista', 130.55, 2024177), ('Maria_Clara', 'Bom_Retiro', 81.58, 680621), ('Helena', 'Liberdade', 48.8, 503469), ('Beatriz', 'Bom_Retiro', 175.64, 2298776), ('Gael', 'Consolacao', 81.2, 1022957), ('Mariana', 'Liberdade', 32.84, 580479), ('Júlia', 'Bom_Retiro', 53.19, 792796), ('Isabella', 'Liberdade', 179.24, 1624631), ('Pedro_Henrique', 'Liberdade', 62.83, 516902), ('Guilherme', 'Se', 144.74, 2284141), ('Luiza', 'Bela_Vista', 50.08, 861776), ('Clara', 'Se', 77.96, 629527), ('Bryan', 'Republica', 45.36, 639258), ('Maria_Luiza', 'Se', 60.67, 976180), ('Noah', 'Republica', 83.26, 1254145), ('Benício', 'Consolacao', 145.52, 2239698), ('Rebeca', 'Bela_Vista', 191.96, 2314653), ('Ana_Luiza', 'Se', 152.2, 2414044), ('Joaquim', 'Bom_Retiro', 113.6, 1496680), ('Enzo', 'Se', 75.03, 691401), ('Felipe', 'Republica', 99.43, 1106357), ('João_Pedro', 'Se', 92.67, 1576409), ('Matheus', 'Consolacao', 32.16, 447602), ('Maitê', 'Liberdade', 121.22, 1264445), ('Enzo_Gabriel', 'Se', 171.28, 3034396), ('Lucca', 'Liberdade', 103.26, 1568312), ('Maria_Helena', 'Bela_Vista', 197.45, 2348865), ('Sarah', 'Bela_Vista', 52.05, 685706), ('Heitor', 'Se', 23.18, 309105), ('Maria_Alice', 'Se', 80.19, 1214878), ('Bento', 'Republica', 69.56, 755630), ('Lavínia', 'Republica', 186.77, 2301193), ('Rafael', 'Consolacao', 64.51, 809794), ('Arthur', 'Consolacao', 146.35, 2194079), ('Lorenzo', 'Se', 172.46, 2018644), ('Catarina', 'Liberdade', 190.81, 3248731)]
    # print(var_4[17])
    # if Q1(entrada_prova) == var_4:
    #     print("var_4 e Q1, são iguais")
    pass