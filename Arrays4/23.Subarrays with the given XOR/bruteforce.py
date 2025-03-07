class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        count = 0
        s = set()
        for i in range(len(A)):
            for j in range(i, len(A)):
                xorr = 0
                for k in range(i, j+1):
                    xorr = xorr^A[k]
                if xorr == B:
                    count = count+1
        return count
#Time limit exceeded
