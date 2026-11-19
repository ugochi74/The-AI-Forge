def matrix_vector_multiply(matrix, vector):
    if not matrix:
       raise ValueError("Matrix cannot be emptys")
    for row in matrix:
        if len(row) != len(vector):
           raise ValueError("Matrix columns must match vector length")
    result  = []
    for row in matrix:
       total = 0
       for i in range(len(row)):
            total += row[i] * vector[i]
       result.append(total)
    return result

if __name__ == "__main__":
 matrix = []

 vector = [2, 3]

 print(matrix_vector_multiply(matrix, vector))