from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = []
        prev_space = 0

        for space in spaces:
            # We get the part of the word from prev_space until space
            ans.append(s[prev_space:space])
            # Update where current space is
            prev_space = space
        # Add the last part of the word
        ans.append(s[space:])
        # Join everything using " " seperator
        return " ".join(ans)
    
    def addSpaces_v2(self, s: str, spaces: List[int]) -> str:
        ans = s
		for i in range(len(spaces)-1, -1, -1):
			ans = ans[0:spaces[i]] + ' ' + ans[spaces[i]:]
		return ans
    

if __name__ == '__main__':
    a = Solution().maxProduct([10, 2, 5, 2])
    print(a)
