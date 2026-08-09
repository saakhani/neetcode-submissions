class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        waterMax = 0
        while i < j:
            waterVolume = min(heights[i], heights[j]) * (j - i)
            waterMax = max(waterVolume, waterMax)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return waterMax