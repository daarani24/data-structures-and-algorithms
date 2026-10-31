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

def middleNode(head):
    slow=head
    fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    return slow

def main():
    n=int(input())
    values=list(map(int,input().split()))
    head=build_list(values)
    mid=middleNode(head)
    print(mid.val if mid else None)

if __name__=='__main__':
    main()