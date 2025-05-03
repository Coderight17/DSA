class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        i = 0
        start = 0
        end = 0
        words = []
        while i <len(s):
            end = s.find(' ',start)
            if end == -1:
                words.append(s[start:])
                break
            else:
                words.append(s[start:end])
            j = end
            while s[j] == ' ':
                j = j + 1
            start = j
        return ' '.join(reversed(words))
# Accepted
# 61 / 61 testcases passed
#   Runtime
# 4
# ms
# Beats
# 17.75%
# Analyze Complexity
# Memory
# 17.99
# MB
# Beats
# 43.76%
