class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        index = 0
        summary_range_list = []
        temp = nums[0]
        n = nums[0]
        for i in range(0, len(nums)):
            if i - index != nums[i] - nums[index]:
                if i - index == 1:
                    summary_range_list.append(str(n))
                else:
                    summary_range_list.append(f"{temp}->{n}")
                temp = nums[i]
                index = i
            n = nums[i]
        if temp == nums[len(nums) - 1]:
            summary_range_list.append(str(n))
        else:
            summary_range_list.append(f"{temp}->{n}")
        return summary_range_list

        