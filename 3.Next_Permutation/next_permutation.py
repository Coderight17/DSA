class Solution:
    def nextPermutation(self, nums) -> None:
        maxind = -1
        for i in range(len(nums)-2, -1, -1):
            if nums[i]<nums[i+1]:
                maxind = i
                break
        if maxind == -1:
            nums.reverse()
        else:
            for i in range(len(nums)-1, maxind, -1):
                if nums[maxind]< nums[i]:
                    nums[maxind], nums[i] = nums[i], nums[maxind]
                    break
            nums[maxind+1:] = reversed(nums[maxind+1:])
a = [2, 3, 1]
s = Solution()
s.nextPermutation(a)
print(a)
