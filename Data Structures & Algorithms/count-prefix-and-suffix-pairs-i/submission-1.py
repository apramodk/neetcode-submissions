class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        
        for i in range(len(words)-1):
            for j in range(i+1,len(words)):
                    count += self.isPrefixAndSuffix(words[i], words[j])

        return count

    def isPrefixAndSuffix(self, str1: str, str2: str) -> bool:
        cmpLen = len(str1)
        sufStart = len(str2) - cmpLen

        # prefix compare
        if str2[0:cmpLen] != str1:
            return False
        
        # suffix compare
        if str2[sufStart::] != str1:
            return False
        
        return True
