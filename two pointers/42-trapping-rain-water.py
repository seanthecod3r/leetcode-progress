from ast import List


class Solution:
    def trap(self, height: List[int]) -> int:

        if not height: return 0

        total_area, l, r = 0, 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                total_area += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                total_area += rightMax - height[r]
        return total_area
