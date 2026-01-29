class Node:
    def __init__(self, info, nxt=None):
        self.data = info

        self.nxt = nxt

class SinglyLL:
    def __init__(self, head=None):
        self.head = head

    def insertatend(self, value):
        temp = Node(value)
        if self.head is not None:
            t1 = self.head
            while t1.nxt is not None:
                  t1 = t1.nxt
            t1.nxt = temp
        else:
            self.head = temp

    def insertatbegining(self, value):

        temp = Node(value)

        temp.nxt = self.head

        self.head = temp

    def insertatmiddle(self, value, x):
        temp = Node(value)

        t1 = self.head

        while t1.nxt is not None:
            if t1.data == x:
                temp.nxt = t1.nxt
                t1.nxt = temp
            t1 = t1.nxt

    def deleteLL(self, value):
        if self.head is None:
            return

        # If head needs to be deleted
        if self.head.data == value:
            self.head = self.head.nxt
            return

        prev = self.head
        curr = self.head.nxt

        while curr is not None:
            if curr.data == value:
                prev.nxt = curr.nxt
                return
            prev = curr
            curr = curr.nxt

    def printLL(self):
        t1 = self.head
        while t1.nxt is not None:
            print(t1.data)
            t1 = t1.nxt
        print(t1.data)




obj = SinglyLL()
obj.insertatend(10)
obj.insertatend(30)
obj.insertatend(20)
obj.insertatbegining(50)
obj.insertatmiddle(40,10)
obj.deleteLL(50)
obj.printLL()