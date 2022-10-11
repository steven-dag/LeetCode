from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        curr_min_num = 1

        for num in nums:
            if curr_min_num == num:
                curr_min_num += 1
            elif nums[0] > 0:
                return curr_min_num
        return curr_min_num


if __name__ == '__main__':
    a = Solution().maxProduct([10, 2, 5, 2])
    print(a)
