from langchain_core.tools import tool
from datetime import datetime
import math


# ============================================================
# TOOL 1: CALCULATOR
# ============================================================

@tool
def calculator(expression: str) -> str:
    """
    Calculates a mathematical expression.
    Example input: "23 * 45"
    """
    try:
        allowed_names = {
            "sqrt": math.sqrt,
            "pow": pow,
            "abs": abs,
            "round": round
        }

        result = eval(
            expression,
            {"__builtins__": {}},
            allowed_names
        )

        return f"Calculation Result: {result}"

    except Exception as e:
        return f"Calculator Error: {str(e)}"


# ============================================================
# TOOL 2: WEB SEARCH (DEMO VERSION)
# ============================================================

@tool
def web_search(query: str) -> str:
    """
    Searches the web for information about a query.
    Returns summarized search results.
    """

    try:
        demo_results = {
            "1000": (
                "1000 is a natural number. It is commonly used to represent "
                "one thousand and is an important milestone in mathematics."
            ),
            "ai": (
                "Artificial Intelligence (AI) is a field of computer science "
                "focused on creating systems that can perform intelligent tasks."
            ),
            "machine learning": (
                "Machine Learning is a subset of AI where systems learn patterns "
                "from data to make predictions or decisions."
            )
        }

        query_lower = query.lower()

        for key, value in demo_results.items():
            if key in query_lower:
                return f"Web Search Result: {value}"

        return (
            f"Web Search Result for '{query}': "
            "No exact demo result found, but the search tool executed successfully."
        )

    except Exception as e:
        return f"Web Search Error: {str(e)}"


# ============================================================
# TOOL 3: RAG DOCUMENT SEARCH
# ============================================================

@tool
def rag_search(query: str) -> str:
    """
    Searches internal documents and returns relevant information.
    """

    try:
        documents = {
            "rag": (
                "RAG stands for Retrieval-Augmented Generation. "
                "It retrieves relevant documents before generating an answer."
            ),
            "langchain": (
                "LangChain is a framework for building applications "
                "using Large Language Models and tools."
            ),
            "vector database": (
                "A vector database stores embeddings and enables "
                "semantic similarity search."
            ),
            "agent": (
                "An AI agent can reason about a task and use tools "
                "to achieve a goal."
            )
        }

        query_lower = query.lower()

        for key, value in documents.items():
            if key in query_lower:
                return f"RAG Result: {value}"

        return "RAG Result: No relevant document found."

    except Exception as e:
        return f"RAG Error: {str(e)}"


# ============================================================
# TOOL 4: DATE & TIME
# ============================================================

@tool
def get_current_datetime(_: str = "") -> str:
    """
    Returns the current date and time.
    """

    try:
        return datetime.now().strftime(
            "%A, %d %B %Y - %I:%M %p"
        )

    except Exception as e:
        return f"DateTime Error: {str(e)}"


# ============================================================
# SIMPLE MULTI-TOOL AGENT DEMO
# ============================================================

def run_multi_tool_demo():

    print("\n" + "=" * 60)
    print("MULTI-TOOL RESEARCH ASSISTANT")
    print("=" * 60)

    # Query 1
    print("\nQuery 1: Calculate 23 * 45")
    result = calculator.invoke({"expression": "23 * 45"})
    print(result)

    # Query 2
    print("\nQuery 2: Search information about AI")
    result = web_search.invoke({"query": "AI"})
    print(result)

    # Query 3
    print("\nQuery 3: Find RAG information from documents")
    result = rag_search.invoke({"query": "What is RAG?"})
    print(result)

    # Query 4
    print("\nQuery 4: Get current date and time")
    result = get_current_datetime.invoke({"_": ""})
    print(result)

    print("\n" + "=" * 60)
    print("ALL TOOLS EXECUTED SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    run_multi_tool_demo()