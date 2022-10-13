from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from itertools import chain
        d = {}
        rev_d = {}
        for i in range(len(arr)):
            if arr[i] in d:
                d[(arr[i])] = d[(arr[i])] + 1
            else:
                d[(arr[i])] = 1
        for key, value in d.items():
            rev_d.setdefault(value, set()).add(key)
        result = set(chain.from_iterable(values for key, values in rev_d.items() if len(values) > 1))
        if not result:
            return True
        else:
            return False


if __name__ == '__main__':
    a = Solution().uniqueOccurrences([1, 2, 2, 1, 1, 3])
    print(a)
