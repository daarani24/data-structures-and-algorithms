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

def same_tree(p,q):
    if p is None and q is None:
        return True
    if p is None or q is None or p.val!=q.val:
        return False
    return same_tree(p.left,q.left) and same_tree(p.right,q.right)

def subtree(root,subroot):
    if subroot is None:
        return True
    if root is None:
        return False
    if same_tree(root,subroot):
        return True
    return subtree(root.left,subroot) or subtree(root.right,subroot)

def main():
    tree1=json.loads(input())
    tree2=json.loads(input())

    root=build_tree(tree1)
    subroot=build_tree(tree2)

    print(subtree(root,subroot))

if __name__ == "__main__" :
    main() 