'''[Questão criada por Izadora Oliveira (adaptada)] Lurdes tem um brechó e quer um programa que armazene todas as suas peças com seus respectivos preços, 
quantidade da peça e que ela possa excluir e incluir itens depois. Use uma lista ou lista composta para armazenar o nome do item, o preço e a quantidade. 
Faça um menu com opções de incluir e excluir os itens ( que forem vendidos).No final o programa deve mostrar os itens vendidos (excluídos), 
a lista com os itens cadastrados( apenas aqueles que não foram vendidos e o total vendido.  *'''


inicio = []
total = []
excluidos = []
final = []

resposta = "null"
while resposta != 'N':
    inicio.append(str(input('Qual peça você deseja adicionar?\n')))
    inicio.append(float(input('Quanto custa a peça?\n')))
    inicio.append(int(input('Quantas peças?\n')))
    total.append(inicio[:])
    inicio.clear()
    resposta = str(input('Deseja continuar?(S/N)\n'))
    resposta = resposta.upper()


opção = 3

while opção != 0:
    print('\n[0]Sair \n[1]Incluir \n[2]Excluir')
    opção = int(input())
    if opção == 1:
        inicio.append(str(input('Qual peça você deseja adicionar?\n')))
        inicio.append(float(input('Quanto custa a peça?\n')))
        inicio.append(int(input('Quantas peças?\n')))
        total.append(inicio[:])
        inicio.clear()

    if opção == 2:
        excluir = str(input('Qual peça deseja excluir?\n'))
        excluidos.append(excluir[:])


print('os itens vendidos foram:', excluidos)

print('o total de itens vendidos foi:', len(excluidos))
