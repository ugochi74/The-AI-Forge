from relu import linear_layer_with_relu

def two_layer_network(x, W1, b1, W2, b2):
    first_output = linear_layer_with_relu(W1, x, b1)
    second_output = linear_layer_with_relu(W2, first_output, b2)
    return second_output


if __name__ == "__main__":
 x = [2, 3]

 W1 = [
    [2, -3],
    [-4, 5],
    [1, -2]
 ]

 b1 = [1, -1, 2]

 W2 = [
    [1, 2, 1],
    [2, 1, 1]
 ]

 b2 = [1, -2]

 print(two_layer_network(x, W1, b1, W2, b2))