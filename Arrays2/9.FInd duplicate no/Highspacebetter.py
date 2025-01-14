class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        frequency = {}
        for i in nums:
            if i in frequency:
                frequency[i] = frequency[i] + 1
                return i
            else:
                frequency[i] = 1
