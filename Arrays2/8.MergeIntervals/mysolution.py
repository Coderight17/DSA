class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n = len(intervals)
        i = 0
        while i< n:
            if i+1 <n :
                if intervals[i][1] >= intervals[i+1][0]:
                        intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
                        del intervals[i+1]
                        n = n-1
                else:
                    i = i+1
            else:
                break
        return intervals
