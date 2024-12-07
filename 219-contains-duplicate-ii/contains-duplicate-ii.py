class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        check = {}
        for index, val in enumerate(nums):
            if check.get(val):
                for i in check[val]:
                    if abs(i - index) <= k:
                        return True
                check[val].append(index)
            else:
                check[val] = [index]           
        return False
        