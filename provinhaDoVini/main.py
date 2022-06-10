global var_1
global var_2
global var_3
global var_4
global var3_max
global var4_min
global var_9
var_1 = []
var_2 = []
var_3 = []
var_4 = []

def Q1(entrada: str) -> None:
    entradaArr = entrada.split()
    for i in range(0,len(entradaArr),4):
        temp = entradaArr[i:i+4]
        var_1.append(temp[0])
        var_2.append(temp[1])
        var_3.append(float(temp[2]))
        var_4.append(int(temp[3]))

def Q2(var_1, var_2, var_3, var_4):
    global var3_max
    global var4_min
    var3_max = max(var_3)
    var4_min = min(var_4)



def Q3(var_1,var_2,var_3,var_4):
    var_9 = []
    for index in range(0,len(var_4)):
        imc = 0
        imc = var_4[index] / (var_3[index]**2)
        if imc < 18.5:
            tempStr = "magro"
        elif imc > 25:
            tempStr = "sobrepeso"
        else:
            tempStr = "normal"
        var_9.append(tempStr)

entrada_prova="João Dor_Garganta 1.2 67 Vitor Febre 1.25 51 Arthur Dor_Cabeca 1.18 79 Marina Febre 1.51 71 Catarina Tosse 1.37 44 Vinícius Tosse 0.94 33 Samuel Nauseas 1.43 80 Leonardo Colica 1.05 37 Isabella Febre 1.49 43 Yasmin Tosse 0.76 41 Gabriel Colica 1.51 57 Enrico Tosse 1.22 30 Maria_Clara Febre 1.24 20 Bryan Nauseas 0.56 60 Beatriz Nauseas 1.44 29 Guilherme Dor_Garganta 0.8 80 Heitor Dor_Cabeca 0.74 71 Liz Colica 1.48 16 Esther Colica 0.73 55 Rafael Tosse 0.72 66 Maria_Luiza Nauseas 0.54 39 Lara Colica 0.86 32 Mariana Dor_Garganta 0.88 72 Lavínia Tosse 0.83 61 Ana_Luiza Dor_Cabeca 1.08 75 Emanuelly Colica 0.58 55 Théo Tosse 0.78 45 Maria_Cecília Dor_Cabeca 1.28 20 Isabelly Colica 1.56 70 Lorenzo Dor_Garganta 0.72 80 Felipe Tosse 0.74 69 Antonella Nauseas 1.52 15 Davi Nauseas 0.61 52 Lorena Dor_Cabeca 1.43 30 Joaquim Colica 1.07 26 Vicente Tosse 1.5899999999999999 32 Cecília Nauseas 1.41 70 Clara Nauseas 1.16 51 Giovanna Nauseas 0.84 80 Rafaela Nauseas 0.97 56 Henrique Tosse 1.26 29 Maria_Helena Tosse 0.7 23 Miguel Colica 0.87 54 Pedro_Henrique Febre 0.62 46 Enzo_Gabriel Nauseas 0.52 42 Ana_Laura Febre 0.66 22 Daniel Dor_Cabeca 0.54 33 Lucca Febre 1.3 65 Melissa Nauseas 1.48 14 Benício Nauseas 1.3900000000000001 32 Alice Nauseas 1.16 34 Calebe Dor_Cabeca 1.46 49 Eduardo Tosse 1.41 13 Emanuel Nauseas 1.32 45 João_Pedro Nauseas 1.24 47 Eloá Dor_Cabeca 0.72 80 Isis Dor_Cabeca 1.22 79 Sophia Dor_Cabeca 0.61 47 Bernardo Nauseas 0.94 76 Gael Dor_Cabeca 1.5899999999999999 74 Anthony Dor_Cabeca 1.09 14 Bento Dor_Garganta 0.7 31 Alícia Nauseas 0.58 63 Noah Colica 0.91 72 Matheus Febre 0.81 18 Benjamin Dor_Garganta 0.79 64 "
# var_1=['João', 'Vitor', 'Arthur', 'Marina', 'Catarina', 'Vinícius', 'Samuel', 'Leonardo', 'Isabella', 'Yasmin', 'Gabriel', 'Enrico', 'Maria_Clara', 'Bryan', 'Beatriz', 'Guilherme', 'Heitor', 'Liz', 'Esther', 'Rafael', 'Maria_Luiza', 'Lara', 'Mariana', 'Lavínia', 'Ana_Luiza', 'Emanuelly', 'Théo', 'Maria_Cecília', 'Isabelly', 'Lorenzo', 'Felipe', 'Antonella', 'Davi', 'Lorena', 'Joaquim', 'Vicente', 'Cecília', 'Clara', 'Giovanna', 'Rafaela', 'Henrique', 'Maria_Helena', 'Miguel', 'Pedro_Henrique', 'Enzo_Gabriel', 'Ana_Laura', 'Daniel', 'Lucca', 'Melissa', 'Benício', 'Alice', 'Calebe', 'Eduardo', 'Emanuel', 'João_Pedro', 'Eloá', 'Isis', 'Sophia', 'Bernardo', 'Gael', 'Anthony', 'Bento', 'Alícia', 'Noah', 'Matheus', 'Benjamin']
# var_2=['Dor_Garganta', 'Febre', 'Dor_Cabeca', 'Febre', 'Tosse', 'Tosse', 'Nauseas', 'Colica', 'Febre', 'Tosse', 'Colica', 'Tosse', 'Febre', 'Nauseas', 'Nauseas', 'Dor_Garganta', 'Dor_Cabeca', 'Colica', 'Colica', 'Tosse', 'Nauseas', 'Colica', 'Dor_Garganta', 'Tosse', 'Dor_Cabeca', 'Colica', 'Tosse', 'Dor_Cabeca', 'Colica', 'Dor_Garganta', 'Tosse', 'Nauseas', 'Nauseas', 'Dor_Cabeca', 'Colica', 'Tosse', 'Nauseas', 'Nauseas', 'Nauseas', 'Nauseas', 'Tosse', 'Tosse', 'Colica', 'Febre', 'Nauseas', 'Febre', 'Dor_Cabeca', 'Febre', 'Nauseas', 'Nauseas', 'Nauseas', 'Dor_Cabeca', 'Tosse', 'Nauseas', 'Nauseas', 'Dor_Cabeca', 'Dor_Cabeca', 'Dor_Cabeca', 'Nauseas', 'Dor_Cabeca', 'Dor_Cabeca', 'Dor_Garganta', 'Nauseas', 'Colica', 'Febre', 'Dor_Garganta']
# var_3=[1.2, 1.25, 1.18, 1.51, 1.37, 0.94, 1.43, 1.05, 1.49, 0.76, 1.51, 1.22, 1.24, 0.56, 1.44, 0.8, 0.74, 1.48, 0.73, 0.72, 0.54, 0.86, 0.88, 0.83, 1.08, 0.58, 0.78, 1.28, 1.56, 0.72, 0.74, 1.52, 0.61, 1.43, 1.07, 1.59, 1.41, 1.16, 0.84, 0.97, 1.26, 0.7, 0.87, 0.62, 0.52, 0.66, 0.54, 1.3, 1.48, 1.39, 1.16, 1.46, 1.41, 1.32, 1.24, 0.72, 1.22, 0.61, 0.94, 1.59, 1.09, 0.7, 0.58, 0.91, 0.81, 0.79]
# var_4=[67, 51, 79, 71, 44, 33, 80, 37, 43, 41, 57, 30, 20, 60, 29, 80, 71, 16, 55, 66, 39, 32, 72, 61, 75, 55, 45, 20, 70, 80, 69, 15, 52, 30, 26, 32, 70, 51, 80, 56, 29, 23, 54, 46, 42, 22, 33, 65, 14, 32, 34, 49, 13, 45, 47, 80, 79, 47, 76, 74, 14, 31, 63, 72, 18, 64]

Q1(entrada_prova)
Q2(var_1,var_2,var_3,var_4)
Q3(var_1,var_2,var_3,var_4)
print(var3_max)