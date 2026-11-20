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
- Read and run the Python functions in `code/vectors.py` one at a time.
- Learn how cosine similarity compares embedding directions.

## Key takeaway

Linear algebra gives machine learning a way to represent and work with numerical data. Vectors hold ordered numbers, matrices organize numbers and transform vectors, and operations such as dot products help compare and process them. I should understand the small examples first before moving to more advanced AI applications.


## Personal Reflection

- The dot product measures how two vectors relate to each other. It is especially useful in AI when comparing embeddings.
The formula: u.v = (u1*v1 ) + (u2*v2)

- In AI, words, sentences, images, and other data can be represented as numerical vectors called embeddings.

Cosine similarity helps us measure how similar two embedding directions are.

Its formula is:
\[
\text{Similarity}(u,v)=
\frac{u\cdot v}{\|u\|\times\|v\|}
\]



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

- Implement Mean Squared Error (MSE) in pure Python.
- Calculate MSE by hand for a few small examples.
- Understand how a loss value relates to model training.
- Later, learn how backpropagation uses the loss to help update weights and biases.

### Evidence and limits

- Ran `two_layer_network.py` successfully.
- Verified output: `[13, 4]`.
- The network uses fixed weights and biases. It is a forward-pass demonstration, not a trained model.
- MSE has been introduced conceptually only; no loss function, backpropagation, or parameter update has been implemented yet.
