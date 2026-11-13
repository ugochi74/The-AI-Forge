"""
Linear Algebra Intuition - Phase 1, Lesson 1
AI Engineering from Scratch

Fundamental vector and matrix operations implemented from first principles
in pure Python (zero external dependencies).
"""

import math
from typing import List, Tuple

Vector = List[float]
Matrix = List[List[float]]


def vector_add(u: Vector, v: Vector) -> Vector:
    """Add two vectors element-by-element."""
    if len(u) != len(v):
        raise ValueError(f"Vectors must have the same dimension: {len(u)} != {len(v)}")
    return [a + b for a, b in zip(u, v)]


def vector_subtract(u: Vector, v: Vector) -> Vector:
    """Subtract vector v from vector u."""
    if len(u) != len(v):
        raise ValueError(f"Vectors must have the same dimension: {len(u)} != {len(v)}")
    return [a - b for a, b in zip(u, v)]


def scalar_multiply(c: float, v: Vector) -> Vector:
    """Multiply a vector by a scalar number."""
    return [c * x for x in v]


def vector_magnitude(v: Vector) -> float:
    """Calculate the Euclidean length (L2 norm) of a vector."""
    return math.sqrt(sum(x * x for x in v))


def normalize_vector(v: Vector) -> Vector:
    """Scale a vector so its magnitude is 1.0 (unit vector)."""
    mag = vector_magnitude(v)
    if mag == 0.0:
        raise ValueError("Cannot normalize a zero vector")
    return [x / mag for x in v]


def dot_product(u: Vector, v: Vector) -> float:
    """
    Compute the dot product of two vectors: sum(u_i * v_i).
    Measures the directional alignment of two vectors.
    """
    if len(u) != len(v):
        raise ValueError(f"Vectors must have the same dimension: {len(u)} != {len(v)}")
    return sum(a * b for a, b in zip(u, v))


def cosine_similarity(u: Vector, v: Vector) -> float:
    """
    Compute cosine similarity: (u . v) / (||u|| * ||v||).
    Returns a score between -1.0 (opposite) and +1.0 (identical direction).
    """
    mag_u = vector_magnitude(u)
    mag_v = vector_magnitude(v)
    if mag_u == 0.0 or mag_v == 0.0:
        raise ValueError("Cannot compute cosine similarity with a zero vector")
    return dot_product(u, v) / (mag_u * mag_v)


def matrix_vector_multiply(W: Matrix, x: Vector) -> Vector:
    """
    Multiply a matrix W (shape M x N) by a vector x (length N).
    Each element of the output is the dot product of a matrix row with x.
    This is the core forward operation of a neural network linear layer!
    """
    if not W:
        return []
    n_cols = len(W[0])
    if len(x) != n_cols:
        raise ValueError(f"Matrix columns ({n_cols}) must match vector length ({len(x)})")
    return [dot_product(row, x) for row in W]


def linear_layer(W: Matrix, x: Vector, b: Vector) -> Vector:
    """
    Neural Network Linear Layer: y = Wx + b
    """
    Wx = matrix_vector_multiply(W, x)
    return vector_add(Wx, b)


def run_demonstrations():
    print("=" * 60)
    print("PHASE 1, LESSON 1: LINEAR ALGEBRA INTUITION")
    print("=" * 60)

    # 1. Basic Vector Operations
    print("\n--- 1. Basic Vector Operations ---")
    u = [3.0, 2.0]
    v = [1.0, 4.0]
    print(f"Vector u: {u}")
    print(f"Vector v: {v}")
    print(f"u + v:    {vector_add(u, v)}")
    print(f"u - v:    {vector_subtract(u, v)}")
    print(f"2 * u:    {scalar_multiply(2.0, u)}")
    print(f"||u||:    {vector_magnitude(u):.4f}")
    print(f"u_norm:   {[round(x, 4) for x in normalize_vector(u)]}")

    # 2. Dot Product & Alignment
    print("\n--- 2. Dot Product & Alignment ---")
    same_dir = [2.0, 2.0]
    perp_dir = [-2.0, 2.0]
    opp_dir = [-2.0, -2.0]

    print(f"Dot product (same direction):     {dot_product(u, same_dir):.2f}")
    print(f"Dot product (perpendicular 90°): {dot_product([2.0, 0.0], [0.0, 3.0]):.2f} (orthogonal)")
    print(f"Dot product (opposite direction): {dot_product([1.0, 2.0], [-1.0, -2.0]):.2f}")

    # 3. AI Intuition: Semantic Similarity (RAG / Embeddings)
    print("\n--- 3. AI Intuition: Embeddings & Cosine Similarity ---")
    # Toy 3D embeddings: [is_animal, is_pet, is_mechanical]
    embeddings = {
        "puppy":    [0.90, 0.95, 0.05],
        "dog":      [0.85, 0.88, 0.08],
        "wolf":     [0.92, 0.15, 0.10],
        "airplane": [0.02, 0.01, 0.98]
    }

    query = "dog"
    print(f"Query concept: '{query}'")
    for word, emb in embeddings.items():
        sim = cosine_similarity(embeddings[query], emb)
        print(f"  Similarity with '{word:<8}': {sim:.4f}")

    # 4. AI Intuition: Neural Network Linear Layer (y = Wx + b)
    print("\n--- 4. AI Intuition: Neural Network Linear Layer (y = Wx + b) ---")
    # Input vector: 2 features (e.g., [temperature, humidity])
    x = [25.0, 60.0]
    # Weight matrix: 3 output neurons x 2 inputs
    W = [
        [0.2,  0.5],   # Neuron 1 weights
        [-0.1, 0.8],   # Neuron 2 weights
        [0.4, -0.3]    # Neuron 3 weights
    ]
    # Bias vector for 3 neurons
    b = [1.0, 0.5, -2.0]

    y = linear_layer(W, x, b)
    print(f"Input features (x):    {x}")
    print(f"Weight matrix (W):     {W}")
    print(f"Bias vector (b):       {b}")
    print(f"Layer output (y=Wx+b): {[round(val, 2) for val in y]}")

    # 5. Sanity Assertions
    assert vector_add([1, 2], [3, 4]) == [4, 6]
    assert dot_product([1, 2], [3, 4]) == 11
    assert math.isclose(cosine_similarity([1, 0], [0, 1]), 0.0, abs_tol=1e-7)
    assert math.isclose(cosine_similarity([2, 0], [5, 0]), 1.0, abs_tol=1e-7)
    print("\n[OK] All internal tests and assertions passed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    run_demonstrations()
