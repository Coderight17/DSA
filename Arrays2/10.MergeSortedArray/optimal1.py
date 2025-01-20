class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m-1
        j = 0
        while i>=0 and j<n:
            if nums1[i] > nums2[j]:
                nums1[i], nums2[j] = nums2[j], nums1[i]
                i = i-1
                j = j+1
            else:
                break
        nums1[0:m] = sorted(nums1[0:m])
        nums2[0:n] = sorted(nums2[0:n])
        j= 0
        for i in range(m, m+n):
            nums1[i] = nums2[j]
            j = j+1  
