class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row_length = len(heights)
        col_length = len(heights[0])

        def dfs_helper(ocean_hash):
            stack = list(ocean_hash)
            while stack:
                a, b = stack.pop()
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for da, db in directions:
                    new_a, new_b = a + da, b + db
                    if 0 <= new_a < row_length and 0 <= new_b < col_length and (new_a, new_b) not in ocean_hash and heights[new_a][new_b] >= heights[a][b]:
                        ocean_hash.add((new_a, new_b))
                        stack.append((new_a, new_b))

        atlantic = set()
        pacific = set()

        for i in range(row_length):
            atlantic.add((i, col_length-1))
            pacific.add((i, 0))

        for i in range(col_length):
            atlantic.add((row_length - 1, i))
            pacific.add((0, i))

        dfs_helper(atlantic)
        dfs_helper(pacific)

        common = atlantic.intersection(pacific)
        return list(common)


        