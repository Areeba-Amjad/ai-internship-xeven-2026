# Day 15 — Introduction to Large Language Models

## Overview

Day 15 focused on understanding Large Language Models (LLMs), their architecture, major providers, important API parameters, practical applications, limitations, and basic chatbot development.

## Research Topics

The following topics were studied:

- Large Language Models (LLMs)
- Transformer architecture
- Attention mechanism
- Pre-training and fine-tuning
- OpenAI GPT models
- Anthropic Claude
- Google Gemini
- Tokens
- Context windows
- Temperature
- API parameters
- LLM use cases
- LLM limitations

## Research Sources

Research was conducted using:

- ChatGPT
- Google Gemini
- Anthropic Claude
- "Attention Is All You Need" — Vaswani et al.
- Google Cloud Generative AI / LLM resources

## Afternoon Session — API Integration

### Task 1: OpenAI API Setup

The following steps were implemented:

- Installed `openai` and `python-dotenv`
- Configured environment variables
- Created a `.env` file for the API key
- Added `.env` to `.gitignore`
- Created an OpenAI client
- Tested a basic API request
- Implemented API error handling
- Examined token usage where available

### API Limitation

The live API request returned:

`429 RateLimitError — insufficient_quota`

The account did not have available API quota. Therefore, live API execution could not be completed without enabling paid API usage.

The limitation was documented and offline simulations were used for parameter experimentation.

## Task 2: Parameter Exploration

The following parameters were explored:

- Temperature
- Maximum output tokens
- Top-p
- Frequency penalty
- Presence penalty

Offline simulations were created to demonstrate:

- Different temperature behaviors
- Output length limitations
- Focused vs diverse sampling
- Parameter effects and use cases

A comparison table was also created.

## Task 3: Simple Chatbot

An offline chatbot was implemented with:

- Interactive user input
- Response generation
- Chatbot personality
- Conversation history
- Context awareness
- Input validation
- Error handling
- Exit functionality

The chatbot can demonstrate basic questions related to:

- Python
- LLMs
- Data Science

## Security

The API key was stored in `.env` and `.env` was added to `.gitignore`.

**API keys must never be committed to GitHub.**

## Billing

Billing and cost calculation were intentionally excluded because paid API usage was not available for this assignment.

## Technologies Used

- Python
- Jupyter Notebook
- OpenAI Python SDK
- python-dotenv
- Pandas
- Git
- GitHub

## Conclusion

Day 15 provided practical experience with LLM concepts, API integration, parameter experimentation, error handling, and chatbot development. The project also demonstrated how to safely handle API credentials and document limitations when live API access is unavailable.