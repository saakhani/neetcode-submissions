class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs_helper(a, b):
            stack = [(a, b)]
            while stack:
                a, b = stack.pop()
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for da, db in directions:
                    new_a, new_b = a + da, b + db
                    if 0 <= new_a < n and 0 <= new_b < m and grid[new_a][new_b] == '1':
                        stack.append((new_a, new_b))
                        grid[new_a][new_b] = '0'

        n = len(grid)
        m = len(grid[0])
        count = 0
        for i in range (n):
            for j in range (m):
                if grid[i][j] == '1':
                    count += 1
                    dfs_helper(i, j)
        
        return count