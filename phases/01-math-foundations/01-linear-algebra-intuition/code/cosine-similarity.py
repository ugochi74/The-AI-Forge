from vector_magnitude import vector_magnitude
from dot_product import dot_product


def cosine_similarity(u, v):
    magnitude_u = vector_magnitude(u)
    magnitude_v = vector_magnitude(v)
    if magnitude_u == 0 or magnitude_v == 0:
        raise ValueError("Cannot compare zero vectors")
    product = dot_product(u, v)
    return product / (magnitude_u * magnitude_v)
if __name__ == "__main__":
  v = [1, 0]
  u = [0, 1]
  print(cosine_similarity(u, v))
  u = [3, 4]
  v = [-4, 3]

  print(cosine_similarity(u, v))