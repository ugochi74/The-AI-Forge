from linear_layer import linear_layer
def relu(value):
    return max(0, value)


# result = []

# for value in output:
#     result.append(relu(value))
# print(result)

def relu_vector(vector):
    result = []
    for value in vector:
        result.append(relu(value))
    return result

# output = [-3, 2, -4, 9]
# print(relu_vector(output))

def linear_layer_with_relu(W, x, b):
    linear_output = linear_layer(W, x, b)
    activated_output = relu_vector(linear_output)
    return activated_output

if __name__ == "__main__":
 W = [
    [2, -3],
    [-4, 5],
    [1, -2]
 ]

 x = [2, 3]

 b = [1, -1, 2]

 print(linear_layer_with_relu(W, x, b))