class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        maxsum = nums[0]
        for item in nums:
            sum = sum + item
            if sum > maxsum:
                maxsum = sum
            if sum <0:
                sum = 0
        return maxsum
