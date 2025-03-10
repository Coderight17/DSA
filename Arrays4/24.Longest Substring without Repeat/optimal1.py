class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: 
        n = len(s)
        if n == 0:
            return 0
        left = 0
        right = 0
        max7 = float('-inf')
        st = set()
        while right < n:
            if s[right] in st:
                while left < right and s[right] in st:
                    st.remove(s[left])
                    left = left+1
            st.add(s[right])
            if right-left+1 > max7:
                max7 = right-left+1
            right = right + 1
        return max7
#Runtime -> 16ms, beats 69.62%
#Memory 17.82 MB, beats 53.08%
