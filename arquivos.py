arquivo = open('exemplo.txt', 'r')

conteudo = arquivo.read()
print(conteudo)

open('exemplo.txt', 'w').write('Olá, mundo!')

with open('exemplo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

with open('exemplo.txt', 'w') as arquivo:
    arquivo.write('Adeus Python!')

arquivo.close()