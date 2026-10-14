import json
from collections import deque

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def maxDepth(self,root):
        if root is None:
            return 0
        left_depth=self.maxDepth(root.left)
        right_depth=self.maxDepth(root.right)
        return 1+max(left_depth,right_depth)

def build_tree(values):
    if not values or values[0] is None:
        return None
    root=TreeNode(values[0])
    queue=deque([root])
    i=1
    while queue and i<len(values):
        cur=queue.popleft()
        if i<len(values):
            if values[i] is not None:
                cur.left=TreeNode(values[i])
                queue.append(cur.left)
            i+=1
        if i<len(values):
            if values[i] is not None:
                cur.right=TreeNode(values[i])
                queue.append(cur.right)
            i+=1
    return root

def main():
    values=json.loads(input())
    root=build_tree(values)

    solution=Solution()
    print(solution.maxDepth(root))

if __name__ == "__main__" :
    main() 