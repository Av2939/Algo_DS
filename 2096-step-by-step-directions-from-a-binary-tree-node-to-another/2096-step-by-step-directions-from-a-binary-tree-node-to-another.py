# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        graph = defaultdict(list)
        queue = collections.deque([root])
        
        while queue:
            node = queue.popleft()
            
            if node.left:
                graph[node.left.val].append((node.val, 'U'))
                graph[node.val].append((node.left.val, 'L'))
                
                queue.append(node.left)
                
            if node.right:
                graph[node.right.val].append((node.val, 'U'))
                graph[node.val].append((node.right.val, 'R'))
                
                queue.append(node.right)
                
        
        seen = set()
        queue = collections.deque([(startValue, "")])
        
        while queue:
            cur_val, cur_path = queue.popleft()
            
            if cur_val in seen:
                continue
            
            seen.add(cur_val)
            
            if cur_val == destValue:
                return cur_path
            
            else:
                
                for child, direction in graph[cur_val]:
                    if child not in seen:
                        queue.append((child, cur_path + direction))