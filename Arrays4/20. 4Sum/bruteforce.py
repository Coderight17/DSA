class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        st = set()
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2 ):
                for k in range(j+1, len(nums)-1):
                    for l in range(k+1, len(nums)):
                        sum = nums[i] + nums[j]
                        sum = sum + nums[k]
                        sum = sum + nums[l]
                        if sum == target:
                            temp = [nums[i], nums[j], nums[k], nums[l]]
                            temp.sort()
                            st.add(tuple(temp))
        final_array = [list(x) for x in st]      
        return final_array
#Time limit exceeded -> 282/294 test cases passed
