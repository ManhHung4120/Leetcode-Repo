class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        count = 0
        sort_nums = sorted(nums)
        if sort_nums[0]:
            return 0
        for i in sort_nums[1:len(sort_nums)]:
            if count + 1 != i:
                return count + 1
            count = i
        return count + 1

        