from langchain_core.tools import tool
import time


# ============================================================
# TOOLS
# ============================================================

@tool
def calculator(expression: str) -> str:
    """Calculate a mathematical expression."""

    try:
        # Simple safe evaluation for demo purposes
        allowed_chars = "0123456789+-*/(). "

        if not all(char in allowed_chars for char in expression):
            return "Error: Invalid mathematical expression."

        result = eval(expression, {"__builtins__": {}})
        return str(result)

    except Exception as e:
        return f"Calculator Error: {str(e)}"


@tool
def web_search(query: str) -> str:
    """Search for summarized information about a query."""

    try:
        database = {
            "1035": (
                "1035 is a natural number. "
                "It comes after 1034 and before 1036."
            ),
            "1000": (
                "1000 is one thousand, an important number "
                "commonly used in mathematics and counting."
            ),
            "ai": (
                "Artificial Intelligence enables machines "
                "to perform tasks that normally require human intelligence."
            )
        }

        query = query.lower()

        for key, value in database.items():
            if key in query:
                return value

        return f"Search completed for: {query}. No exact result found."

    except Exception as e:
        return f"Web Search Error: {str(e)}"


# ============================================================
# ADVANCED REACT AGENT
# ============================================================

class ReActAgent:

    def __init__(self, max_iterations=5, max_retries=2):
        self.max_iterations = max_iterations
        self.max_retries = max_retries
        self.tools_used = []

    def execute_tool(self, tool_name, tool_input):

        for attempt in range(self.max_retries):

            try:

                if tool_name == "calculator":
                    self.tools_used.append(tool_name)

                    return calculator.invoke(
                        {"expression": tool_input}
                    )

                elif tool_name == "web_search":
                    self.tools_used.append(tool_name)

                    return web_search.invoke(
                        {"query": tool_input}
                    )

                else:
                    return f"Invalid Tool Usage: {tool_name}"

            except Exception as e:

                print(
                    f"Tool failed. Retry "
                    f"{attempt + 1}/{self.max_retries}"
                )

                time.sleep(1)

        return "Tool execution failed after maximum retries."

    def run(self, query):

        print("\n" + "=" * 60)
        print("ADVANCED REACT AGENT")
        print("=" * 60)

        print(f"\nUser Query: {query}")

        iteration = 0

        # ------------------------------------------------
        # STEP 1: REASONING
        # ------------------------------------------------

        iteration += 1

        if iteration > self.max_iterations:
            return "Maximum iterations reached."

        print("\nThought:")
        print(
            "The query requires a calculation first, "
            "then information about the calculated result."
        )

        # ------------------------------------------------
        # STEP 2: ACTION - CALCULATOR
        # ------------------------------------------------

        print("\nAction:")
        print("Using Calculator Tool")

        calculation = self.execute_tool(
            "calculator",
            "23 * 45"
        )

        print("\nObservation:")
        print(calculation)

        # ------------------------------------------------
        # STEP 3: SECOND REASONING
        # ------------------------------------------------

        iteration += 1

        if iteration > self.max_iterations:
            return "Maximum iterations reached."

        print("\nThought:")
        print(
            "The calculation is complete. "
            "Now I need to search information about the result."
        )

        # ------------------------------------------------
        # STEP 4: ACTION - WEB SEARCH
        # ------------------------------------------------

        print("\nAction:")
        print("Using Web Search Tool")

        search_result = self.execute_tool(
            "web_search",
            str(calculation)
        )

        print("\nObservation:")
        print(search_result)

        # ------------------------------------------------
        # FINAL ANSWER
        # ------------------------------------------------

        print("\nFinal Answer:")

        final_answer = (
            f"23 × 45 = {calculation}. "
            f"Information: {search_result}"
        )

        print(final_answer)

        print("\nTools Used:", self.tools_used)
        print("=" * 60)


# ============================================================
# RUN AGENT
# ============================================================

if __name__ == "__main__":

    agent = ReActAgent(
        max_iterations=5,
        max_retries=2
    )

    agent.run(
        "What's 23 * 45? Then search for information on that number."
    )