class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singly:
    def insert_at_end(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            return self.head
        t=self.head
        while t.next:
            t=t.next
        t.next=newnode
        return head


