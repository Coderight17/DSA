class Solution:
    def sortColors(self, nums) -> None:
        zero = 0
        one = 0
        two = 0
        for i in nums:
            if i ==0:
                zero = zero + 1
            elif i == 1:
                one = one + 1
            elif i == 2:
                two = two+1
        for i in range(len(nums)):
            if i<zero:
                nums[i] = 0
            elif i< zero +one:
                nums[i] = 1
            else:
                nums[i] = 2

a = [2,0,2,1,1,0]
s = Solution()
s.sortColors(a)
print(a) 
