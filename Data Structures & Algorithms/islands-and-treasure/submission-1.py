class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # m x n grid
        # - each element is -1, 0, INF. 
        # -1 is impassable
        # 0 is a target
        # INF is passable

        # we want to modify each element in a grid such that, any INF spot, shows the distance from a given target to another spot

        # I understand the problem, as we basically want each land space to represent how close is the nearest treasure chest.

        # based on ex 2, i can see that if a given land block cannot reach a chest, then we should leave it as INF,
        # 1. traverse through the 2d matrix

        # 2. on discovery of a treasure chest, we could bfs traverse through all adjacent blocks
            # on bfs, our base case is q empty - because of the constraint of inplace change for grid, im assuming we want to optimize for space here
            # if a given element already has a non-INF number, we should only change if our current distance is less than the existing val
            # in this approach, we guarantee that we are only traversing all unvisited vals

        # we want the current vector space, (we'll call bfs when we hit a 0 block)
        m,n = len(grid), len(grid[0])

        def bfs(x,y):
            nonlocal grid
            direct = [[-1,0], [1,0], [0,-1], [0,1]]
            q = deque([(x,y)])

            while q:
                cx,cy = q.popleft()
                dist = grid[cx][cy]

                for dx,dy in direct:
                    nx, ny = cx+dx, cy+dy
                    if nx < m and nx >= 0 and ny < n and ny >= 0:
                        # if the new space contains a val greater than the dist we're trying to check
                        if grid[nx][ny] > dist+1:
                            q.append((nx,ny))
                            grid[nx][ny] = dist+1

        visit = []
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    visit.append((r,c))

        for r,c in visit:
            bfs(r,c)
