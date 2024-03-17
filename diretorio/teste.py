import __init__
import datetime
import os

print(__init__.soma(1, 2))
print(__init__.subtracao(1, 2))
print(__init__.multiplicacao(1, 2))
print(__init__.divisao(1, 2))

print(datetime.datetime.now())
print(datetime.datetime.now().year)
print(datetime.datetime.now().month)
print(datetime.datetime.now().day)
print(datetime.datetime.now().hour)
print(datetime.datetime.now().minute)
print(datetime.datetime.now().second)
print(datetime.datetime.now().microsecond)
print(datetime.datetime.now().isoformat())
print(datetime.datetime.now().ctime())

print(os.getcwd())
print(os.listdir())

