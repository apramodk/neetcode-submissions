class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(choices, cache, target):
            if target == 0:
                res.append(cache.copy())
                return

            for i, c in enumerate(choices):
                if c > target:
                    break
                if i > 0 and c == choices[i - 1]:
                    continue
                cache.append(c)
                backtrack(choices[i+1:], cache, target - c)
                cache.pop()

        backtrack(candidates, [], target)
        return res