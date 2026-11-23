# Lesson Reflection: Linear Algebra Intuition

## What I understood

- **Vectors:** A vector is an ordered list of numbers. The order matters, and the number of values tells us its dimension.
- **Vector operations:** Vector addition combines matching components. Scalar multiplication multiplies every component by the same number.
- **Magnitude:** Magnitude measures the length of a vector.
- **Dot product:** The dot product multiplies matching components and adds the results. For two non-zero vectors, its sign tells us whether the angle is below, equal to, or above 90 degrees.
- **Matrices:** A matrix is a grid of numbers arranged in rows and columns. Matrix-vector multiplication uses the rows of a matrix to calculate a new vector.
- **Connection to AI:** Vectors can represent data features and embeddings. Matrices and dot products are used in neural network calculations and embedding comparisons.

## What I found difficult

- **Thinking about many dimensions:** It is easy to picture a 2D or 3D vector, but difficult to picture a vector with hundreds of components. The calculations still follow the same rules.
- **Rows and columns:** I need more practice identifying matrix shapes and matching the matrix columns with the vector length during matrix-vector multiplication.
- **Connecting the formulas to AI:** I understand the basic idea, but I need more examples to see how these operations are used in real machine learning systems.

## What I need to practise

- Calculate vector addition, scalar multiplication, magnitude, and dot products by hand.
- Identify matrix rows, columns, and shapes.
- Practise matrix-vector multiplication using small examples.
- Read and run the Python functions in the `code/` directory one at a time.
- Learn how cosine similarity compares embedding directions.

## Key takeaway

Linear algebra gives machine learning a way to represent and work with numerical data. Vectors hold ordered numbers, matrices organize numbers and transform vectors, and operations such as dot products help compare and process them. I should understand the small examples first before moving to more advanced AI applications.

## Personal Reflection

- The dot product measures how two vectors relate to each other. It is especially useful in AI when comparing embeddings.
- In AI, words, sentences, images, and other data can be represented as numerical vectors called embeddings.
- Cosine similarity helps measure how similar two embedding directions are.

The cosine similarity formula is:

`similarity(u, v) = (u · v) / (magnitude(u) × magnitude(v))`

---

## Reflection — 20 November 2026

### What I learned

- I can combine smaller functions to build a larger neural-network operation.
- A linear layer calculates `W × x + b`; ReLU is then applied to its output.
- ReLU changes negative values to zero and leaves positive values unchanged.
- In a two-layer feed-forward network, the first layer's activated output becomes the second layer's input.
- I implemented the two-layer forward pass and ran the script. The verified output for the example was `[13, 4]`.
- Forward propagation and loss are different: forward propagation produces a prediction, while loss measures how far that prediction is from the target.

### What I found challenging

- Understanding how the output of one layer becomes the input of the next layer.
- Separating the jobs of the network's forward pass and the loss function.
- Remembering that ReLU is applied after the linear calculation, not before it.

### What I can explain now

A two-layer network takes an input, applies a linear transformation and ReLU, then passes that result through another linear transformation and ReLU. This produces the network's final prediction. A loss function can then compare that prediction with the correct target.

### What I still need to practise

- Implement Mean Squared Error (MSE) if it is revisited as part of a later neural-network topic.
- Understand how a loss value relates to model training.
- Later, learn how backpropagation uses the loss to help update weights and biases.

### Evidence and limits

- Ran `two_layer_network.py` successfully.
- Verified output: `[13, 4]`.
- The network uses fixed weights and biases. It is a forward-pass demonstration, not a trained model.
- MSE has been introduced conceptually only; no loss function, backpropagation, or parameter update has been implemented yet.

---

## Reflection — 22 November 2026

### What I learned

- A set of vectors is linearly independent when none of its vectors can be made by combining the others.
- A set is linearly dependent when at least one vector can be expressed as a combination of the other vectors.
- A basis must be both linearly independent and able to span the space.
- Matrix rank is the number of independent rows or columns.
- Row reduction helps reveal which rows are dependent. Once a matrix is in echelon form, the number of non-zero rows gives its rank.

### Examples I can explain

For these vectors:

- `v1 = [1, 2, 0]`
- `v2 = [0, 1, 1]`
- `v3 = [1, 3, 1]`

I found that:

`v1 + v2 = v3`

Therefore, the set is linearly dependent and contains two independent vectors. I answered both the dependence question and the independent-vector count correctly.

For this matrix:

`[[1, 0, 2], [0, 1, 1], [2, 1, 5]]`

the third row is twice the first row plus the second row. Row reduction produces two non-zero rows and one zero row, so its rank is 2.

### What I found challenging

- Understanding that a vector can be dependent even when its individual values are different from the other vectors.
- Connecting the idea of a combination of vectors to the number of independent directions.
- Remembering that rank counts independent rows or columns, not simply the total number of rows or columns.

### What I still need to practise

- Implement row reduction in Python and test the rank function with different matrices.
- Practise identifying pivots and zero rows.
- Continue with projection and Gram-Schmidt, which are still outstanding parts of the official lesson.

### Evidence and limits

- Correctly identified `[1, 3, 1]` as the sum of `[1, 2, 0]` and `[0, 1, 1]`.
- Correctly stated that the example set contains two independent vectors.
- Followed a walkthrough of a possible `matrix_rank.py` implementation.
- The Python implementation has not yet been confirmed as created or executed, so no successful code test is claimed.
- No official lesson quiz score is recorded for this session.

### Personal takeaway

I learned that having more vectors does not always mean having more independent information. A vector can be a combination of other vectors. Rank helps us measure how much independent information a matrix contains. I should verify the idea with my own Python implementation before moving on.


---

## Reflection — 23 November 2026

### What I practised
- Restarted linear independence and linear dependence from the mathematical basics.
- Practised scalar multiplication and remembered to multiply every component by the same scalar.
- Practised vector addition and linear combinations.
- Correctly recognised dependent pairs when one vector was a scalar multiple of the other.
- Correctly recognised an independent pair when no single scalar could produce one vector from the other.
- Learned that any set containing the zero vector is linearly dependent.
- Correctly expressed `[2, 3]` as `2A + 3B` and `[4, 5]` as `4A + 5B`, where `A = [1, 0]` and `B = [0, 1]`.

### What became clearer
- The same scalar must work for every component when checking whether two vectors are scalar multiples.
- With three or more vectors, dependence can happen through a combination of multiple vectors, not only through a scalar multiple of one vector.
- Two vectors can be independent while adding another vector that is their combination makes the whole set dependent.

### What I need to keep practising
- Checking linear combinations carefully, component by component.
- Distinguishing the test for two vectors from the more general test for three or more vectors.
- Understanding why any set of more than two vectors in 2D must be linearly dependent.
- Explaining my reasoning with equations rather than giving only the classification.

### Evidence from this session
- Correctly identified `[6, 4]` as twice `[3, 2]`.
- Correctly identified `[9, 15]` as three times `[3, 5]`.
- Correctly classified `[2, 3]` and `[4, 7]` as independent after checking that no one scalar works for both components.
- Correctly identified `[1, 0]` and `[0, 1]` as independent.
- Correctly identified a set containing `[0, 0]` as dependent.
- Correctly expressed `[2, 3]` as `2[1, 0] + 3[0, 1]` and `[4, 5]` as `4[1, 0] + 5[0, 1]`.

### Still in progress
The exercise with four vectors `A = [1, 0]`, `B = [0, 1]`, `C = [2, 3]`, and `D = [1, 1]` has been assigned but not answered. I have not implemented or tested Python code for this session.

### Personal takeaway
I am beginning to understand that linear dependence is not only about one vector being a multiple of another. A vector can also be created by combining other vectors. I need to keep practising these mathematical relationships until I can identify and explain them confidently.


---

## Reflection — Vector Projection — 23 November 2026

### What I learned
- Projection extracts the part of one vector that points in the direction of another vector.
- The shadow analogy helped me understand the geometric meaning.
- I worked through projecting `[3, 4]` onto `[1, 0]` and obtained `[3, 0]`.
- I learned that the part left over after projection is perpendicular to the target direction.

### What became clearer
- The dot product tells us how strongly the vectors align.
- Dividing by the target vector's dot product with itself gives the scalar needed to scale that target vector.
- Projection is a vector result, not just a single number.

### Python work
- Reviewed a Python implementation using a reusable dot-product function.
- The proposed function checks vector dimensions and prevents projection onto a zero vector.
- The expected output for the worked example is `[3.0, 0.0]`.

### Evidence and limits
- The mathematical example was worked through in the lesson.
- Python code was supplied, but I have not yet confirmed saving and running `vector_projection.py` locally. Therefore, I am not recording a successful execution or test yet.

### What I should do next
- Run the projection implementation and check its output.
- Test a projection onto a vector that is not aligned with the horizontal axis.
- Continue to Gram-Schmidt after verifying the projection code.

### Personal takeaway
Projection makes the idea of vector direction more concrete: it lets me isolate how much of one vector lies along another direction. I should connect the formula to the geometric picture and verify the implementation with more than one example.
