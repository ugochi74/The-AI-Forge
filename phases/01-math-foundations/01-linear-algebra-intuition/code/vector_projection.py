
from dot_product import dot_product

def vector_projection(vector_a, vector_b):
    if len(vector_a) != len(vector_b):
        raise ValueError("Vectors must have the same dimensions")

    denominator = dot_product(vector_b, vector_b)

    if denominator == 0:
        raise ValueError("Cannot project onto a zero vector")

    numerator = dot_product(vector_a, vector_b)

    scalar = numerator / denominator

    result = []

    for value in vector_b:
        result.append(scalar * value)

    return result


if __name__ == "__main__":
    vector_a = [3, 4]
    vector_b = [1, 0]

    result = vector_projection(vector_a, vector_b)

    print("Projection:", result)
