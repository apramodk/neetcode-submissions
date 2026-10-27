class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # nums = [2,5,6,9]
        # target = 9
        # so for any given num in nums, we can chose to either add num or some other nums[i]

        res = []
        def dfs(nums, target, arr):
            nonlocal res
            if target == 0:
                # print("Target Hit!!")
                addRes(arr)
                # print(res)
                return
            if target < 0:
                return

            for i in range(len(nums)):
                num = nums[i]
                arr.append(num)
                # print(f"i={i}, target={target-num} arr={arr}")
                dfs(nums[i:], target-num, arr)
                arr.pop()
        
        def addRes(arr):
            res.append(arr.copy())

        dfs(nums, target, [])

        return res