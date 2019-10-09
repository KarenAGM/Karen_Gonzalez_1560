class Stack:
      def __init__(self):
            self.__data=[]
      def length(self):
            return len(self.__data)
      def is_empty(self):
            return self.length()==0
      def peek(self):
            return self.__data[self.length()-1]
      def pop(self):
            return self.__data.pop()
      def push(self,value):
            self.__data.append(value)
      def to_String(self):
            for e in self.__data:
                  print(f"|{e}|", end="")

def main():
      pila=Stack()
      pila.push(14)
      pila.push(1)
      pila.push(2)
      pila.push(5)
      pila.to_String()
      print(pila.pop())

main()

def quita_medio(pila):
      aux=Stack()
      mid=pila.length()

      for elem in range(0,mid,1):
            aux.push(pila.pop())
      pila.poo()

      for elem in range(0,mid-1,1):
            lista.push(aux.pop())
      return pila  
