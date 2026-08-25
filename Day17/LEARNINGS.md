# Learnings - Text Embeddings & Semantic Search

## Overview

In this task, I learned how text embeddings convert text into numerical
vectors that capture semantic meaning. I also implemented semantic
similarity, semantic search, and document similarity using Python.

---

## 1. What Are Embeddings?

Embeddings are numerical vector representations of text.

They convert words, sentences, or documents into high-dimensional vectors
so that text with similar meanings can be represented by similar vectors.

For example:

- "dog" and "puppy" should have high semantic similarity.
- "dog" and "car" should have lower semantic similarity.

---

## 2. How Embeddings Work

An embedding model processes text using a neural network and converts it
into a numerical vector.

The vectors are positioned in a high-dimensional space.

Texts with similar meanings tend to be closer together in this space,
while unrelated texts tend to be farther apart.

---

## 3. Embedding Model

For the practical implementation, I used:

- Sentence Transformers
- `all-MiniLM-L6-v2`

The model generates 384-dimensional sentence embeddings.

Example:

```text
Embedding shape: (3, 384)