class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        def linearsearch(nums, n):
            for i in nums:
                if i == n:
                    return True
            return False
        longest = 1
        for i in range(len(nums)):
            x = nums[i]
            count = 1
            while linearsearch(nums, x+1):
                x = x + 1
                count = count + 1
            longest = max(count, longest)
        return longest
  #Time limit exceeded
  #67/80 test cases passed
