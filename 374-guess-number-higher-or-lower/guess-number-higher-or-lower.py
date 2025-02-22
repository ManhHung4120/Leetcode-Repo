# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        if n == 2:
            return 1 if guess(1) == 0 else 2
        i, j = 1, n
        mid = (i + j) // 2
        while i < j:
            if guess(mid) == 0:
                return mid
            if guess(mid) == 1:
                i = mid + 1
            else:
                j = mid - 1
            mid = (i + j) // 2
        return mid

        