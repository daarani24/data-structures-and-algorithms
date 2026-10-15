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

class solution:
    def invert(self,root):
        if not root:
            return None
        root.left,root.right=root.right,root.left
        self.invert(root.left)
        self.invert(root.right)
        return root

def print_tree(root):
    if root is None:
        return 
    print(root.val,end=" ")
    print_tree(root.left)
    print_tree(root.right)

def main():
    values=json.loads(input())
    root=build_tree(values)

    sol=solution()
    root=sol.invert(root)
    
    print_tree(root)
    print()

if __name__ == '__main__':
    main()