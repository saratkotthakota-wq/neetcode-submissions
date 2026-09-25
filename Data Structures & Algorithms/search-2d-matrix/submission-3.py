class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rowl, rowr = 0, len(matrix)-1
        targetRow = -1

        while rowl <= rowr:
            mid = (rowl+rowr)//2
            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                targetRow = mid
                break
            if target < matrix[mid][0]:
                rowr = mid - 1
            if target > matrix[mid][-1]:
                rowl = mid + 1

        if targetRow == -1:
            return False

        l, r = 0, len(matrix[targetRow])-1

        while l <= r:
            mid = (l+r)//2
            if matrix[targetRow][mid] == target:
                return True
            if matrix[targetRow][mid] < target:
                l = mid+1
            if matrix[targetRow][mid] > target:
                r = mid-1
        return False
        
                