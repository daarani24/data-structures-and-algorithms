import heapq

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

def merge_k_heap(lists):
    heap=[]
    for i,head in enumerate(lists):
        if head:
            heapq.heappush(heap,(head.val,i,head))
    dummy=tail=ListNode()
    while heap:
        _,i,node=heapq.heappop(heap)
        tail.next=node
        tail=node
        if node.next:
            heapq.heappush(heap,(node.next.val,i,node.next))

    tail.next=None
    return dummy.next

def run_merge():
    k=int(input())
    lists=[]
    for i in range(k):
        values=list(map(int,input(f"Enter sorted elements of list{i+1}:").split()))
        lists.append(build_list(values))

    res=merge_k_heap(lists)
    print(to_list(res))

if __name__=='__main__':
    run_merge()