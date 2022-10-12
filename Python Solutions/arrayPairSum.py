from typing import List


class Solution:

    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0

        for i in range(0, len(nums), 2):
            ans += min(nums[i], nums[i + 1])
        return ans


if __name__ == '__main__':
    a = Solution().arrayPairSum([1,4,3,2])
    print(a)

