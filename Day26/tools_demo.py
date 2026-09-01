"""
Day 26 - LangChain Agents & Tool Calling
Local Tool Calling Demo

This demo works WITHOUT an OpenAI API key.
"""

# -----------------------------
# TOOL 1: Calculator
# -----------------------------

def calculator(operation: str, a: float, b: float) -> float:
    """
    Performs basic mathematical calculations.

    Parameters:
        operation: add, subtract, multiply, divide
        a: first number
        b: second number

    Returns:
        Calculation result
    """

    if operation == "add":
        return a + b

    elif operation == "subtract":
        return a - b

    elif operation == "multiply":
        return a * b

    elif operation == "divide":
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    else:
        raise ValueError("Unknown operation.")


# -----------------------------
# TOOL 2: Greeting
# -----------------------------

def greeting(name: str) -> str:
    """
    Returns a personalized greeting.
    """
    return f"Hello {name}! Welcome to the Day 26 Agent Demo."


# -----------------------------
# TOOL 3: Word Counter
# -----------------------------

def word_count(text: str) -> int:
    """
    Counts the number of words in a text.
    """
    return len(text.split())


# -----------------------------
# TOOL REGISTRY
# -----------------------------

tools = {
    "calculator": calculator,
    "greeting": greeting,
    "word_count": word_count
}


# -----------------------------
# SIMPLE LOCAL AGENT
# -----------------------------

def simple_agent(task: str):

    print("\n" + "=" * 60)
    print("AGENT STARTED")
    print("=" * 60)

    print(f"User Query: {task}")

    task_lower = task.lower()

    # Planning
    print("\n[1] Planning...")
    
    # Tool selection
    if "calculate" in task_lower or "divide" in task_lower:
        selected_tool = "calculator"

    elif "hello" in task_lower or "greet" in task_lower:
        selected_tool = "greeting"

    elif "count" in task_lower and "word" in task_lower:
        selected_tool = "word_count"

    else:
        print("No suitable tool found.")
        return

    print(f"[2] Tool Selected: {selected_tool}")

    # Tool execution
    print("[3] Executing Tool...")

    if selected_tool == "calculator":

        result = tools[selected_tool](
            operation="divide",
            a=500,
            b=25
        )

    elif selected_tool == "greeting":

        result = tools[selected_tool]("Areeba")

    elif selected_tool == "word_count":

        result = tools[selected_tool](
            "LangChain agents can use tools"
        )

    # Observation
    print(f"[4] Tool Result: {result}")

    # Final answer
    print("[5] Integrating Result...")

    print("\nFinal Answer:")
    print(result)

    print("=" * 60)


# -----------------------------
# RUN AGENT
# -----------------------------

if __name__ == "__main__":

    simple_agent(
        "Calculate 500 divided by 25"
    )