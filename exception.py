
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Exception ZeroDivisionError: ", e)

try:
    list=[1,2,3,4,5]
    print(list[10])
except IndexError as e:
    print("Exception IndexError: ", e)

x = -1
if x < 0:
    raise Exception("Sorry, no numbers below zero")

try:
    arquivo = open('exemplo1.txt', 'r')
    conteudo = arquivo.read()
except FileNotFoundError as e:
    print("Exception FileNotFoundError: ", e)
except IndexError:
    print("Erro desconhecido")
except:
    print("Erro desconhecido")
else:
    print(conteudo)
finally:
    arquivo.close()