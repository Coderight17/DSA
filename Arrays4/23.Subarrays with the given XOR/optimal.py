class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        count = 0
        m = {}
        m[0] = 1
        n = len(A)
        X = 0
        for i in range(n):
            X = X^A[i]
            x = X^B
            if x in m:
                count = count + m[x]
            if X in m:
                m[X] = m[X] + 1
            else:
                m[X] = 1
        return count
