def vector_magnitude(v):
    total = 0

    for number in v:
        total += number ** 2

    return total ** 0.5



def normalize_vector(v):
    magnitude = vector_magnitude(v)

    if magnitude == 0:
        raise ValueError("Cannot normalize a zero vector")

    result = []

    for number in v:
        result.append(number / magnitude)

    return result


v = [3, 4]

print(vector_magnitude(v))
print(normalize_vector(v))