#Your task is to complete this function
 
class Solution:
    def maxLen(self, arr):
        # code here
        L  = 0
        n = len(arr)
        for i in range(n):
            sum7 = 0
            for j in range(i, n):
                sum7 = arr[j] + sum7
                if sum7 == 0:
                    length = j-i+1
                    if length > L:
                        L = length
        return L
#Time limit exceeded, 1010/1111 test cases passed
