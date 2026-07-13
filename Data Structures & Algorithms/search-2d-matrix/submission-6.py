class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)
        
        while l < r:
            mid = (l+r)//2

            if target < matrix[mid][0]:
                r = mid
            elif target > matrix[mid][-1]:
                l = mid + 1
            
            else:
                l, r = 0, len(matrix[mid])
        
                while l < r:
                    mid_in = (l+r)//2

                    if matrix[mid][mid_in] == target:
                        return True
                    elif target < matrix[mid][mid_in]:
                        r = mid_in
                    else:
                        l = mid_in + 1
                return False
        return False

