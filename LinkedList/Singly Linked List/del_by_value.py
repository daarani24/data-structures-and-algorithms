def del_by_val(head,val):
    if head is None:
        return head
    if head.data==val:
        head=head.next
        return
    t=head
    while t.next and t.next.data!=val:
        t=t.next
    if t.next is None:
        print("value is not found")
    else:
        t.next=t.next.next