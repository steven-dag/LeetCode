from typing import List

class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:

        longest_time = logs[0][1]
        time = 0
        ans = logs[0][0]

        for i in range(len(logs)):
            task_time = abs(time - logs[i][1])

            if (task_time > longest_time) or (task_time == longest_time and ans > logs[i][0]):
                longest_time = task_time
                ans = logs[i][0]
            time = logs[i][1]
        return ans
      
if __name__ == '__main__':
    a = Solution().hardestWorker(10,[[0,3],[2,5],[0,9],[1,15]])
    print(a)
