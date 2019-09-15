class Array:
    def __init__(self, size):
        self.__size = size
        self.__data = []
        for index in range(size):
            self.__data.append(index)
        
    def length( self ):
        return self.__size
        print(self.__size)
        
    def get_item(self,index):
        if index >= 0 and index < self.__size:
            return self.__data[index]
        else:
            return None # Index no valido

    def set_item (self, index, valor):
        if index >= 0 and index < self.__size:
            self.__data[index] = valor
        else:
            print("index fuera de rango")

    def clearing( self, valor ):
        
        for index in range(self.__size):
            self.__data[index] = valor

    def to_string(self):
        print(self.__data)
            
def main():
    a = Array(10)
    a.to_string()
    print(f"El tamaño del arreglo es: {a.length()}")
    a.set_item(2,10)
    a.to_string()
    print(f"El elemento 4 es: {a.get_item(14)}")
    a.clearing(0)
    a.to_string()
    
main()
