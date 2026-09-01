from datetime import datetime
from collections import defaultdict
import time


# ============================================================
# PERFORMANCE TRACKER
# ============================================================

class PerformanceTracker:

    def __init__(self):
        self.tool_usage = defaultdict(int)
        self.successful_calls = 0
        self.failed_calls = 0
        self.total_cost = 0.0
        self.total_calls = 0

    def track(self, tool_name, success=True, cost=0.0):

        self.tool_usage[tool_name] += 1
        self.total_calls += 1
        self.total_cost += cost

        if success:
            self.successful_calls += 1
        else:
            self.failed_calls += 1

    def report(self):

        success_rate = (
            self.successful_calls / self.total_calls * 100
            if self.total_calls > 0 else 0
        )

        average_cost = (
            self.total_cost / self.total_calls
            if self.total_calls > 0 else 0
        )

        print("\n" + "=" * 60)
        print("AGENT PERFORMANCE REPORT")
        print("=" * 60)

        print("\nTool Usage Frequency:")

        for tool, count in self.tool_usage.items():
            print(f"- {tool}: {count}")

        print(f"\nTotal Tool Calls: {self.total_calls}")
        print(f"Successful Calls: {self.successful_calls}")
        print(f"Failed Calls: {self.failed_calls}")
        print(f"Success Rate: {success_rate:.2f}%")
        print(f"Average Cost: ${average_cost:.4f}")

        print("=" * 60)


# ============================================================
# CONVERSATION MEMORY
# ============================================================

class ConversationMemory:

    def __init__(self):
        self.history = []

    def add(self, role, message):

        self.history.append({
            "role": role,
            "message": message
        })

    def get_context(self):

        return self.history


# ============================================================
# TOOLS
# ============================================================

class ResearchTools:

    def __init__(self, tracker):
        self.tracker = tracker

    def rag_search(self, query):

        try:

            documents = {
                "rag": (
                    "RAG stands for Retrieval-Augmented Generation. "
                    "It retrieves relevant information before generating answers."
                ),
                "langchain": (
                    "LangChain is a framework used for building "
                    "LLM applications, agents, and tool-based workflows."
                ),
                "vector": (
                    "Vector databases store embeddings and support "
                    "semantic similarity search."
                )
            }

            for key, value in documents.items():

                if key in query.lower():

                    self.tracker.track(
                        "RAG Search",
                        True,
                        0.001
                    )

                    return value

            self.tracker.track(
                "RAG Search",
                False,
                0.001
            )

            return "No relevant document found."

        except Exception as e:

            self.tracker.track(
                "RAG Search",
                False
            )

            return f"RAG Error: {str(e)}"

    def web_search(self, query):

        try:

            results = {
                "rag": (
                    "Recent AI systems increasingly use RAG architectures "
                    "to improve factual accuracy."
                ),
                "langchain": (
                    "LangChain continues to be widely used for "
                    "developing AI agents and LLM applications."
                )
            }

            for key, value in results.items():

                if key in query.lower():

                    self.tracker.track(
                        "Web Search",
                        True,
                        0.002
                    )

                    return value

            self.tracker.track(
                "Web Search",
                True,
                0.002
            )

            return f"Recent search completed for: {query}"

        except Exception as e:

            self.tracker.track(
                "Web Search",
                False
            )

            return f"Web Search Error: {str(e)}"

    def calculator(self, expression):

        try:

            result = eval(
                expression,
                {"__builtins__": {}}
            )

            self.tracker.track(
                "Calculator",
                True,
                0.0001
            )

            return result

        except Exception as e:

            self.tracker.track(
                "Calculator",
                False
            )

            return f"Calculator Error: {str(e)}"

    def get_datetime(self):

        try:

            result = datetime.now().strftime(
                "%A, %d %B %Y - %I:%M %p"
            )

            self.tracker.track(
                "DateTime",
                True,
                0.0
            )

            return result

        except Exception as e:

            self.tracker.track(
                "DateTime",
                False
            )

            return f"DateTime Error: {str(e)}"


# ============================================================
# MULTI-TOOL RESEARCH ASSISTANT
# ============================================================

class ResearchAssistant:

    def __init__(self):

        self.tracker = PerformanceTracker()
        self.memory = ConversationMemory()
        self.tools = ResearchTools(self.tracker)

    def research(self, query):

        print("\n" + "=" * 60)
        print("MULTI-TOOL RESEARCH ASSISTANT")
        print("=" * 60)

        print(f"\nUser Query: {query}")

        self.memory.add("user", query)

        # Step 1: RAG Search
        print("\n[1] Searching internal documents...")

        rag_result = self.tools.rag_search(query)

        print("RAG Result:")
        print(rag_result)

        # Step 2: Web Search
        print("\n[2] Searching for recent updates...")

        web_result = self.tools.web_search(query)

        print("Web Result:")
        print(web_result)

        # Step 3: Date/Time
        print("\n[3] Getting current date and time...")

        current_time = self.tools.get_datetime()

        print(current_time)

        # Final Answer
        answer = (
            f"\nInternal Document Information:\n{rag_result}\n\n"
            f"Recent Web Information:\n{web_result}\n\n"
            f"Research completed on: {current_time}"
        )

        self.memory.add("assistant", answer)

        print("\nFINAL RESEARCH ANSWER")
        print("-" * 60)
        print(answer)

        # Show Memory
        print("\nCONVERSATION MEMORY")
        print("-" * 60)

        for item in self.memory.get_context():
            print(
                f"{item['role'].upper()}: "
                f"{item['message'][:100]}..."
            )

        # Performance Report
        self.tracker.report()


# ============================================================
# RUN
# ============================================================

if __name__ == "__main__":

    assistant = ResearchAssistant()

    assistant.research(
        "Find information about RAG in my documents, "
        "then search web for recent updates about RAG."
    )