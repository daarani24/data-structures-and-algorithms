def countNode (head):
    if head is None:
        return head
    t=head
    c=0
    while t:
        t=t.next
        c+=1
    print(c)