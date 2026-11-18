def matrix_vector_multiply(matrix, vector):
    result  = []
    for row in matrix:
        total = 0
        for i in range(len(row)):
            total += row[i] * vector[i]
        result.append(total)
    return result

if __name__ == "__main__":
 matrix = [
    [2, 3],
    [4, 5]
 ]

 vector = [3, 2]

 print(matrix_vector_multiply(matrix, vector))