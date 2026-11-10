class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k

        # we should keep a min heap, so that we only pop the min vals,
        heapq.heapify(self.minHeap)
        # in case our maxHeap on init is larger than size k
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
        
    def add(self, val: int) -> int:
        if len(self.minHeap) < self.k:
            heapq.heappush(self.minHeap, val)
        else:
            heapq.heappushpop(self.minHeap, val)

        return self.minHeap[0]
