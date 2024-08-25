from ast import List


class Solution:
    def binarySearch(self, arr, target, left, right):
        if left > right:
            return -1
        
        mid = int((left + right) / 2)

        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            return self.binarySearch(arr, target, left, mid - 1)
        else:
            return self.binarySearch(arr, target, mid + 1, right)

    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, target, 0, len(nums) - 1)