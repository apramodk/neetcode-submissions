class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rlen, clen = len(grid), len(grid[0])
        mArea = 0

        def dfs(r,c):
            direct = [[-1,0], [1,0], [0,-1], [0,1]]
            # check for out of bounds
            if r < 0 or r >= rlen or c < 0 or c >= clen:
                return 0

            # do nothing if 0
            if grid[r][c] == 0:
                return 0

            # since we've visited this grid space set to 0
            grid[r][c] = 0
            cArea = 1

            # go each cardinal direction
            for x, y in direct:
                cArea += dfs(r+x, c+y)

            return cArea


        for r in range(rlen):
            for c in range(clen):
                val = grid[r][c]

                if val == 1:
                    mArea = max(dfs(r,c), mArea)

        return mArea