class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mySet = set(nums)

        return len(nums) != len(mySet)