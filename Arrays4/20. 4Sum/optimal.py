class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        solution = []
        for i in range(n):
            if i >= 1 and nums[i-1] == nums[i]:
                continue
            for j in range(i+1, n):
                if j > i + 1 and nums[j-1] == nums[j]:
                    continue
                k = j + 1
                l = n-1
                while k < l:
                    sum = nums[i] + nums[j] + nums[k] + nums[l]
                    if sum == target:
                        temp = [nums[i], nums[j], nums[k], nums[l]]
                        solution.append(temp)
                        k = k + 1
                        l = l -1
                        while k <l and nums[k] == nums[k-1]:
                            k = k + 1
                        while k < l and l < n -1 and nums[l] == nums[l +1]:
                            l =  l -1
                    elif sum < target:
                        k = k + 1
                    else:
                        l = l -1
        return solution
#All test cases accepted
#Runtime 437 ms, beats 29.42%
#Memory 17.91 MB, beats 39.28%
