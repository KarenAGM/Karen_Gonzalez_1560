def burbuja(data):
    for tope in range(len(data)-1,0,-1):
        for index in range(0,tope,1):
            if data[index]>data[index +1 ]:
                data[index],data[index+1]=data[index + 1],data[index]
        print(data)
    return data

def main():
    print(burbuja([8,5,9,6,3]))
    print(burbuja([899,22,43,556,23,42,3,78,1,23,0,21,88,77]))
"""   
    lista=[8,5,9,3]
    min=0
    for index in range(len(lista)):
        if lista[index]<lista[min]:
            min=index
    print(f"El valor minimo es:{lista[min]} en la posicion {min}")
    min=lista[0]
    for d in lista:
        if d < min:
            min=d
    print(f"El minimo {d}")
"""

main()

"""
Es una mejora al metodo burbuja, consiste en iterar una solavez sobre el arreglo,colocar un pivote
buscar el elemento mas pequeño adelante del pivote e intercambiarlo por el pivote
"""
def seleccion(data):
    for pivote in range(len(data)-1):
        min=pivote
        for index in range(pivote,len(data),1):
            if data[index]>data[min]:
                pass
            else:
                min=index
        data[min],data[pivote]=data[pivote],data[min]
        print(data)
    return data

def main():
    print(seleccion([8,5,9,3,6]))

main()


