class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid), len(grid[0])
        counter = 0

        def dfs(row, col):
            direct = [[-1,0], [1,0], [0,-1], [0,1]]

            # do nothing if we're in an invalid index
            if row < 0 or row >= m or col < 0 or col >= n:
                return
            # do nothing if we're in a 0 element index
            if grid[row][col] == "0":
                return
            
            # swap 1 to 0
            grid[row][col] = "0"
            # try each cardinal direction
            for r,c in direct:
                dfs(row+r, col+c)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    counter += 1
                    dfs(i,j)
        
        return counter