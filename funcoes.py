def saudar(nome):
    print(f'Olá, {nome}!')

saudar('Maria')

def somar(a, b):
    return a+b

soma=somar(2, 3)
print(soma)

def multiplicar(a, b):
    return a*b

multiplicacao=multiplicar(2, 3)
print(multiplicacao)

def saldacao(nome, saudacao='Olá'):
    print(f'{saudacao}, {nome}!')

saldacao('Jorge')

def testeGlobal():
    soma=0
    print(f'Soma dos valores: {soma}')

testeGlobal()