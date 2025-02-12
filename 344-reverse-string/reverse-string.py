class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n, m = 0, len(s) - 1
        while n < m:
            s[n], s[m] = s[m], s[n]
            n += 1
            m -= 1
        