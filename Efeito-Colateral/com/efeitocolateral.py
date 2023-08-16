#Função COM efeito colateral 
def converte_1(lista):
    for i in range(len(lista)):
        lista[i] = int(lista[i])
#Função SEM efeito colateral 
def converte_2(lista):
    nova_lista = []
    for item in lista:
        nova_lista.append(int(item))
    return nova_lista
#Principal
numeros_1 = ['1', '2', '3', '4']
numeros_2 = ['1', '2', '3', '4']

converte_1(numeros_1)
numero_3 = converte_2(numeros_2)