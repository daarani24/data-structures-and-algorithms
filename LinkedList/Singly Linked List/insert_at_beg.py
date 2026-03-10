class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singly:
    def __init__ (self):
        self.head=None
    def insert_at_beg(self,data):
        new_node=Node(data)
        self.new_node.next=self.head
        self.head=new_node
