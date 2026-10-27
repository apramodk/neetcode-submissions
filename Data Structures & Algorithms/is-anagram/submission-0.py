class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # immediately if len not same false
        if len(s) != len(t):
            return False

        setS = dict()
        setT = dict()
        for i in range(len(s)):
            if s[i] not in setS:
                setS[s[i]] = 1
            else:
                setS[s[i]] += 1
            if t[i] not in setT:
                setT[t[i]] = 1
            else:
                setT[t[i]] += 1
        
        return setT == setS