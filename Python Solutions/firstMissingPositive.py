from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        curr_min_num = 1

        for num in nums:
            if curr_min_num == num:
                # This means that curr_min_num already exists in num, so it cant be the smallest
                # missing positive number
                # ex. num = [1, 2, 0] -> sorted: [0, 1, 2]
                # At the first number we'll have curr_min_num = 1 == num
                # At the third loop we'll end up at curr_min_num = 2 == num
                # Which when we exit the loop we'll have curr_min_num = 3 which is the answer
                curr_min_num += 1
            elif nums[0] > 0:
                return curr_min_num
        return curr_min_num


if __name__ == '__main__':
    a = Solution().maxProduct([10, 2, 5, 2])
    print(a)