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

def reverse_iteration(head):
    prev,cur=None,head
    while cur:
        nxt=cur.next
        cur.next=prev
        prev,cur=cur,nxt
    return prev

def main():
    n=int(input("Enter no.of nodes:"))
    if n<0:
        return
    if n==0:
        head=None
    else:
        values=list(map(int,input().split()))
        if len(values)!=n:
            return
        head=build_list(values)
    print(to_list(head))
    head=reverse_iteration(head)
    print(to_list(head))

if __name__ == '__main__':
    main()