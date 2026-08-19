# Day 12: Functions in Python - Learnings

## What I Learned

Today I learned about functions in Python and how they help make programs reusable, organized, and easier to maintain.

## Function Definition

- Functions are defined using the `def` keyword.
- Parameters allow functions to receive input values.
- The `return` statement sends a value back to the caller.
- A function without a return statement returns `None`.

## Function Arguments

I learned about different types of arguments:

- Positional arguments
- Keyword arguments
- Default parameters
- Argument unpacking using `*` and `**`

## Variable Scope

I learned the difference between:

- Local variables
- Global variables
- The `global` keyword
- Variable lifetime

## Function Design Principles

Good functions should:

- Follow the Single Responsibility Principle.
- Have descriptive names.
- Include useful docstrings.
- Be reusable and easy to understand.
- Avoid unnecessary code duplication.

## Practical Implementation

I implemented three practical tasks:

### Task 1: Math Utility Library

Created functions for:

- `calculate_average()`
- `find_median()`
- `get_standard_deviation()`

The functions also include input validation and optional rounding precision.

### Task 2: Text Processing Functions

Created functions for:

- `count_words()`
- `extract_emails()`
- `remove_punctuation()`
- `title_case()`
- `process_text()`

I also practiced returning multiple values using tuples.

### Task 3: Validation Function Suite

Created validation functions for:

- Email
- Phone number
- Date
- Password

Each validator returns:

```python
(is_valid, error_message)

## Additional Learning

### Dunder / Magic Methods

- Dunder methods are special Python methods that start and end with double underscores.
- They allow Python objects to work with built-in Python operations.
- Learned common methods such as `__init__()`, `__str__()`, `__len__()`, and `__add__()`.
- Practiced implementing these methods using custom classes.

### Functions vs Methods

- A function is a reusable block of code that can be called independently.
- A method is a function associated with an object or class.
- Learned the difference between functions such as `len()` and methods such as `append()`.
- Practiced both functions and methods with practical Python examples.

### Key Takeaway

Understanding functions, methods, and dunder methods helps in writing reusable, organized, and object-oriented Python programs.