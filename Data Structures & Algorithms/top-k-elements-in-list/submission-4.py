class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = dict()
        # get count
        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1

        # init bucket
        bucket = [[] for _ in range(len(nums)+1)]
        for num, freq in freqMap.items():
            bucket[freq].append(num)

        ret = []
        for i in range(len(bucket)-1, 0, -1):
            ret.extend(bucket[i])
            if(len(ret) >= k):
                return ret[:k]
    
        return ret