class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0 
        for c in range(0, (2*n-1)):
            left, right = c // 2, c // 2 + c % 2
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1
        return count


        