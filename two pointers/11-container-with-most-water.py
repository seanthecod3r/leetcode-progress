from ast import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = ((r - l) * min(heights[r], heights[l]))
        while l < r:
            if ((r - l) * min(heights[r], heights[l])) > max_area:
                max_area = ((r - l) * min(heights[r], heights[l]))
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                r -= 1
            
        return max_area