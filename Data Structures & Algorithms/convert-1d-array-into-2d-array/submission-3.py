class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m*n:
            return []

        ret,tmp = [], []
        for i,v in enumerate(original):
            tmp.append(v)
            if len(tmp) == n:
                ret.append(tmp)
                tmp = []

        return ret