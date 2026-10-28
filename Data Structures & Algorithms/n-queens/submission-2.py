class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        queens = []
        res = []

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
                cache = []
                base = '.'*n
                for i in queens:
                    cache.append((base[:i] + 'Q' + base[i+1:]))
                res.append(cache.copy())
                return
            
            for i in range(n):
                if notValid(i):
                    continue
                queens.append(i)
                dfs()
                queens.pop()

        dfs()

        return res