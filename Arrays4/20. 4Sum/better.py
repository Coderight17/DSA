class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        s = set()
        for i in range(n):
            for j in range(i+1, n):
                hs = set()
                for k in range(j+1, n):
                    sum7 = nums[i] + nums[j] + nums[k]
                    fourth = target - sum7
                    if fourth in hs:
                        temp = [nums[i], nums[j], nums[k], fourth] 
                        temp.sort()
                        s.add(tuple(temp))
                    hs.add(nums[k])
        solution = [list(temp) for temp in s]
        return solution
#All test cases accepted
#Time complexity -> beats 5.66%(1002ms)
#Space complexity -> beats 58.04%(17.88MB)
