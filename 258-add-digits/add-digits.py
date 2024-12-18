class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            count = 0
            for i in str(num):
                count += int(i)
            num = count
        return num
        