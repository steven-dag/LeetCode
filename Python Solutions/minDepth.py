from typing import List, Optional


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:  return 0
        leftDepth = self.minDepth(root.left)
        rightDepth = self.minDepth(root.right)
        if root.left is None and root.right is None:
            return 1
        if root.left is None:
            return 1 + rightDepth
        if root.right is None:
            return 1 + leftDepth
        return min(leftDepth, rightDepth) + 1

if __name__ == '__main__':

    leet = Solution()

    leet.minDepth([3,9,20,null,null,15,7])
