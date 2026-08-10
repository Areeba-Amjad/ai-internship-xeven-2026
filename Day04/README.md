 Day 04 – Operators & Type Conversion

## Overview

Day 04 focused on Python operators, type conversion, logical expressions, operator precedence, and error handling.

## Topics Covered

* Logical operators: `and`, `or`, `not`
* Comparison operators
* Arithmetic operators
* Type conversion
* Operator precedence
* Input validation
* Error handling

## Task 1: Advanced Login System

The Advanced Login System validates the following requirements:

* Username must contain at least 5 characters.
* Password must contain at least 8 characters.
* User must be at least 18 years old.

The program displays specific error messages when the requirements are not met. Access is granted only when all conditions are satisfied.

**File:** `login_system.py`

## Task 2: Multi-Operation Calculator

The Multi-Operation Calculator accepts two numbers and performs different mathematical operations.

Supported operations:

* Addition (`+`)
* Subtraction (`-`)
* Multiplication (`*`)
* Division (`/`)
* Modulus (`%`)
* Exponentiation (`**`)

The program also handles division by zero and invalid operations.

**File:** `multi_operation_calculator.py`

## Error Handling

Both programs were tested with different inputs to make sure invalid values are handled correctly.

Examples of tested cases:

* Short username
* Short password
* Age below 18
* Invalid operation
* Division by zero
* Valid numeric inputs

## Learning Outcomes

During Day 04, I learned how Python operators are used for calculations and decision-making. I also practiced converting values between different data types using functions such as `int()`, `float()`, and `str()`.

I improved my understanding of logical operators, comparison operators, arithmetic operators, operator precedence, input validation, and error handling.

## Files

```text
Day04/
├── login_system.py
├── multi_operation_calculator.py
├── Day04_Operators_Type_Conversion.ipynb
└── README.md
```

## Conclusion

Day 04 provided practical experience with Python operators and type conversion. The login system and calculator helped me understand how operators, conditions, input validation, and error handling can be combined to create reliable Python programs.
