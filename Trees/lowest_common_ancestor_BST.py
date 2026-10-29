import json
from collections import deque

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

def build_tree(values):
    if not values or values[0] is None:
        return None
    root=TreeNode(values[0])
    q=deque([root])
    i=1
    while q and i<len(values):
        node=q.popleft()
        if i<len(values) and values[i] is not None:
            node.left=TreeNode(values[i])
            q.append(node.left)
        i+=1
        if i<len(values) and values[i] is not None:
            node.right=TreeNode(values[i])
            q.append(node.right)
        i+=1
    return root

def lowest_common_ancestor(root,p,q):
    while root:
        if p<root.val and q<root.val:
            root=root.left
        elif p>root.val and q>root.val:
            root=root.right
        else:
            return root.val
    return None

def main():
    values=json.loads(input())
    p=int(input())
    q=int(input())
    root=build_tree(values)
    res=lowest_common_ancestor(root,p,q)
    print(res)

if __name__=='__main__':
    main()
