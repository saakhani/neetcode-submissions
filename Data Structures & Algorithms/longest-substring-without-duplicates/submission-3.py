class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 1
        n = len(s)
        if (n == 0):
            return 0
        characters = {s[0]}
        max = 1
        while r < n:
            while s[r] in characters:
                characters.remove(s[l])
                l += 1
            characters.add(s[r])
            r += 1
            length = r - l
            if ((length)>max):
                max = length
        return max


