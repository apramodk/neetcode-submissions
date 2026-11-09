class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        pq = []
        dist = {i:-1 for i in range(n)}
        adj = self.adjList(n, edges)
        dist[src] = 0
        heapq.heappush(pq, (0, src))

        while pq:
            # prio the lowest weight paths
            pDist, pNode = heapq.heappop(pq)

            # check if locked node (no point in processing)
            if pDist > dist[pNode] and dist[pNode] != -1:
                continue
            
            # otherwise process adjacencies in list
            for (cNode, cDist) in adj[pNode]:
                if dist[cNode] > pDist + cDist or dist[cNode] == -1:
                    dist[cNode] = pDist + cDist
                    heapq.heappush(pq, (dist[cNode], cNode))

        return dist

    def adjList(self, n,edges):
        adjList = [[] for _ in range(n)]

        for src, dst, weight in edges:
            adjList[src].append((dst, weight))
        
        return adjList



#####################################################
        # given n verticies, a list of edges, and a source node
        # we want to find the shortest path from the start vertex to all other verticies

        # our return should be a dictionary where the key is the node, and the value is the distance from the source to the node

        # 2 <= n <= 100

        # lets start by creating an adjacency list,
        """
        {
            0: (1,10), (2,3)
            1: (3,2)
            2: (1,4), (3,8), (4, 2)
            3: (4,5)
            4: 
        }
        """

        # then we will have a dictionary where each node keeps track of its distance from src
        """
        {
            0: 0
            1: 10 -> 7
            2: 3
            3: 12 -> 11
            4: 5
        }
        """

        # now we can start from source, and traverse through each path 
        """
            src = 0
            src -> src = 0

            now we can choose to go to its children:
                0-> 1 = 10 (so 10 is our current fastest path)
                0-> 2 = 3 (3 is our fastest path to 2)

            now we process the neighbors of 0
            1,2

            1 can get to 3 in 2 steps, 
            since the shortest path to 1 as of now is 10, the shortest known path to 3 will now be 12

            2 can get to 1 in 7 steps from src, 7 is less than 1, so we should update 1 to be 7
            2 can get to 3 in 11 steps from src, so we should update 3
            2 can get to 4 in 5 steps from src, so set 4 to 5

            so now we have a way to get to 3,4 and a new way to get to 1
        """

        # so maybe what we want to do is keep a priority queue, and remove a value from the queue once we find an optimal path to it
                
