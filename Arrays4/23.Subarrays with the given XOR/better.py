class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        count = 0
        for i in range(len(A)):
            xorr = 0
            for j in range(i, len(A)):
                xorr = xorr^A[j]
                if xorr == B:
                    count = count + 1
        return count
