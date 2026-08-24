
# Day 16 Learnings: LangChain Setup & First Chains

## 1. What is LangChain?

LangChain is a framework for developing applications powered by
Large Language Models (LLMs).

It provides reusable components that make it easier to build workflows
involving prompts, models, document processing, retrieval, tools, and
agents.

## 2. Core Components

I learned about the main components of LangChain:

### Models

Models are responsible for generating responses or performing
language-related tasks.

### Prompts

Prompt templates provide reusable instructions with dynamic variables.

### Chains

Chains connect multiple components together to create a workflow.

### Memory

Memory can be used to maintain information across interactions in
conversational applications.

## 3. LCEL

LangChain Expression Language (LCEL) provides a simple way to connect
LangChain components.

The pipe operator `|` is used to connect components.

Example:

prompt = PromptTemplate(
    input_variables=["topic"],
    template="Explain {topic} in simple words."
)
