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

def merge_two_list(list1,list2):
    dummy=ListNode()
    tail=dummy
    while list1 and list2:
        if list1.val<list2.val:
            tail.next=list1
            list1=list1.next
        else:
            tail.next=list2
            list2=list2.next
        tail=tail.next

    if list1:
        tail.next=list1
    else:
        tail.next=list2
    return dummy.next

def print_list(head):
    values=[]
    while head:
        values.append(str(head.val))
        head=head.next
    print(" ".join(values))

def main():
    n=int(input())
    list1_values=list(map(int,input().split()))
    m=int(input())
    list2_values=list(map(int,input().split()))

    list1=build_list(list1_values)
    list2=build_list(list2_values)

    merge=merge_two_list(list1,list2)

    print_list(merge)

if __name__=='__main__':
    main()    
        