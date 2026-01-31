def search_matrix(matrix, target):
    sort_matrix=[]
    for i in matrix:
        (sort_matrix.extend(i))
    sort_matrix.sort()
    if target in sort_matrix:
        return True
    else:
        return False



matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
print(search_matrix(matrix, 4))  # True
print(search_matrix(matrix, 16))  # False