"""
Day 26: LangChain Agents Fundamentals
"""

print("=" * 60)
print("LANGCHAIN AGENTS FUNDAMENTALS")
print("=" * 60)


# What is an Agent?

print("\n1. WHAT IS AN AGENT?")
print("""
An AI Agent is an LLM-powered system that can:
- Understand a task
- Make decisions
- Select appropriate tools
- Execute actions
- Observe results
- Repeat steps if necessary
""")


# ReAct Framework

print("\n2. REACT FRAMEWORK")
print("""
ReAct = Reasoning + Acting

The agent follows:

Thought → What should I do?
Action → Which tool should I use?
Observation → What result did I get?
Thought → Do I need another action?
Final Answer → Respond to user
""")


# Agent Loop

print("\n3. AGENT LOOP")
print("""
User Query
    ↓
Planning
    ↓
Tool Selection
    ↓
Tool Execution
    ↓
Observe Result
    ↓
Integrate Result
    ↓
Final Answer
""")


# Agent Types

print("\n4. AGENT TYPES")

agent_types = {
    "Zero-Shot Agent":
        "Selects tools based on task description without examples.",

    "Conversational Agent":
        "Maintains conversation history and context.",

    "Structured Tool Agent":
        "Uses tools with structured inputs and parameters.",

    "OpenAI Functions Agent":
        "Uses OpenAI function/tool calling capabilities."
}

for agent, description in agent_types.items():
    print(f"\n{agent}:")
    print(description)


# Challenges

print("\n5. AGENT CHALLENGES")

challenges = [
    "Wrong tool selection",
    "Infinite loops",
    "High API costs",
    "Slow execution",
    "Tool execution failures",
    "Incorrect interpretation of results"
]

for i, challenge in enumerate(challenges, 1):
    print(f"{i}. {challenge}")