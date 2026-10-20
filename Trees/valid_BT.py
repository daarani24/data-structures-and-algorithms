from collections import deque

class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def build_tree(values):
    if not values or values[0] is None:
        return None
    root=TreeNode(values[0])
    q=deque([root])
    i=1
    while q and i<len(values):
        cur=q.popleft()
        if i<len(values) and values[i] is not None:
            cur.left=TreeNode(values[i])
            q.append(cur.left)
        i+=1
        if i<len(values) and values[i] is not None:
            cur.right=TreeNode(values[i])
            q.append(cur.right)
        i+=1
    return root

def is_valid(root,low=float('-inf'),high=float('inf')):
    if root is None:
        return True
    if not low<root.val<high:
        return False
    return is_valid(root.left,low,root.val) and is_valid(root.right,root.val,high)

values=list(map(int,input().split()))

root=build_tree(values)

res=is_valid(root)

print(res)