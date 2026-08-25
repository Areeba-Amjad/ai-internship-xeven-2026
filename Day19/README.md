# Day 19: Prompt Engineering Mastery

## Overview

Day 19 focused on advanced Prompt Engineering techniques and practical implementation using Jupyter Notebook.

The main objective was to understand how different prompting strategies affect Large Language Model (LLM) behavior and how structured prompts can improve output reliability.

---

## Topics Covered

- Zero-Shot Prompting
- Few-Shot Prompting
- Chain-of-Thought (CoT) Prompting
- System Messages
- Prompt Patterns
- Prompt Templates
- Structured Output
- JSON Output Control
- Markdown Table Generation
- Code Generation
- Prompt Robustness Testing
- Common Prompting Pitfalls

---

## Task 1: Prompting Technique Comparison

### Selected Task

Sentiment Analysis

A dataset containing 20 labeled sentiment samples was created.

### Techniques Implemented

#### 1. Zero-Shot Prompting

The model receives only the task instructions without examples.

Best suited for:

- Simple classification
- Straightforward tasks
- General text transformation

#### 2. Few-Shot Prompting

Three examples were provided before asking the model to classify new text.

Best suited for:

- Specialized classification
- Custom categories
- Tasks where examples clarify the expected behavior

#### 3. Chain-of-Thought Prompting

The prompt encouraged careful multi-step reasoning for complex cases.

Best suited for:

- Mathematical reasoning
- Logical problems
- Multi-step analysis

### Evaluation

The notebook includes a framework for measuring:

- Accuracy
- Response speed
- Estimated token usage
- Cost
- Best use case

### API Limitation

Live API evaluation could not be completed because the configured API account returned:

`429 - insufficient_quota`

No artificial accuracy or cost values were reported.

The prompts and 20-sample evaluation dataset remain ready for testing when API quota becomes available.

---

## Task 2: Prompt Template Library

A reusable prompt template library was created for common LLM tasks.

### Templates

1. Summarization
2. Information Extraction
3. Text Generation
4. Text Analysis

Each template includes:

- System message
- User instruction
- Output format
- Constraints
- Examples

### Variables

The templates support:

```text
{text}
{format}
{constraints}
{examples}

prompt_templates.json