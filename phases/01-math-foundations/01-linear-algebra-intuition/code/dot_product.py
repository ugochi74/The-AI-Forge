def dot_product(u, v):
    if len(u) != len(v):
        raise ValueError("Vectors must have the same lenght")
    total = 0
    for i in range(len(u)):
        total += u[i] * v[i]
    return total
if __name__ == "__main__":
 u = [3, 2]
 v = [4, 5]

 print(dot_product(u, v))