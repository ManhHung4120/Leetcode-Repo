class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for i in range(0, len(columnTitle)):
            result += (ord(columnTitle[i]) - 64) * pow(26, len(columnTitle) - i - 1)
        return result
        
        