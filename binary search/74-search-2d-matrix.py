from ast import List


class Solution:
    def binarySearch(self, arr, target, left, right):
        if left > right:
            return False
        
        mid = int((left + right) / 2)

        if arr[mid] == target:
            return True
        elif target < arr[mid]:
            return self.binarySearch(arr, target, left, mid - 1)
        else:
            return self.binarySearch(arr, target, mid + 1, right)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if self.binarySearch(row, target, 0, len(row) - 1) == True:
                return True
        return False