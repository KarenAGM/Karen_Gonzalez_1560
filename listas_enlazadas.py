class Nodo:
    def __init__(self,value,siguiente = None):
        self.data = value
        self.next = siguiente


class Linked_List:
    def __init__(self):
        self.head = None

    def is_empty( self ):
        return self.head == None

    def get_tail ( self ):
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
        return cur_node

    def append( self, value):
        if self.is_empty():
            self.head = Nodo(value)
        else:
            self.get_tail().next = Nodo (value)

    def transversal ( self ) :
        cur_node = self.head
        while cur_node.next != None:
            print(cur_node.data, " --> ", end ="")
            cur_node = cur_node.next
        print(cur_node.data)

    def prepend( self, value ):
        self.head = Nodo (value, self.head)

    def add_before(self,reference_value,value):
        aux=self.head
        while aux.next.data != reference_value:
            aux=aux.next
        nuevo=Nodo(value,aux.next)
        aux.next=nuevo

    def add_after(self,reference_value,value):
        aux = self.head
        while aux.data != reference_value:
            aux = aux.next
        nuevo = Nodo(value,aux.next)
        aux.next = nuevo

    def remove(self,value):
        if(value==self.head.data):
            self.head=self.head.next
        else:
            aux = self.head
            while aux.next.data != value:
                aux = aux.next
            if aux.next.next==None:
               aux.next=None

            else:
                aux.next=aux.next.next

    def pop(self):
        cur_node = self.head
        while cur_node.next.next != None:
            cur_node = cur_node.next
        aux= cur_node.next
        cur_node.next = None
        return aux.data



def main():
    lista=Linked_List()
    lista.append(3)
    lista.append(5)
    lista.transversal()
    lista.add_before(5,4)
    lista.transversal()
    lista.add_before(4,3.5)
    lista.transversal()
    lista.add_after(4,4.5)
    lista.transversal()
    lista.remove(4)
    lista.transversal()
    lista.remove(3)
    lista.transversal()
    lista.remove(5)
    lista.transversal()
    print(lista.pop())
    lista.transversal()
main()