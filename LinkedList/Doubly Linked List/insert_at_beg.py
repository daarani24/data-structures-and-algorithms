class Node:
    def __init__ (self,data):
        self.data=data
        self.next=None
        self.prev=None
class doubly:
    def __init__(self):
        self.head=None
def insert_at_beg(self,data):
    new=Node(data)
    if self.head is None:
        self.head=new
        return
    new.next=self.head
    self.head.prev=new
    self.head=new