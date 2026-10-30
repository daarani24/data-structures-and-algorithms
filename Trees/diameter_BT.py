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

def diameter(root):
    d=0
    def height(node):
        nonlocal d
        if node is None:
            return 0
        left_h=height(node.left)
        right_h=height(node.right)
        d=max(d,left_h+right_h)
        return 1+max(left_h,right_h)
    height(root)
    return d

def main():
    values=json.loads(input())
    root=build_tree(values)
    print(diameter(root))

if __name__=='__main__':
    main()