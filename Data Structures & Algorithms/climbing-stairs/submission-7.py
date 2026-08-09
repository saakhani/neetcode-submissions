class Solution:
    def climbStairs(self, n: int) -> int:
        stairs = [-1] * (n)
        if n <= 2:
            return n
        stairs[0] = 1
        stairs[1] = 2
        for i in range (2, n):
            if stairs[i] != -1:
                continue
            else:
                stairs[i] = stairs[i-1] + stairs[i-2]
        return stairs[n-1]
