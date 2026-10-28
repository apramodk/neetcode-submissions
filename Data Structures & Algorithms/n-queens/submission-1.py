class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # once we place a queen in a given row, no other queen can be in that row
        # we wanna place a queen on every other col, such that it wont be in an occupied diagonal, or an occupied column

        # so given an index on a 2d grid, (x,y) any value that is diagonal of (x,y) => (x + i, y + i)
        # lets say we have idx_0 = (x_0, y_0), and idx_1 = (x_1, y_1), how do we check if idx_1 is on a diagonal space of idx_0?

        # if x_0 - x_1 == y_0 - y_1 (the negative diagonal)
        # if x_0 - x_1 == y_1- y_0 (the positive diagonal)

        # index = row, val = col
        queens = []
        res = []
        base = '.'*n
        cache = []

        # from set queens, ensure the current x,y
        # not in invalid col, or diagonal
        def notValid(y):
            x = len(queens)
            for ox, oy in enumerate(queens):
                if oy == y or abs(ox-x) == abs(oy-y):
                    return True
            
            return False

        # try each choice
        def dfs():
            # if valid and we've filled the spaces then add to results
            if len(queens) == n:
                res.append(cache.copy())
                return
            
            for i in range(n):
                if notValid(i):
                    continue

                cache.append((base[:i] + 'Q' + base[i+1:]))
                queens.append(i)
                dfs()
                cache.pop()
                queens.pop()

        dfs()

        return res