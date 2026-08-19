# Day 10: Key Learnings

## Dictionaries

I learned that Python dictionaries store data in key-value pairs. They are
mutable, which means their contents can be changed after creation.

Dictionaries provide efficient average-case lookup for values using keys.

## Dictionary Methods

I practiced important dictionary methods:

- `get()` — safely access a value
- `keys()` — return dictionary keys
- `values()` — return dictionary values
- `items()` — return key-value pairs
- `update()` — add or update dictionary data
- `pop()` — remove an item

## Nested Dictionaries

I learned how to store dictionaries inside other dictionaries to represent
complex structured data.

For example, a student dictionary can contain student information and
another dictionary containing grades for different subjects.

## JSON

I learned how to work with JSON files using Python's `json` module.

- `json.dump()` is used to write Python data to a JSON file.
- `json.load()` is used to read JSON data from a file.

JSON is useful for persistent storage and exchanging structured data.

## Dictionary Comprehensions

I learned that dictionary comprehensions provide a short and readable way
to create dictionaries.

Example:

```python
numbers = [1, 2, 3, 4, 5]

squares = {number: number ** 2 for number in numbers}