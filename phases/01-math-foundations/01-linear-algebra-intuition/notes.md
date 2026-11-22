# Linear Algebra Intuition

Course lesson: [Linear Algebra Intuition](https://aiengineeringfromscratch.com/learn/math-foundations/linear-algebra-intuition)

## What you should learn

By the end of this lesson, you should be able to:

- Explain what a vector and a matrix are.
- Add vectors and multiply a vector by a scalar.
- Calculate a vector's magnitude (length).
- Calculate a dot product and explain what its sign tells us.
- Understand how matrices transform vectors.
- Determine linear independence, basis, and rank.
- Explain projection and Gram-Schmidt, and connect these ideas to AI.

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

## 10. Python practice

The `code/` directory contains pure Python implementations for vector operations, cosine similarity, matrix-vector multiplication, and a simple neural-network layer.

Run individual scripts from the repository root. Read one function at a time and test it with small inputs.

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

---

## 13. Linear layer with an activation function

A neural network layer can first perform a linear transformation and then apply an activation function.

The linear transformation is:

`y = W × x + b`

- `x` is the input vector.
- `W` is the weight matrix.
- `b` is the bias vector.
- `y` is the linear output.

The **ReLU** activation function is:

`ReLU(z) = max(0, z)`

It keeps positive values and changes negative values to zero. For example:

`ReLU([-3, 2, -4, 9]) = [0, 2, 0, 9]`

Applying ReLU after the linear transformation gives:

`activated_output = ReLU(W × x + b)`

An activation function such as ReLU adds non-linearity. This allows a neural network to learn more than a simple linear relationship.

## 14. A two-layer feed-forward network

A two-layer network sends the input through one layer, then sends that layer's output into the next layer.

The process is:

1. Pass the original input through the first linear layer.
2. Apply ReLU to the first layer's output.
3. Use that activated output as the second layer's input.
4. Apply the second layer and return its output.

The implementation in `two_layer_network.py` uses the reusable `linear_layer_with_relu()` function twice.

For the example values in the script:
- Input: `[2, 3]`
- First layer output after ReLU: `[0, 6, 0]`
- Final output after the second layer and ReLU: `[13, 4]`

The script was run successfully and printed `[13, 4]`. This is a forward-pass demonstration with fixed weights and biases. It does not train the network or update its weights.

## 15. Forward propagation and loss

**Forward propagation** is the process of passing input data through the network's layers to calculate a prediction.

A **loss function** measures how far a prediction is from the correct target value. For one example:

- Prediction: `15`
- Actual target: `20`
- Squared error: `(20 - 15)² = 25`

For multiple examples, **Mean Squared Error (MSE)** is the average of all squared prediction errors:

`MSE = sum((actual - prediction)²) / number_of_examples`

Keep these steps separate:
- Forward propagation produces the prediction.
- The loss function measures prediction error.
- Training uses the error to adjust model parameters.

MSE was introduced as an additional neural-network concept, but it is not the next unfinished requirement on the official Linear Algebra Intuition lesson page.

---

## 16. Linear independence

A set of vectors is **linearly independent** when no vector in the set can be made by combining the other vectors.

If at least one vector can be written as a combination of the others, the set is **linearly dependent**.

Example:

`v1 = [1, 0, 0]`

`v2 = [0, 1, 0]`

`v3 = [2, 1, 0]`

Notice:

`v3 = 2 × v1 + v2`

Check:

`2 × [1, 0, 0] + [0, 1, 0] = [2, 1, 0]`

Therefore, the three-vector set is linearly dependent. The first two vectors are independent, while the third adds no new independent direction.

### Another example practised

`v1 = [1, 2, 0]`

`v2 = [0, 1, 1]`

`v3 = [1, 3, 1]`

Since:

`v1 + v2 = [1, 3, 1] = v3`

the three vectors are linearly dependent. There are **two independent vectors** in this set.

## 17. Basis

A **basis** is a set of vectors that satisfies two conditions:

1. The vectors are linearly independent.
2. They span the space, meaning their combinations can represent every vector in that space.

Example:

`[1, 0]` and `[0, 1]` form a basis for the 2D plane. Any 2D vector `[x, y]` can be written as:

`[x, y] = x × [1, 0] + y × [0, 1]`

The vectors are independent and together span the entire 2D plane.

## 18. Matrix rank

The **rank** of a matrix is the number of independent rows or, equivalently, the number of independent columns.

Consider:

`A = [[1, 0, 2], [0, 1, 1], [2, 1, 5]]`

The third row is a combination of the first two:

`R3 = 2 × R1 + R2`

So the three rows are not all independent. There are two independent rows, and the matrix has rank 2.

### Finding rank with row reduction

Row reduction uses three elementary row operations:

- Swap two rows.
- Multiply a row by a non-zero number.
- Add a multiple of one row to another row.

For the matrix above:

Start with:

`[[1, 0, 2], [0, 1, 1], [2, 1, 5]]`

First, replace row 3 with row 3 minus twice row 1:

`[[1, 0, 2], [0, 1, 1], [0, 1, 1]]`

Then replace row 3 with row 3 minus row 2:

`[[1, 0, 2], [0, 1, 1], [0, 0, 0]]`

There are two non-zero rows, so the rank is 2.

**Remember:** After row reduction to echelon form, count the non-zero rows to find the rank.

### Python implementation plan

The next practical task is to create `code/matrix_rank.py`. The planned function will:

1. Validate that the matrix is not empty and that all rows have equal length.
2. Make a copy so the original matrix is not changed.
3. Find a non-zero pivot in each column.
4. Swap rows when needed and eliminate values below each pivot.
5. Count the pivots to return the rank.

A code walkthrough was provided, but the file has **not yet been confirmed as created or run**. Do not treat the implementation as verified until it is tested locally.

## 19. Today's revision — 22 November 2026

What I learned:

- Linear independence means that no vector in a set can be formed from the other vectors.
- Linear dependence means at least one vector can be expressed as a combination of the others.
- A basis is a linearly independent set that spans the space.
- Matrix rank counts independent rows or columns.
- Row reduction helps reveal dependent rows and calculate rank.
- In the example matrix, the third row equals twice the first row plus the second row, so the matrix has rank 2.
- In the vector exercise, `[1, 3, 1]` equals `[1, 2, 0] + [0, 1, 1]`, so the set contains two independent vectors.

**Checkpoint:** Correctly identified the three-vector set as linearly dependent and correctly answered that it contains two independent vectors.

**Not yet verified:** The `matrix_rank.py` implementation has been explained but has not yet been confirmed as saved, executed, or tested.

**Next steps in the official lesson:**
1. Create and test `matrix_rank.py` using row reduction.
2. Complete the official linear independence and rank exercises.
3. Learn vector projection.
4. Learn Gram-Schmidt and verify orthonormal vectors.
5. Continue with the lesson's NumPy and PyTorch applications.

