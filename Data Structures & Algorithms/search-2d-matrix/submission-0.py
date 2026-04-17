class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        low = 0
        high = (n*m)-1
        while low<=high:
            mid = (high+low)//2
            row ,col= mid//m ,mid%m
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]>target:
                high-=1
            else:
                low+=1
        return False       