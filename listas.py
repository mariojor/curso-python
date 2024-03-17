#Listas
numeros=[1,2,3,4,5]

print(numeros[4])

numeros.append(6)
print(numeros)

numeros.remove(3)
print(numeros)

#Tuplas
tupla=(1,2,3,3,3,3,3,34,5)
print(tupla.index(5))
print(tupla.count(3))

#Dicionários
pessoa={
    'nome':'Jorge', 
    'idade':20
    }

print(pessoa.values())
print(pessoa.keys())
print(pessoa['nome'])
print(pessoa.get('idade'))
print(pessoa.get('peso', 'Não encontrado'))

for chave, valor in pessoa.items():
    print(chave, valor)

#Conjuntos
    
frutas={'maçã', 'banana', 'uva', 'laranja', 'maçã'}
outrasFrutas={'coco', 'abacaxi', 'uva'}
print(frutas)

frutas.add('morango')
print(frutas)

frutas.remove('maçã')
print(frutas)

if 'coco' in frutas:
    print('Uva encontrada')
else:
    print('Coco não encontrada')

print(f'union {frutas.union(outrasFrutas)}')
print(f'intersection {frutas.intersection(outrasFrutas)}')
