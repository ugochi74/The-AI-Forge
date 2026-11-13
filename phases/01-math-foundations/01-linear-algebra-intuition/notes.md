# Linear Algebra Intuition

Course lesson: [Linear Algebra Intuition](https://aiengineeringfromscratch.com/lesson?path=phases/01-math-foundations/01-linear-algebra-intuition)

## What you should learn

By the end of this lesson, you should be able to:

- Explain what a vector and a matrix are.
- Add vectors and multiply a vector by a scalar.
- Calculate a vector's magnitude (length).
- Calculate a dot product and explain what its sign tells us.
- Understand, at a basic level, how a matrix can transform a vector.

You do not need to memorize every formula at once. Work through the small examples first.

---

## 1. What is a vector?

A **vector** is an ordered list of numbers.

Example:

`[3, 2]`

This vector contains two numbers:

- First component: `3`
- Second component: `2`

The order matters. `[3, 2]` and `[2, 3]` are different vectors.

In a simple 2D drawing, we can picture a vector as an arrow from the starting point `(0, 0)` to the point `(3, 2)`.

In machine learning, vectors are used to store numerical features. A text or image embedding is also a vector: a list of numbers created by a model to represent information.

**Remember:** A vector is an ordered collection of numbers. In 2D or 3D, we can draw it as an arrow. In AI, it may have hundreds or thousands of components.

## 2. Dimensions and components

A **component** is one number inside a vector.

The **dimension** is the number of components.

| Vector | Number of components | Dimension |
|---|---:|---:|
| `[3, 2]` | 2 | 2D |
| `[1, 4, 7]` | 3 | 3D |
| `[2, 5, 1, 8]` | 4 | 4D |

A vector with 768 components is a 768-dimensional vector. We cannot easily draw that many dimensions, but we can still perform the same kinds of calculations.

## 3. Scalar multiplication

A **scalar** is one ordinary number, such as `2`, `-3`, or `0.5`.

Scalar multiplication means multiplying every component of a vector by that number.

Example:

`A = [2, 3]`

`3 × A = [3 × 2, 3 × 3] = [6, 9]`

A positive scalar changes the vector's length without reversing its direction. A negative scalar also reverses its direction.

## 4. Vector addition

To add two vectors, add the numbers in matching positions.

Example:

`A = [2, 3]`

`B = [4, 5]`

`A + B = [2 + 4, 3 + 5] = [6, 8]`

The vectors must have the same number of components.

## 5. Magnitude: the length of a vector

The **magnitude** tells us how long a vector is.

For a 2D vector `[x, y]`:

`magnitude = √(x² + y²)`

Example: find the magnitude of `[3, 4]`.

`√(3² + 4²) = √(9 + 16) = √25 = 5`

For a 3D vector, include the third component:

`[2, 3, 6]`

`magnitude = √(2² + 3² + 6²) = √49 = 7`

A **unit vector** is a vector whose magnitude is 1. Normalizing a non-zero vector means changing its length to 1 while keeping its direction.

## 6. The dot product

The **dot product** takes two vectors, multiplies the numbers in matching positions, and adds those products. The answer is one number (a scalar).

Example:

`A = [2, 4]`

`B = [4, 2]`

`A · B = (2 × 4) + (4 × 2) = 8 + 8 = 16`

The vectors must have the same number of components.

For two non-zero vectors, the sign of the dot product tells us about their angle:

- **Positive:** the angle is less than 90°.
- **Zero:** the vectors are perpendicular (90°).
- **Negative:** the angle is greater than 90°.

A positive dot product does not automatically mean two vectors are highly similar, because the result also depends on their lengths. Cosine similarity is used when we want to compare direction while accounting for vector length.

## 7. Cosine similarity

**Cosine similarity** compares the direction of two non-zero vectors. It is calculated by dividing their dot product by the product of their magnitudes.

`cosine similarity = (A · B) / (magnitude(A) × magnitude(B))`

Its value is between -1 and +1:

| Value | Meaning |
|---:|---|
| +1 | Same direction |
| 0 | Perpendicular directions |
| -1 | Opposite directions |

A value closer to +1 means the vectors point in more similar directions. In search systems, this can help compare text or image embeddings.

**Important:** A cosine similarity of zero means the vectors are perpendicular. It does not prove that the real-world ideas are unrelated.

Cosine similarity cannot be calculated for a zero vector because its magnitude is zero and division by zero is not allowed.

## 8. What is a matrix?

A **matrix** is a rectangular arrangement of numbers in rows and columns.

Example:

`A = [[1, 2], [3, 4]]`

It has:

- 2 rows
- 2 columns
- Shape: 2 × 2

Read a matrix by finding the row first and then the column. In this example, the number in row 2, column 1 is `3`.

Matrices help store and work with groups of numbers. In machine learning, they are commonly used for datasets and model calculations.

## 9. How a matrix transforms a vector

A matrix can multiply a vector to produce a new vector. This operation is called **matrix-vector multiplication**.

Example:

`W = [[1, 2], [0, 1]]`

`x = [2, 3]`

Multiply each matrix row by the vector:

- First row: `(1 × 2) + (2 × 3) = 8`
- Second row: `(0 × 2) + (1 × 3) = 3`

The result is:

`W × x = [8, 3]`

The matrix has transformed the input vector `[2, 3]` into `[8, 3]`.

The number of values in the input vector must match the number of columns in the matrix.

A neural network uses this kind of calculation in a layer. A common form is:

`y = W × x + b`

- `x` is the input vector.
- `W` is the weight matrix.
- `b` is the bias vector.
- `y` is the output vector.

For now, remember that the layer takes numerical input, performs matrix-vector multiplication, and adds a bias.

---

## 10. Python practice

The file `code/vectors.py` contains pure Python functions for vector addition, subtraction, scalar multiplication, magnitude, normalization, dot product, cosine similarity, matrix-vector multiplication, and a simple neural-network layer.

Run it from the repository root:

```bash
python3 phases/01-math-foundations/01-linear-algebra-intuition/code/vectors.py
```

The captured result is saved in `outputs/vectors-output.txt`. The verification steps are recorded in `verification/run-check.md`.

Start by reading one function at a time. For example, `vector_add` adds matching components. You do not need to understand the whole file at once.

## 11. Quick revision

- **Vector:** an ordered list of numbers.
- **Component:** one number in a vector.
- **Dimension:** the number of components.
- **Scalar multiplication:** multiply every component by one number.
- **Vector addition:** add matching components.
- **Magnitude:** the length of a vector.
- **Dot product:** multiply matching components and add the results.
- **Cosine similarity:** compare the directions of two non-zero vectors.
- **Matrix:** numbers arranged in rows and columns.
- **Matrix-vector multiplication:** use a matrix to calculate a new vector.

## 12. Connection to AI

Machine learning models work with numbers. Vectors can represent input features and embeddings. Matrices help models process groups of numbers and transform vectors. Dot products and cosine similarity are useful in operations such as comparing embeddings and calculating attention scores.

These are building blocks. Real AI systems combine many such operations with additional ideas and algorithms.
