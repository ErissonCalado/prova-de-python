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
