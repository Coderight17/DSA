class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] > 2*nums[j]:
                    count = count + 1
        return count
# Time limit exceeded(32/140 test cases passed)
