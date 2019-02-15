#!/usr/bin/env

lista = [1,2, '3' ,( 'uno', 'dos' ,3)]

print(type(lista))

print(lista)

print(lista[0])

print(lista[3][-1])

lista.append('nuevo')

print (lista)

for item in lista:
    print (item)
    if type (item) == tuple:
        for item2 in item 
            print(item2)


