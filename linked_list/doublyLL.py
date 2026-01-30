class Node:
    def __init__(self, value = None):
        self.data = value
        self.next = None
        self.prev = None

class DoublyLL:
    def __init__(self):
        self.head = None


    def insertatend(self,value):
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = node
        node.prev = temp

    def insertatbeg(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            return

        node.next = self.head
        self.head.prev = node
        self.head = node


    def printDLL(self):
        t1 = self.head
        while t1.next is not None:
            print(t1.data, end = " <--> ")
            t1 = t1.next
        print(t1.data)


obj = DoublyLL()
obj.insertatend(10)
obj.insertatend(20)
obj.insertatend(30)
obj.insertatbeg(50)
obj.insertatbeg(60)
obj.insertatbeg(70)
obj.printDLL()