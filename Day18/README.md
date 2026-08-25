# Day 18: Text Splitters & Chunking Strategies

## Overview

This project explores document chunking strategies and LangChain text splitters used in Retrieval-Augmented Generation (RAG) systems.

The notebook demonstrates how document chunk size, overlap, structure, and metadata affect document processing and retrieval.

---

## Learning Objectives

* Understand why documents are chunked.
* Learn different chunking strategies.
* Understand chunk size and overlap.
* Compare fixed-size and recursive chunking.
* Use LangChain text splitters.
* Preserve document metadata.
* Build a smart document processor.
* Experiment with different chunk sizes.

---

## Tasks Completed

### Task 1 — Compare Chunking Methods

Compared:

* `CharacterTextSplitter`
* `RecursiveCharacterTextSplitter`

Configuration:

```text
CharacterTextSplitter
chunk_size = 500
overlap = 0

RecursiveCharacterTextSplitter
chunk_size = 500
overlap = 50
```

### Result

`RecursiveCharacterTextSplitter` provided better context preservation and semantic coherence because it considers natural separators and uses overlap.

---

### Task 2 — Optimal Chunk Size Experiment

Tested:

```text
200 characters
500 characters
1000 characters
2000 characters
```

Measured:

* Number of chunks
* Average chunk size
* Estimated storage
* Retrieval quality
* Recommended chunk size

A local TF-IDF representation was used as a lightweight retrieval proxy.

> Note: TF-IDF was used instead of a neural embedding model or paid API. Therefore, the retrieval experiment demonstrates relative behavior rather than production semantic-search performance.

---

### Task 3 — Smart Document Processor

Implemented an automatic document processor.

| Document          | Processing Method                                           |
| ----------------- | ----------------------------------------------------------- |
| Markdown `.md`    | MarkdownHeaderTextSplitter + RecursiveCharacterTextSplitter |
| Python `.py`      | PythonCodeTextSplitter                                      |
| Plain text `.txt` | RecursiveCharacterTextSplitter                              |

The processor also preserves:

* Source
* Document type
* Section
* Chunk ID
* Token count
* Overlap

---

## Technologies Used

* Python
* Jupyter Notebook
* LangChain
* `langchain-text-splitters`
* `tiktoken`
* Scikit-learn
* NumPy
* Pandas

---

## Project Structure

```text
Day18/
│
├── Day18_Text_Splitters_Chunking_Strategies.ipynb
├── README.md
└── LEARNINGS.md
```

---

## Main LangChain Components

### RecursiveCharacterTextSplitter

General-purpose text splitting with recursive separators.

### TokenTextSplitter

Token-based text splitting.

### MarkdownHeaderTextSplitter

Structure-aware Markdown splitting with header metadata.

### PythonCodeTextSplitter

Specialized splitting for Python source code.

---

## Key Concepts

### Chunking

Dividing large documents into smaller retrievable units.

### Chunk Size

Controls approximately how much text each chunk contains.

### Chunk Overlap

Repeats some content between neighboring chunks to preserve context.

### Metadata

Information describing a chunk, such as source, section, page, and chunk ID.

### Retrieval Precision

The ability of a retrieval system to return relevant information instead of unrelated content.

---

## Chunk Size Trade-Off

```text
Small Chunks
    ↓
Higher Precision
    ↓
Less Context

Large Chunks
    ↓
More Context
    ↓
Potentially Lower Precision
```

The optimal value depends on the dataset and application.

---

## RAG Pipeline

```text
Document
    ↓
Document Type Detection
    ↓
Chunking
    ↓
Metadata
    ↓
Embeddings
    ↓
Vector Database
    ↓
Similarity Search
    ↓
Retrieved Context
    ↓
LLM
    ↓
Answer
```

---

## Important Finding

There is no universally optimal chunk size.

A good chunking strategy should balance:

* Semantic coherence
* Retrieval precision
* Context preservation
* Storage requirements
* Processing cost
* Metadata traceability

For a general RAG system, `RecursiveCharacterTextSplitter` is a strong starting point.

For structured Markdown, combining `MarkdownHeaderTextSplitter` with recursive splitting provides useful section-level context.

---

## Limitations

The Task 2 retrieval experiment used TF-IDF as a local retrieval proxy.

TF-IDF is not equivalent to modern neural embedding models such as sentence-transformer embeddings or API-based embedding models.

This approach was intentionally selected to complete the experiment without requiring a paid API or GPU-based deep-learning framework.

---

## References

* [LangChain Text Splitters](https://docs.langchain.com/oss/python/integrations/splitters/index)
* [LangChain Recursive Text Splitter](https://docs.langchain.com/oss/python/integrations/splitters/recursive_text_splitter)
* [LangChain Token Text Splitter](https://docs.langchain.com/oss/python/integrations/splitters/split_by_token)
* [LangChain Markdown Header Splitter](https://docs.langchain.com/oss/python/integrations/splitters/markdown_header_metadata_splitter)
* [McTaba Labs — Chunking Strategies for RAG](https://www.mctaba.com/kb/rag-chunking-strategies)
* [Thread Transfer — RAG Document Chunking Best Practices](https://thread-transfer.com/blog/2026-06-17-rag-document-chunking-best-practices/)

---

## Status

**Day 18 — Completed**

All three required tasks were implemented and documented.
