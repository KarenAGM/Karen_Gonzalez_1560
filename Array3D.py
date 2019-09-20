"""

class Array3D:
    def __init__(self,rows,cols,depht):
        self.__rows=rows
        self.__cols=cols
        self.__depht=depht
        self.__data=[]
        for i in range(self.__depht):
            aux=[]
            for j in range(self.__rows):
                aux2=[]
                for k in range(self.__cols):
                    aux2.append(None)
                aux.append(aux2)
                self.__data.append(aux)

    def to_String(self):
        print(self.__data)

    def get_num_rows(self):
         return(self.__rows)

    def get_num_cols(self):
        retunr(self.__cols)

    def get_num_depht(self):
        retunr(self.__depht)
"""

array=[0 for x in range(5)]
print(array)
array=[x for x in range(5)]
print(array)
array=[(x+1)*10 for x in range(5)]
print(array)
array=[x for x in range(10,60,10)]
print(array)
Array2D=[[0 for x in range(4)]for x in range(3)]
print(Array2D)
Array3D=[[[0 for x in range(4)]for x in range(3)]for x in range (5)]
print(Array3D)

print("---Grid---")
for ren in Array2D:
    print(ren)
print("______________")
tab=' '
cont=1
for grid in Array3D:
    print(f"{tab*int(cont-1)}Capa {cont-1}")
    for ren in grid:
        print(f"{tab*int(cont-1)} {ren}")
    print("")
    cont+=1

