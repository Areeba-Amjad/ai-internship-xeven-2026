# Day 26: AI Agents, Tools & ReAct Architecture

## Overview

Day 26 focused on understanding and implementing AI Agents, custom tools, ReAct-style reasoning, multi-tool workflows, conversation memory, and agent performance tracking.

The practical work demonstrates how an AI agent can select and use different tools to solve tasks instead of relying only on a language model.

## Learning Objectives

* Understand AI Agents and agent-based workflows
* Build custom tools using the `@tool` decorator
* Implement calculator, web search, RAG search, and date/time tools
* Understand ReAct architecture
* Build multi-step agent workflows
* Add error handling and retry logic
* Implement maximum iteration limits
* Create a multi-tool research assistant
* Add conversation memory
* Track agent performance

---

## Task 1: Custom Tools

Custom tools were created using the LangChain `@tool` decorator.

### Tools Implemented

#### 1. Calculator Tool

Accepts a mathematical expression and returns the calculated result.

Example:

```text
23 * 45
```

Result:

```text
1035
```

Features:

* Typed parameters
* Tool description
* Error handling
* Mathematical operations

#### 2. Web Search Tool

A demo web search tool was implemented to simulate searching and returning summarized information.

Features:

* Accepts a search query
* Returns summarized results
* Handles unknown queries
* Includes error handling

#### 3. RAG Search Tool

A simple Retrieval-Augmented Generation search tool was created to search internal document knowledge.

Topics included:

* RAG
* LangChain
* Vector Databases
* AI Agents

#### 4. Date and Time Tool

Returns the current system date and time.

---

## Task 2: ReAct Agent

A ReAct-style agent was implemented.

ReAct stands for:

**Reasoning + Acting**

The agent follows the workflow:

```text
User Query
     ↓
Thought
     ↓
Action
     ↓
Tool Selection
     ↓
Observation
     ↓
Next Thought
     ↓
Final Answer
```

### Example Query

```text
What's 23 * 45? Then search for information on that number.
```

### Agent Workflow

1. Understand the query
2. Select Calculator Tool
3. Calculate the result
4. Observe the result
5. Select Web Search Tool
6. Search information about the result
7. Generate final answer

### Additional Features

* Multiple tool usage
* Verbose reasoning output
* Tool selection tracking
* Maximum iteration limits
* Invalid tool handling
* Retry logic
* Error handling

---

## Task 3: Multi-Tool Research Assistant

A Multi-Tool Research Assistant was developed that combines multiple tools.

### Available Tools

* RAG Search
* Web Search
* Calculator
* Date and Time

### Workflow

```text
User Query
     ↓
Search Internal Documents
     ↓
Retrieve Relevant Information
     ↓
Search Recent Information
     ↓
Use Additional Tools if Required
     ↓
Combine Results
     ↓
Final Research Answer
```

### Example Query

```text
Find information about RAG in my documents, then search web for recent updates about RAG.
```

The assistant first retrieves information from internal documents and then searches for additional information.

---

## Conversation Memory

A simple conversation memory system was implemented.

The agent stores:

* User queries
* Assistant responses

This allows the system to maintain conversation context and refer to previous interactions.

---

## Agent Performance Tracking

A performance tracker was implemented to monitor tool usage.

Metrics include:

* Tool usage frequency
* Total tool calls
* Successful calls
* Failed calls
* Success rate
* Total estimated cost
* Average cost per tool call

### Example Metrics

```text
Tool Usage Frequency:
- RAG Search: 1
- Web Search: 1
- DateTime: 1

Total Tool Calls: 3
Successful Calls: 3
Failed Calls: 0
Success Rate: 100%

Average Cost: Calculated per tool call
```

---

## Files Created

```text
Day26/
│
├── .env
├── .gitignore
├── agent_basics.py
├── tools_demo.py
├── simple_agent.py
├── multi_tool_agent.py
├── react_agent_advanced.py
├── research_assistant.py
├── README.md
└── LEARNINGS.md
```

---

## Technologies Used

* Python
* LangChain
* LangChain Core
* OpenAI API
* Python Decorators
* Custom Tools
* ReAct Architecture
* RAG Concepts

---

## Key Concepts

### AI Agent

An AI Agent is a system capable of reasoning about a task, selecting appropriate tools, executing actions, and generating a final response.

### Tool

A tool provides an agent with an external capability such as:

* Calculation
* Search
* Database retrieval
* API interaction
* Date and time retrieval

### ReAct

ReAct combines reasoning and action.

The agent repeatedly:

```text
Think → Act → Observe → Think → Answer
```

### Multi-Tool Agent

A multi-tool agent can choose between multiple available tools depending on the user's request.

### Memory

Memory allows an agent to store previous interactions and maintain conversation context.

### Performance Monitoring

Performance tracking helps evaluate agent efficiency, reliability, tool usage, success rate, and estimated cost.

---

## Conclusion

Day 26 demonstrated the practical implementation of AI Agents and agent-based workflows. Custom tools were developed and integrated into ReAct-style workflows. A Multi-Tool Research Assistant was also created with memory and performance tracking.

This work provides a foundation for building more advanced autonomous AI agents capable of reasoning, planning, selecting tools, retrieving information, and completing complex multi-step tasks.
