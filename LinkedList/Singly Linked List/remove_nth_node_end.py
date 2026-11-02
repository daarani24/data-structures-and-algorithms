class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

def build_list(values):
    dummy=ListNode()
    tail=dummy
    for v in values:
        tail.next=ListNode(v)
        tail=tail.next
    return dummy.next

def to_list(head):
    res=[]
    while head:
        res.append(head.val)
        head=head.next
    return res

def removenode(head,n):
    dummy=ListNode(0)
    dummy.next=head
    slow=dummy
    fast=dummy
    for i in range(n+1):
        fast=fast.next
    while fast:
        slow=slow.next
        fast=fast.next
    slow.next=slow.next.next
    return dummy.next

def main():
    values=list(map(int,input().split()))
    n=int(input())
    head=build_list(values)
    res=removenode(head,n)
    print(to_list(res))

if __name__=='__main__':
    main()