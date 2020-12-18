'''[Questão criada por Nicolas Mathias (adaptada)] Cinco amigos saíram para jantar fora e nessa noite ficou definido que seria feito um sorteio para quem iria pagar a conta.
 Para isso faça um dicionário com os nomes dos amigos, faça um sorteio dentre esses para ver quem vai pagar a conta. Além disso, 
 seu programa deve pegar o valor da conta que pode ser adiciono os 10% do garçom. *'''



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
