lista=[]
def suma(lista):
    a=sum(lista)
    return a
def resta(lista):
    resta = 0
    for i in range (len(lista)):
        resta = resta - lista[i]
    return resta
def promedio(lista):
    p = sum(lista)/len(lista)
    return p
def mayor(lista):
    mayor = 0
    if lista[0]>=lista[1]:
        if lista [0]>=lista[2]:
            mayor = lista[0]
        else:
            mayor = lista[2]
    elif lista[1]>=lista[2]:
        mayor = lista[1]
    else:
        mayor = lista[2]
    return (mayor)
def multiplicacion(lista):
    m = 1
    for i in range (len(lista)):
        m = m*lista[i]
    return (m)

for i in range(3):
    a=int(input())
    lista.append(a)
s = suma(lista)
r = resta(lista)
p = promedio(lista)
ma = mayor(lista)
mu = multiplicacion(lista)
print ("suma: ", s, " resta: ", r, " promedio: ", p, " mayor: ", ma, " multplicacion: ", mu)
input()
