from typing import List


class Solution:
    def fillCups(self, amount: List[int]) -> int:
        # On each iteration we fill the max and min seconds needed
        seconds = 0
        amount.sort()

        while amount[-1] > 0:
            amount[-1] -= 1
            amount[-2] -= 1
            seconds += 1
            amount.sort()
        return seconds


if __name__ == '__main__':
    a = Solution().fillCups([1, 4, 2])
    print(a)
