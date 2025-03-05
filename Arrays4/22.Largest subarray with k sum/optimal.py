#Your task is to complete this function
 
class Solution:
    def maxLen(self, arr):
        # code here
        maxi = 0
        freq = {}
        n = len(arr)
        sum = 0
        for i in  range(n):
            sum = sum + arr[i]
            if sum == 0:
                maxi = i + 1
            else:
                if sum in freq:
                    maxi = max(maxi, i-freq[sum])
                else:
                    freq[sum] = i
        return maxi
#Time taken : 0.65 ms
#1111/111 test cases passed
