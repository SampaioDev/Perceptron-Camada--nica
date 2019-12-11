import random

pesos = [
    1,
    1,
    1,
]

vies = 1
coeficiente = 0.3
dataSet = [
    [0, 0, -1],
    [0, 1, -1],
    [1, 0, -1],
    [1, 1, 1],
]

def validarPesos(i):
    somatorio = pesos[0]*dataSet[i][0] + pesos[1]*dataSet[i][1] + pesos[2] * vies
    if(somatorio >= 0):
        saida = 1
    else:
        saida = -1
    return saida

def recalcularPesos(p, erro):
    dr = coeficiente * erro
    for y in range (3):
        if y == 2:
            pesos[y] = pesos[y] + ( dr * vies)
        else:
            pesos[y] = pesos[y] + ( dr * dataSet[p][y])    

def perceptron(indice):
    saida = validarPesos(indice)
    if(saida != dataSet[indice][2]):
        recalcularPesos(indice, (dataSet[indice][2] - saida))
        perceptron(indice)
    else:
        if(indice > 0):
            perceptron(indice -1)
    # print('saida: ', saida)
    # print('saida esperada: ', dataSet[p][2])
    # print('######################')

if __name__ == "__main__":
    print('Pesos Iniciais: ', pesos)
    print('######################')
    for p in range(len(dataSet)):
        if p == 0:
            print('Primeira Linha:')
        if p == 1:
            print('Segunda Linha:')
        if p == 2:
            print('Terceira Linha:')
        if p == 3:
            print('Quarta Linha:')
        print('x1: ', dataSet[p][0])
        print('x2: ', dataSet[p][1])
        print('Saída Esperada: ', dataSet[p][2])
        print('######################')
        perceptron(p)
    print('Pesos Finais:', pesos)