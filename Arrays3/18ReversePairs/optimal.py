# i = low
# j = mid+1
# count = 0
# while i <= mid and j <= high:
#   if nums[i] > 2*nums[j]:
#       count = count+mid-i+1
#       i = i+1
#   else:
#       j = j+1
#   return count -> Why does this not work?
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def getcount(nums, low, mid, high):
            i = low
            j = mid+1
            count = 0
            for i in range(low, mid+1):
                while j <= high and nums[i] > 2*nums[j]:
                    j = j+1
                count = count+j-mid-1
            return count
        def merge(nums, low, mid, high):
            i = low
            j = mid+1
            t = []
            while i <= mid and j <=high:
                if nums[i] > nums[j]:
                    t.append(nums[j])
                    j = j+1
                else:
                    t.append(nums[i])
                    i = i+1
            while i <= mid:
                t.append(nums[i])
                i = i+1
            while j <= high:
                t.append(nums[j])
                j = j+1
            for i in range(low, high+1):
                nums[i] = t[i-low]
        def mergesort(nums, low, high):
            count = 0
            if low < high:
                mid = (low+high)//2
                count = count + mergesort(nums, low, mid)
                count = count + mergesort(nums, mid+1, high)
                count = count + getcount(nums, low, mid, high)
                merge(nums, low, mid, high)
            return count
        return mergesort(nums, 0, len(nums)-1)
