class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        maxLength, maxi, maxj = 0, 0 ,0
        for c in range(0, (2*n-1)):
            left, right = c // 2, c // 2 + c % 2
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            palindromeLength = right - left - 1
            if palindromeLength > maxLength:
                maxLength = palindromeLength
                maxi, maxj = left + 1, right - 1
        return s[maxi:maxj+1]

