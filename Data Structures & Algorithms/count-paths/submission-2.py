class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def _uniquePaths(m, n, r, c, memo):
            pos = (r, c)
            if pos in memo:
                return memo[pos]

            if r == m-1 and c == n-1:
                return 1

            if r == m or c == n:
                return 0

            down = _uniquePaths(m, n, r+1, c, memo)
            right = _uniquePaths(m, n, r, c+1, memo)

            memo[pos] = down + right
            return memo[pos]

        return _uniquePaths(m, n, 0, 0, {})