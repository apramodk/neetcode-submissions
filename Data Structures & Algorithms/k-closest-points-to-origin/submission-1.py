class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # we are just returning the k closest poitns to the origin

        # the distance between 2 points is defined as sqrt((x1-x2)^2 + (y1-y2)^2)
        # so we basically wanna maintain a maxHeap, such that once our maxHeap is of size k, we pop the max euclidean distance if the point we're trying to add in is smaller
        def dist(x,y):
            return (x**2 + y**2)**0.5

        maxHeap = []
        for x,y in points:
            cDist = -dist(x,y)
            # if maxHeap currently has less than k just add
            if len(maxHeap) < k:
                heapq.heappush(maxHeap, (cDist, [x,y]))
                continue
            
            # if cDist is closer than the furthest we should pushpop, else do nothing
            if cDist > maxHeap[0][0]:
                heapq.heappushpop(maxHeap, (cDist, [x,y]))

        return [point for _,point in maxHeap]