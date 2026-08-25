# Day 18: Text Splitters & Chunking Strategies

## Overview

Day 18 focused on document chunking and text splitters used in Retrieval-Augmented Generation (RAG) systems.

The main goal was to understand how large documents are divided into smaller chunks before embedding, storage, and retrieval.

---

## 1. Why Document Chunking Is Important

Documents are chunked for several reasons:

* LLMs have finite context windows.
* Embedding models have input-size limitations.
* Smaller chunks can improve retrieval precision.
* Chunking makes vector search more efficient.
* Relevant context can be retrieved without sending an entire document to the LLM.

A good chunk should contain enough information to preserve meaning while avoiding unnecessary content.

---

## 2. Chunking Strategies

### Fixed-Size Chunking

Fixed-size chunking divides text according to a predefined number of characters or tokens.

**Advantages:**

* Simple
* Fast
* Predictable

**Disadvantages:**

* Can split sentences or ideas
* Does not understand document structure

### Sentence-Based Chunking

Sentence-based chunking splits text at sentence boundaries.

**Advantages:**

* Preserves complete sentences
* More natural boundaries

**Disadvantages:**

* Sentence lengths vary
* Long sentences may still be too large

### Semantic Chunking

Semantic chunking uses meaning or topic changes to determine chunk boundaries.

**Advantages:**

* Better semantic coherence
* Useful for topic-rich documents

**Disadvantages:**

* More computationally expensive
* Requires semantic similarity or model-based processing

### Recursive Character Chunking

`RecursiveCharacterTextSplitter` recursively attempts larger separators before falling back to smaller ones.

It is a strong general-purpose option for RAG pipelines.

---

## 3. Chunk Size and Overlap

A practical starting range for many RAG applications is approximately 256–1024 tokens.

The exact size depends on the document and retrieval requirements.

### Small Chunks

* More precise retrieval
* Less irrelevant information
* Less surrounding context

### Large Chunks

* More surrounding context
* Better continuity
* Potentially more irrelevant information
* Lower retrieval precision in some cases

### Overlap

Overlap repeats some content between neighboring chunks.

It helps preserve information when an important sentence or concept crosses a chunk boundary.

However, excessive overlap increases the number of chunks and storage/indexing requirements.

---

## 4. LangChain Splitters

### RecursiveCharacterTextSplitter

Used as a general-purpose text splitter.

Configuration used:

```python
RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
```

### TokenTextSplitter

Used when token count needs to be controlled directly.

### MarkdownHeaderTextSplitter

Used for Markdown documents.

It preserves heading information as metadata, which is useful for structured documentation.

### PythonCodeTextSplitter

Used for Python source code so that code structure can be preserved more effectively than simple character splitting.

---

## 5. Task 1: Chunking Method Comparison

Two methods were compared:

### CharacterTextSplitter

* Chunk size: 500 characters
* Overlap: 0

### RecursiveCharacterTextSplitter

* Chunk size: 500 characters
* Overlap: 50 characters

### Finding

`RecursiveCharacterTextSplitter` provided better context preservation because it considers natural text boundaries and uses overlap.

The fixed character splitter is simpler, but it can produce less meaningful boundaries.

### Conclusion

For general RAG documents, `RecursiveCharacterTextSplitter` is a better starting point than simple fixed-size character splitting.

---

## 6. Task 2: Optimal Chunk Size Experiment

The following chunk sizes were tested:

* 200 characters
* 500 characters
* 1000 characters
* 2000 characters

The experiment measured:

* Number of chunks
* Average chunk size
* Estimated storage
* Retrieval quality
* Recommendation

### Embedding Experiment

A local TF-IDF vector representation was used as a lightweight retrieval proxy.

This avoided requiring a paid API or a large neural embedding model.

### Important Limitation

TF-IDF is not equivalent to modern semantic embedding models.

Therefore, the retrieval scores should be interpreted as comparative experiment results rather than production-level semantic retrieval benchmarks.

### Finding

Chunk size affects both retrieval behavior and storage requirements.

Smaller chunks create more retrieval units, while larger chunks reduce the number of chunks and preserve more context.

The best chunk size should be selected by evaluating the actual documents and user questions.

---

## 7. Task 3: Smart Document Processor

A reusable smart document processor was implemented.

It automatically detects:

| File Type | Splitter                                                    |
| --------- | ----------------------------------------------------------- |
| `.md`     | MarkdownHeaderTextSplitter + RecursiveCharacterTextSplitter |
| `.py`     | PythonCodeTextSplitter                                      |
| `.txt`    | RecursiveCharacterTextSplitter                              |

### Metadata Preserved

Each chunk contains metadata such as:

* `source`
* `type`
* `section`
* `chunk_id`
* `tokens`
* `overlap`

### Intelligent Overlap

Technical documents receive more overlap because code and structured technical content can depend on surrounding context.

Plain/narrative documents receive less overlap to reduce unnecessary duplication.

---

## 8. Key Lessons

1. Chunking is a fundamental step in RAG.
2. Chunk boundaries affect retrieval quality.
3. Small chunks improve precision but may lose context.
4. Large chunks preserve context but can introduce irrelevant information.
5. Overlap helps preserve context across boundaries.
6. `RecursiveCharacterTextSplitter` is a useful general-purpose splitter.
7. `TokenTextSplitter` is useful for token-based constraints.
8. `MarkdownHeaderTextSplitter` preserves document structure.
9. Metadata improves source tracking and filtering.
10. Chunk size should be evaluated experimentally.
11. Different document types require different splitting strategies.
12. There is no single chunk size that works optimally for every RAG application.

---

## 9. Final Takeaway

The main lesson from Day 18 is that chunking is not simply about cutting a document into equal pieces.

Effective chunking balances:

* Semantic coherence
* Retrieval precision
* Context preservation
* Storage efficiency
* Metadata traceability

A practical RAG pipeline can therefore follow:

```text
Document
   ↓
Document Type Detection
   ↓
Structure-Aware Splitting
   ↓
Recursive / Token Chunking
   ↓
Metadata Preservation
   ↓
Embeddings
   ↓
Vector Database
   ↓
Retrieval
   ↓
LLM Context
   ↓
Answer
```

## References

* LangChain Text Splitters:
  https://docs.langchain.com/oss/python/integrations/splitters/index

* LangChain Recursive Character Text Splitter:
  https://docs.langchain.com/oss/python/integrations/splitters/recursive_text_splitter

* LangChain Token Text Splitter:
  https://docs.langchain.com/oss/python/integrations/splitters/split_by_token

* LangChain Markdown Header Text Splitter:
  https://docs.langchain.com/oss/python/integrations/splitters/markdown_header_metadata_splitter

* McTaba Labs — Chunking Strategies for RAG:
  https://www.mctaba.com/kb/rag-chunking-strategies

* Thread Transfer — RAG Document Chunking Best Practices:
  https://thread-transfer.com/blog/2026-06-17-rag-document-chunking-best-practices/
