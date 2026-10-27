class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets = dict()

        for s in strs:
            sortedStr = ''.join(sorted(s))

            if sortedStr in buckets:
                buckets[sortedStr].append(s)
                continue
            
            buckets[sortedStr] = [s]

        ret = []
        for key,val in buckets.items():
            ret.append(val)

        return ret
