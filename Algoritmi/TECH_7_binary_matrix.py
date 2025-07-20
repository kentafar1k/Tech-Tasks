"""Дана целочисленная матрица размером n x n (matrix), обладающая следующими свойствами:

Каждая строка отсортирована в порядке неубывания (элементы в строке идут слева направо в возрастающем порядке).

Первый элемент каждой строки больше последнего элемента предыдущей строки (матрица полностью отсортирована, если "развернуть" её в один список).

Также дан целочисленный параметр target.
Необходимо реализовать функцию search_matrix(matrix: List[List[int]], target: int) -> bool, которая возвращает:"""

from typing import List


def search_matrix(matrix: List[List[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False

    rows = len(matrix)
    cols = len(matrix[0])

    left, right = 0, rows * cols - 1

    while left <= right:
        mid = (left + right) // 2
        row = mid // cols
        col = mid % cols
        mid_val = matrix[row][col]

        if mid_val == target:
            return True
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1

    return False



# Test case 1: Basic test case
matrix1 = [
    [1, 3, 5],
    [7, 9, 11],
    [13, 15, 17]
]
target1 = 9
assert search_matrix(matrix1, target1) == True

# Test case 2: Target not present
matrix2 = [
    [1, 3, 5],
    [7, 9, 11],
    [13, 15, 17]
]
target2 = 10
assert search_matrix(matrix2, target2) == False

# Test case 3: Single row matrix
matrix3 = [[1, 2, 3, 4, 5]]
target3 = 3
assert search_matrix(matrix3, target3) == True

# Test case 4: Single column matrix
matrix4 = [[1], [3], [5], [7], [9]]
target4 = 7
assert search_matrix(matrix4, target4) == True

# Test case 5: Empty matrix
matrix5 = []
target5 = 5
assert search_matrix(matrix5, target5) == False

print("Done")