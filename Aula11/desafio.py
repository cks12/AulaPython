from random import choice

def sort(peoples: list) -> list:
    wins = []

    for i in range(0,10):
        s = choice(peoples)
        peoples.remove(s)
        wins.append(s)
    wins.sort()
    return wins
def rank(peoples: list):
    p = peoples
    random.choice(p, weights)
def main():
    registro_clientes = ['Helena' , 'Miguel','Alice' , 'Arthur','Laura' , 'Heitor','Manuela' , 'Bernardo','Valentina' , 'Davi','Sophia' , 'Théo','Isabella' , 'Lorenzo','Heloísa' , 'Gabriel','Luiza' , 'Pedro','Júlia' , 'Benjamin','Lorena' , 'Matheus','Lívia' , 'Lucas','Maria Luiza' , 'Nicolas','Cecília' , 'Joaquim','Eloá' , 'Samuel','Giovanna' , 'Henrique','Maria Clara' , 'Rafael','Maria Eduarda' , 'Guilherme','Mariana' , 'Enzo','Lara' , 'Murilo','Beatriz' , 'Benício','Antonella' , 'Gustavo','Maria Júlia' , 'Isaac','Emanuelly' , 'João Miguel','Isadora' , 'Lucca','Ana Clara' , 'Enzo Gabriel','Melissa' , 'Pedro Henrique','Ana Luiza' , 'Felipe','Ana Júlia' , 'João Pedro','Esther' , 'Pietro','Lavínia' , 'Anthony','Maitê' , 'Daniel','Maria Cecília' , 'Bryan','Maria Alice' , 'Davi Lucca','Sarah' , 'Leonardo','Elisa' , 'Vicente','Liz' , 'Eduardo','Yasmin' , 'Gael','Isabelly' , 'Antônio','Alícia' , 'Vitor','Clara' , 'Noah','Isis' , 'Caio','Rebeca' , 'João','Rafaela' , 'Emanuel','Marina' , 'Cauã','Ana Laura' , 'João Lucas','Maria Helena' , 'Calebe','Agatha' , 'Enrico','Gabriela' , 'Vinícius','Catarina' , 'Bento']
    sas = sort(registro_clientes)
    string = f'''
Pessoas selecionas para participar do sorteio:
Pessoas: {' '.join(map(str, sas))}

'''
    print(string)

if __name__ == "__main__":
    main()