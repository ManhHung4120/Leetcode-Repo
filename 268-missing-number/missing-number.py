class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        count = 0
        for i in range(0,len(nums)):
            count += i - nums[i]
        return count + len(nums)

        