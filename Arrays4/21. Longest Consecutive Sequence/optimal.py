class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        s = set(nums)
        longest = 1
        for i in s:
            if i-1 in s:
                continue
            else:
                x = i
                count = 1
                while x+1 in s:
                    count = count + 1
                    x = x+1
                longest = max(longest, count)
        return longest

#Passes all test cases
#Runtime -> 40ms, beats 92.24%
#Memory -> 34.26 MB, beats 53.57%
