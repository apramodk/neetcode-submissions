class Solution:
    def isPalindrome(self, s: str) -> bool:
        # if a string is the same fwd and bwd then it is a isPalindrome
        # we can ignore non-alphanumeric characters including spaces
        
        # so what we can do is move two pointers from front and back, 
        # we will move both pointers inwards until they are crossed
        # we can have ignore the non-alphanumeric characters by doing 
        # an "isAlphaNumeric" check for the char at each pointer
        s = s.lower()
        l, r = 0, (len(s)-1)

        while(l < r):
            while(s[l].isalnum() == False and l < r):
                l += 1
            while(s[r].isalnum() == False and l < r):
                r -= 1

            if s[l] != s[r]:
                return False
            
            l += 1
            r -= 1

        return True