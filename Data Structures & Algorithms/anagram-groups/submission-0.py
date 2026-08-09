class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for string in strs:
            occurences = [0]*26
            for c in string:
                occurences[ord(c) - ord('a')] += 1
            anagrams[tuple(occurences)].append(string)
        return list(anagrams.values())
        
        