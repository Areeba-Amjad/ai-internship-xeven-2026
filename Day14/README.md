# Day 14: Week 2 Review & Mini-Project

## Overview

Day 14 focused on reviewing Python data structures covered during Week 2 and applying those concepts to a practical Contact Management System.

## Task 1: Data Structures Cheat Sheet

The first task compared four important Python data structures:

* List
* Tuple
* Set
* Dictionary

The comparison covered:

* Mutability
* Ordering
* Duplicate values
* Indexing
* Common use cases
* Time complexity
* Practical Python examples

## Task 2: Contact Management System

A Contact Management System was developed using multiple Python data structures and concepts.

### Data Structure

Contacts are stored using a nested dictionary:

```python
{
    "id": {
        "name": "Areeba",
        "phone": "03001234567",
        "email": "areeba@gmail.com",
        "tags": {"student", "friend"},
        "notes": ["university", "internship"]
    }
}
```

### Features

* Add new contacts
* Search contacts
* Update contact information
* Delete contacts
* Search using partial matches
* Add and remove tags
* Find contacts by tag
* Save contacts to JSON
* Load contacts from JSON
* Error handling for JSON operations
* Display contact statistics
* Interactive menu using loops

### Python Concepts Used

* Dictionaries
* Sets
* Lists
* Functions
* Dictionary comprehensions
* Set operations
* Loops
* Conditional statements
* JSON
* Exception handling
* `Counter`
* Interactive CLI

## Files

```text
Day14/
├── Day14_Data_Structures_Cheat_Sheet.ipynb
├── README.md
└── LEARNINGS.md
```

## How to Run

Open the Jupyter Notebook:

```text
Day14_Data_Structures_Cheat_Sheet.ipynb
```

Run the cells from top to bottom.

The Contact Management System provides an interactive menu where users can add, search, update, delete, and manage contacts.

## Outcome

By completing Day 14, I reviewed Python's major built-in data structures and applied them together in a practical mini-project.
