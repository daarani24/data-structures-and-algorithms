class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=None

def build_list(values):
    dummy=tail=ListNode()
    for v in values:
        tail.next=ListNode(v)
        tail=tail.next
    return dummy.next

def build_cycle_list(values,pos):
    head=build_list(values)
    if pos<0 or not head:
        return head
    target=None
    tail=head
    i=0
    while tail.next:
        if i==pos:
            target=tail
        tail=tail.next
        i+=1
    if i==pos:
        target=tail
    if target is not None:
        tail.next=target
    return head

def is_cycle(head):
    slow=fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            return True
    return False

def main():
    n=int(input())
    if n<0:
        return
    if n==0:
        head=None
    else:
        values=list(map(int,input().split()))
        if len(values)!=n:
            return
        pos=int(input())
        if pos<-1 or pos>=n:
            return
        head=build_cycle_list(values,pos)
    res=is_cycle(head)
    print(res)

if __name__=='__main__':
    main()