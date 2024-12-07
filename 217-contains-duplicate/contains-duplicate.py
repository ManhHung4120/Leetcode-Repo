class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        remove_dupe = set(nums)
        return len(nums) != len(remove_dupe)
        