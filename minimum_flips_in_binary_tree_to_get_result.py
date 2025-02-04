from functools import lru_cache
from typing import Optional


class Solution:
    def minimumFlips(self, root: Optional['TreeNode'], result: bool) -> int:
        @lru_cache(maxsize=None)
        def dfs(node: 'TreeNode', result: bool) -> int:
            if not node.left and not node.right:
                if bool(node.val) == result:
                    return 0
                else:
                    return 1

            if node.val == 2:
                # OR.
                left_F = dfs(node.left, False)
                right_F = dfs(node.right, False)
                if result:
                    left_T = dfs(node.left, True)
                    right_T = dfs(node.right, True)
                    return min(left_T + right_F, left_F + right_T, left_T + right_T)
                else:
                    return left_F + right_F
            elif node.val == 3:
                # AND.
                left_T = dfs(node.left, True)
                right_T = dfs(node.right, True)
                if result:
                    return left_T + right_T
                else:
                    left_F = dfs(node.left, False)
                    right_F = dfs(node.right, False)
                    return min(left_F, right_F)
            elif node.val == 4:
                # XOR.
                left_T = dfs(node.left, True)
                right_T = dfs(node.right, True)
                left_F = dfs(node.left, False)
                right_F = dfs(node.right, False)
                if result:
                    return min(left_T + right_F, left_F + right_T)
                else:
                    return min(left_F + right_F, left_T + right_T)
            else:
                # NOT.
                if node.left:
                    return dfs(node.left, not result)
                else:
                    return dfs(node.right, not result)

        return dfs(root, result)
