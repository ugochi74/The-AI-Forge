# Linear Algebra Intuition

Course lesson: [Linear Algebra Intuition](https://aiengineeringfromscratch.com/lesson?path=phases/01-math-foundations/01-linear-algebra-intuition)

## Learning objectives

- Understand what vectors and matrices actually represent in AI (lists of numbers, spatial arrows, and high-dimensional data points).
- Master basic vector operations from first principles: addition, scalar multiplication, and vector magnitude (length).
- Understand the **dot product** and why it is the backbone of modern AI (measuring similarity, search/RAG, and self-attention in Transformers).
- Understand matrix-vector multiplication as a geometric transformation and as the core operation of a neural network layer.

---

## Key concepts

### 1. What is a Vector?
Depending on who you ask, a vector is:
- **Computer Science view:** A 1-dimensional array or ordered list of numbers (e.g., `[3, 5, 2]`).
- **Physics / Math view:** An arrow in space that has a **magnitude** (length) and a **direction**.
- **AI Engineer view:** An **embedding** or feature representation. Each number in the vector represents an attribute or feature of a concept, word, or image.

```text
2D Vector: [3, 2]
    ^ Y-axis
    |
  2 + - - - > (3, 2)
    |       /
    |     /  Vector arrow
    |   /
    +---+---+---+--> X-axis
    0   1   2   3
```

### 2. Dimension
The number of elements inside a vector:
- `[3, 2]` has 2 dimensions (lives in 2D space).
- `[1, 4, 7]` has 3 dimensions (lives in 3D space).
- In modern AI, word and text embeddings typically have **768**, **1536**, or **4096** dimensions. Even though we cannot picture 1536-dimensional space with our eyes, the math behaves identically to 2D and 3D space!

### 3. Scalar
A single ordinary number (e.g., `3`, `-0.5`, `10`).
When a scalar multiplies a vector, it **scales** (stretches, shrinks, or reverses) its length without changing its line of direction.

### 4. Vector Addition
Adding two vectors element-by-element:
$$\mathbf{u} + \mathbf{v} = [u_1 + v_1, u_2 + v_2, \dots, u_n + v_n]$$
Geometrically, it corresponds to placing the second vector's tail at the tip of the first vector.

### 5. Vector Magnitude (Length)
The length of a vector from the origin $(0, 0)$ to its tip:
$$\|\mathbf{v}\| = \sqrt{v_1^2 + v_2^2 + \dots + v_n^2}$$
A vector with a magnitude of 1 is called a **unit vector** (or normalized vector).

### 6. The Dot Product ($\mathbf{u} \cdot \mathbf{v}$)
Multiply corresponding numbers and sum the results:
$$\mathbf{u} \cdot \mathbf{v} = (u_1 \times v_1) + (u_2 \times v_2) + \dots + (u_n \times v_n)$$

**Why the dot product is so important:**
- It measures **alignment** and **similarity**.
- If two vectors point in the exact same direction: dot product is large and positive.
- If two vectors are perpendicular ($90^\circ$, orthogonal): dot product is **0** (no relationship).
- If two vectors point in opposite directions: dot product is negative.

### 7. Cosine Similarity
$$\text{Cosine Similarity}(\mathbf{u}, \mathbf{v}) = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\| \|\mathbf{v}\|}$$
Cosine similarity ignores vector length and only compares the angle between two vectors:
- `+1.0` = Identical direction (very similar).
- ` 0.0` = Unrelated / perpendicular.
- `-1.0` = Exact opposites.

### 8. Matrices and Transformations
- A **matrix** is a 2D grid of numbers with rows and columns (e.g., $M \times N$).
- In AI, a matrix acts as a **linear transformation**: it takes an input vector and transforms it (rotates, scales, projects) into a new output vector.
- In a neural network layer:
  $$\mathbf{y} = \mathbf{W}\mathbf{x} + \mathbf{b}$$
  where $\mathbf{x}$ is the input vector, $\mathbf{W}$ is the weight matrix (the model's learned knowledge), $\mathbf{b}$ is the bias vector, and $\mathbf{y}$ is the output vector.

---

## Examples and explanations

### Example 1: 2D Vector Addition and Scaling
Suppose we have two vectors:
$$\mathbf{a} = [3, 2], \quad \mathbf{b} = [1, 4]$$

- **Addition:**
  $$\mathbf{a} + \mathbf{b} = [3+1, 2+4] = [4, 6]$$
- **Scalar multiplication ($c = 2$):**
  $$2 \times \mathbf{a} = [2 \times 3, 2 \times 2] = [6, 4]$$
- **Magnitude of $\mathbf{a}$:**
  $$\|\mathbf{a}\| = \sqrt{3^2 + 2^2} = \sqrt{9 + 4} = \sqrt{13} \approx 3.606$$

### Example 2: Dot Product and Similarity
Suppose we represent 3 concepts in a simplified 2D feature space:
`[cuteness, ferocity]`
- **Puppy:** `[0.9, 0.1]`
- **Dog:** `[0.8, 0.3]`
- **Wolf:** `[0.1, 0.9]`

Calculating the dot products:
- **Puppy $\cdot$ Dog:** $(0.9 \times 0.8) + (0.1 \times 0.3) = 0.72 + 0.03 = 0.75$ (high similarity)
- **Puppy $\cdot$ Wolf:** $(0.9 \times 0.1) + (0.1 \times 0.9) = 0.09 + 0.09 = 0.18$ (low similarity)

This simple calculation is the exact intuition behind **Vector Search / RAG** and **Semantic Search**!

### Example 3: Matrix-Vector Product (A Neural Network Layer)
Consider an input vector $\mathbf{x} = [2, 3]$ and a weight matrix $\mathbf{W}$:
$$\mathbf{W} = \begin{bmatrix} 1 & 2 \\ 0 & 1 \\ 3 & -1 \end{bmatrix}$$
Multiplying $\mathbf{W}\mathbf{x}$ means taking the dot product of each row of $\mathbf{W}$ with $\mathbf{x}$:
- Row 1: $(1 \times 2) + (2 \times 3) = 2 + 6 = 8$
- Row 2: $(0 \times 2) + (1 \times 3) = 0 + 3 = 3$
- Row 3: $(3 \times 2) + (-1 \times 3) = 6 - 3 = 3$

Output vector: $\mathbf{y} = [8, 3, 3]$.
A 2-dimensional input was transformed into a 3-dimensional output!

---

## Python practice

We implement all these core concepts from scratch in pure Python without needing external libraries:

```python
import math

def vector_add(u, v):
    return [a + b for a, b in zip(u, v)]

def scalar_multiply(c, v):
    return [c * x for x in v]

def vector_magnitude(v):
    return math.sqrt(sum(x * x for x in v))

def normalize(v):
    mag = vector_magnitude(v)
    return [x / mag for x in v] if mag > 0 else v

def dot_product(u, v):
    return sum(a * b for a, b in zip(u, v))

def cosine_similarity(u, v):
    mag_u = vector_magnitude(u)
    mag_v = vector_magnitude(v)
    if mag_u == 0 or mag_v == 0:
        return 0.0
    return dot_product(u, v) / (mag_u * mag_v)

def matrix_vector_multiply(matrix, vector):
    return [dot_product(row, vector) for row in matrix]
```

---

## What I learned

1. **AI is linear algebra at scale:** At the heart of complex LLMs and neural networks are simply vectors, matrices, and dot products performed billions of times.
2. **Vectors capture meaning:** In modern AI applications, texts, images, and audio are converted into embedding vectors. Similar concepts cluster close together in vector space.
3. **The dot product is our similarity detector:** Whether querying a vector database in RAG or computing self-attention in a Transformer, the dot product determines which tokens and documents are related.
4. **Matrices represent transformations:** Matrix multiplication transforms an input vector from one feature space to another, allowing neural networks to extract high-level patterns from raw data.
