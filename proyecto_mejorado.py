from functools import reduce
import operator

lista=[]
def suma(lista):
    return sum(lista)

def resta(lista):
    return 0 - suma(lista)

def resta2(lista):
    return reduce(operator.__sub__, lista)

def promedio(lista):
    return sum(lista)/len(lista)
  
def mayor(lista):
    return sorted(lista, reverse=True)[0]

def multiplicacion(lista):
    m = 1
    for i in lista:
        m = m*i
    return (m)

def display(lista):
  for i in lista:
    print(i, end = " ")
  print("\n")
  return

length = int(input())
for i in range(length):
    a=int(input())
    lista.append(a)

s = suma(lista)
r = resta(lista)
p = promedio(lista)
ma = mayor(lista)
mu = multiplicacion(lista)
display(lista)


print ("suma: ", s, " \nresta: ", r, " \npromedio: ", p, " \nmayor: ", ma, " \nmultplicacion: ", mu, " \nresta desde el primero: ", resta2(lista))
input("\n\npress enter key to exit")
