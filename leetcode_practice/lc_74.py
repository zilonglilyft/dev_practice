"""
leetcode 74: https://leetcode.com/problems/search-a-2d-matrix/
"""


def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    l = len(matrix)
    if l == 0:
        return False
    w = len(matrix[0])
    if w == 0:
        return False
    left = 0
    right = w * l - 1
    while left <= right:
        mid = (left + right) // 2
        i = mid // w
        j = mid % w
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] > target:
            right = mid - 1
        else:
            left = mid + 1
    else:
        return False

"""
expand the traditional binary search to 2 dimension matrix. Notes:
1. check if l and w is empty. Have to check both
2. the only difference to the traditional binary search is to break the mid further by i = mid//w, and j = mid%w
"""