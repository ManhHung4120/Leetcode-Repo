class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        first, last = 0, len(nums) - 1
        if len(nums) > 1:
            while first <= last:
                while nums[first] == 0:
                    nums.pop(first)
                    nums.append(0)
                    last -= 1
                    if last == 0:
                        break
                first += 1

        """
        Do not return anything, modify nums in-place instead.
        """
        