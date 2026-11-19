from matrix_vector_multiplication import matrix_vector_multiply

def linear_layer(weight, inputs, bias):
    result = matrix_vector_multiply(weight, inputs)
    if len(result) != len(bias):
        raise ValueError("Bias length must match output length")

    output = []
    for i in range(len(result)):
        output.append(result[i] + bias[i])
    return output



W = [
    [2, 3],
    [4, 5], 
    [5, 6]
]

x = [2, 3]

b = [1, 2, 3]
print(linear_layer(W, x, b))

