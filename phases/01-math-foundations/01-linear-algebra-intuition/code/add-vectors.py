def add_vectors(u, v):
    first = u[0] + v[0]
    second = u[1] + v[1]

    return [first, second]

def add_vectors(u, v):
    if len(u) != len(v):
        raise ValueError("jh dk")
    
    result = []
    for i in range(len(u)):
        result.append(u[i] + v[i])
    return result

u = [2, 3, 4]
v = [1, 5, 6]

print(add_vectors(u, v))