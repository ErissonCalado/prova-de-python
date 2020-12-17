signos = ['Macaco', 'Galo', 'Cão', 'Porco', 'Rato', 'Boi', 'Tigre', 'coelho',
          'Dragão', 'Serpente', 'Cavalo', 'Carneiro']


def resposta():
    print(f'O seu signo do Zodíaco Chinês é {signos}.')


def linhas():
    print('-'*50)
    print('*'*50)


def oposto():
    print('*'*50)
    print('-'*50)


ano = int(input('Digite seu ano de nascimento: '))
signos = signos[ano % 12]

linhas()
resposta()
oposto()
