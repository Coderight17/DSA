class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: 
        n = len(s)
        if n == 0:
            return 0
        max7 = -1
        for i in range(n):
            map7 = {}
            for j in range(i, n):
                if s[j] in map7:
                    break
                map7[s[j]] = 1 
            max7 = max(max7, len(map7))
        return max7
#All test cases passed
#Runtime 252ms, beats 7.79%
#Memory 17.89 MB, beats 53.10%
