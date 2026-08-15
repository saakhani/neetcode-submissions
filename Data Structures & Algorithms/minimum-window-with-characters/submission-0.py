class Solution:
    def minWindow(self, s: str, t: str) -> str:
        remaining = len(t)
        need = {}
        for char in t:
            need[char] = need.get(char, 0) + 1
        left, right = 0, -1
        shortest = float('inf')
        leftMin, rightMin = 0, -1

        while right < len(s):
            while remaining == 0:
                subLength = len(s[left:right+1])
                if subLength < shortest:
                    shortest = subLength
                    leftMin, rightMin = left, right
                
                # logic for moving the left pointer
                need[s[left]] = need.get(s[left], 0) + 1
                if need[s[left]] > 0:
                    remaining += 1
                left += 1

            right += 1
            if right >= len(s): break
            if (need.get(s[right], 0) > 0):
                remaining -= 1
            need[s[right]] = need.get(s[right], 0) - 1
            
        return s[leftMin:rightMin + 1]

        
        