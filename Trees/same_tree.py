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
    def same_tree(self,p,q):
        if not p and not q:
            return True
        if not p or not q or p.val!=q.val:
            return False
        return self.same_tree(p.left,q.left) and self.same_tree(p.right,q.right)

def main():
    p_values=json.loads(input())
    q_values=json.loads(input())
    
    p=build_tree(p_values)
    q=build_tree(q_values)

    sol=solution()
    print(sol.same_tree(p,q))

if __name__ == "__main__" :
    main() 

