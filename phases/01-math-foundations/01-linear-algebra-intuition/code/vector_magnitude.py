import math

def vector_magnitude(v):
    total = 0

    for number in v:
        total += number * number

    return math.sqrt(total)


def vector_mag(v):
    total = 0
    for number in v:
        total += number ** 2
    return total ** 0.5

# v = [6, 8]

# (v[0]**2 + v[1]**2)**0.5
if __name__ == "__main__":
 v = [12, 5]
 print(vector_magnitude(v))

 v = [3, 4]

 print(vector_mag(v))