def matrix_vector_multiply(matrix, vector):
    result  = []
    for row in matrix:
        total = 0
        for i in range(len(row)):
            total += row[i] * vector[i]
        result.append(total)
    return result


matrix = [
    [2, 3],
    [4, 5]
]

vector = [2, 3]

print(matrix_vector_multiply(matrix, vector))