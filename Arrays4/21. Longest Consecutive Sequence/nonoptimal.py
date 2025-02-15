#This is the code that I tried myself, I have first sorted this array, and then counted the longest consecutive sequence. It takes O(nlogn) time complexity while it should only take O(n). It beats 96.98% in time
#complexity and 96.33 % in space complexity
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) == 1:
            return 1
        C = 0
        count = 1
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] == 1:
                count = count +1
            elif nums[i] == nums[i-1]:
                count = count
            else:
                count = 1
            if count > C:
                    C = count
        return C
