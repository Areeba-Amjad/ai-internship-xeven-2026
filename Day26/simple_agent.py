"""
Day 26 - Simple ReAct Style Agent
Works without OpenAI API credits
"""


# ==============================
# TOOLS
# ==============================

def calculator(expression):
    """Performs basic arithmetic calculations."""
    try:
        return eval(expression, {"__builtins__": {}}, {})
    except Exception:
        return "Invalid calculation"


def get_weather(city):
    """Returns simulated weather information."""

    weather_data = {
        "lahore": "Sunny, 32°C",
        "karachi": "Warm, 30°C",
        "islamabad": "Cloudy, 25°C"
    }

    return weather_data.get(
        city.lower(),
        "Weather data not available"
    )


def word_counter(text):
    """Counts words in a sentence."""
    return len(text.split())


# ==============================
# REACT STYLE AGENT
# ==============================

def react_agent(query):

    print("\n" + "=" * 60)
    print("REACT STYLE AGENT")
    print("=" * 60)

    print(f"\nUser Query: {query}")

    query_lower = query.lower()

    # THOUGHT
    print("\nThought:")
    print("I need to understand the request and select the right tool.")

    # ACTION + OBSERVATION
    if "weather" in query_lower:

        city = "lahore"

        print("\nAction:")
        print(f"Using Weather Tool for {city}")

        result = get_weather(city)

        print("\nObservation:")
        print(result)

    elif "calculate" in query_lower:

        expression = "125 * 8"

        print("\nAction:")
        print(f"Using Calculator Tool: {expression}")

        result = calculator(expression)

        print("\nObservation:")
        print(result)

    elif "count" in query_lower and "word" in query_lower:

        text = "LangChain agents can use multiple tools"

        print("\nAction:")
        print("Using Word Counter Tool")

        result = word_counter(text)

        print("\nObservation:")
        print(result)

    else:
        result = "No suitable tool found."

    # FINAL ANSWER
    print("\nFinal Answer:")
    print(result)

    print("\n" + "=" * 60)


# ==============================
# RUN AGENT
# ==============================

if __name__ == "__main__":
    react_agent("Calculate 125 multiplied by 8")