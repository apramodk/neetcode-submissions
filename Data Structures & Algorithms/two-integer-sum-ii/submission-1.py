class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # given a target value and a list of numbers in sorted order.
        # where n represents each value in numbers, such that -1000 <= n <= 1000
        # and the target is withing the same bounds

        # we are guaranteed to have a valid solution
        l,r = 0, (len(numbers)-1)

        while(True):
            # ok now we need to figure out the rules for incrementing and decrementing
            # if numbers[l] + numbers[r] < target (increment l)
            # opposite decrement r
            # if target return l and r
            cur = numbers[l] + numbers[r]
            
            if(cur < target):
                l += 1
            elif(cur > target):
                r -= 1
            else:
                return [l+1, r+1]
        
        return []