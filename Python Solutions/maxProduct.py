# Maximum Product of Two Elements in an Array

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        import heapq
        if len(nums) == 2:
            return (nums[0] - 1) * (nums[1] - 1)

        max_vals = heapq.nlargest(2, nums)

        return (max_vals[0] - 1) * (max_vals[1] - 1)


if __name__ == '__main__':
    a = Solution().maxProduct([10, 2, 5, 2])
    print(a)
