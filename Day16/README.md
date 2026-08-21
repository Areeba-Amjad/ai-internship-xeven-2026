# Day 16: LangChain Setup & First Chains

## Overview

Day 16 focused on learning the fundamentals of LangChain and building
basic LLM application workflows.

The main topics covered were LangChain concepts, LCEL, PromptTemplate,
document loaders, and document-based Question Answering.

## Topics Covered

- What is LangChain?
- Core LangChain components
- Models
- Prompt Templates
- Chains
- Memory
- LangChain Expression Language (LCEL)
- LCEL pipe (`|`) operator
- Document loaders
- TextLoader
- PyPDFLoader
- WebBaseLoader
- CSVLoader
- Generic document loader function
- Document Q&A workflow
- Handling long documents
- Context limitations

## Tasks Completed

### Task 1: LangChain Installation & Setup

- Installed LangChain packages.
- Explored PromptTemplate.
- Created reusable prompt templates.
- Learned about LCEL.
- Built the first LCEL chain using:

```text
PromptTemplate → Model → OutputParser