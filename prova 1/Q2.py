'''[Questão criada por Nicolas Mathias (adaptada)] Cinco amigos saíram para jantar fora e nessa noite ficou definido que seria feito um sorteio para quem iria pagar a conta.
 Para isso faça um dicionário com os nomes dos amigos,faça um sorteio dentre esses para ver quem vai pagar a conta. Além disso, 
 seu programa deve pegar o valor da conta que pode ser adiciono os 10% do garçom.'''


import random
amigos = {}

valor = float(input('Qual o valor da conta?'))
porcent = valor * 10 / 100
preço = valor + porcent

for i in range(0, 5):
    amigos[i] = str(input('Informe seu nome: '))
sorteio = random.choice(list(amigos.values()))
print(f'o sorteado a pagar a conta foi: ', sorteio)
print(f'o valor a ser pago com os 10% é:', preço)
