class Solution:
    def climbStairs(self, n: int) -> int:
        # so we have an integer n, which represents a target value
        # starting from some value x, we can either add 1 or 2, 
        # we want to keep track of all distinct ways of getting from x to n
        one, two = 1,1

        for i in range(n-1):
            tmp = one
            one = one + two
            two = tmp
        
        return one
            