class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # so given a list of unique numbers, we want to get each unique combination set, including the empty set
        # we are guaranteed that nums will be atleast len 1, so this would mean our return must be at least [[], [nums[n-1]]]

        # so for each new index we wanna, add to every previous list
        res = []
        subset =[]

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res
        