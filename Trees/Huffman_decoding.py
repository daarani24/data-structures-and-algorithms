class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def decodeHuff(root,s):
    res=[]
    cur=root
    for i in s:
        if i=='0':
            cur=cur.left
        else:
            cur=cur.right
        if cur.left is None and cur.right is None:
            res.append(cur.data)
            cur=root
    print(''.join(res))

def build_tree():
    root=Node(None)
    root.left=Node(None)
    root.right=Node('A')
    root.left.left=Node('B')
    root.left.right=Node("C")
    return root

root=build_tree()
s=input().strip()
decodeHuff(root,s)
