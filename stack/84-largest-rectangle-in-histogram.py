from ast import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = max(min(heights) * len(heights), max(heights))
        max_rec = 0
        
        for i, height in enumerate(heights):
            newHeights = heights[i:len(heights) - i]
            if len(newHeights) > 0:
                new_max_rec = max(min(newHeights) * len(newHeights), max(heights))
                max_rec = max(new_max_rec, max_rec)
        
        for i, height in enumerate(heights):
            newHeights = heights[i:]
            if len(newHeights) > 0:
                new_max_rec = max(min(newHeights) * len(newHeights), max(heights))
                max_rec = max(new_max_rec, max_rec)

        heights.reverse()
        
        for i, height in enumerate(heights):
            newHeights = heights[i:]
            if len(newHeights) > 0:
                new_max_rec = max(min(newHeights) * len(newHeights), max(heights))
                max_rec = max(new_max_rec, max_rec)
        return max_rec
        