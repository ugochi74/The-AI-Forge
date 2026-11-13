# Lesson Reflection: Linear Algebra Intuition

## What I understood

- **Vectors are coordinates for concepts:** I understood that in computer science, a vector is just an ordered list of numbers, but in AI, it represents a data point or "embedding" in multi-dimensional space.
- **The geometry of basic operations:** Vector addition combines two vectors tip-to-tail, and scalar multiplication stretches or shrinks a vector's length without changing its heading.
- **The power of the dot product:** Multiplying matching components and summing them reveals how closely aligned two vectors are. When normalized, this gives cosine similarity—the core technique used in vector databases and semantic search.
- **Neural networks as linear transformations:** A layer in a neural network ($y = Wx + b$) is essentially multiplying an input vector by a weight matrix (taking dot products with each row) and adding a bias vector.

## What I found difficult

- **Visualizing beyond 3 dimensions:** While it's easy to picture 2D or 3D vectors as arrows on paper, thinking about 768- or 1536-dimensional embedding spaces used in real LLMs takes getting used to. Realizing that the mathematical rules (addition, dot product, distance) work exactly the same in high dimensions helped resolve this.
- **Matrix dimension alignment:** Keeping track of rows and columns during matrix-vector multiplication (e.g., ensuring an $M \times N$ matrix multiplies an $N$-length vector to yield an $M$-length vector) requires careful attention to shape rules.

## What I need to practise

- Calculating dot products and matrix-vector multiplications by hand on small matrices ($2 \times 2$ and $3 \times 3$) until the arithmetic feels automatic.
- Implementing vector and matrix operations from scratch in Python without relying on NumPy to cement the underlying logic.
- Connecting vector dot products directly to how LLM attention scores and RAG cosine similarities are computed.

## Key takeaway

Linear algebra is the foundational language of AI. "Understanding" or "meaning" in modern AI models is represented as a position (vector) in space, and "reasoning" or "processing" is moving and transforming those vectors using matrices.
