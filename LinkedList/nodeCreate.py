class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

def build_list(values):
    dummy=tail=ListNode()
    for v in values:
        tail.next=ListNode(v)
        tail=tail.next
    return dummy.next

def to_list(head):
    out=[]
    while head:
        out.append(head.val)
        head=head.next
    return out