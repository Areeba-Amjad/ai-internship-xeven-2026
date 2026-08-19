# Day 9: Tuples & Sets

## Overview

Day 9 focused on Python tuples and sets. Tuples were used to store
fixed geographic coordinates, while sets were used to manage unique
data and perform set operations.

## Topics Covered

- Tuples in Python
- Tuple indexing
- Tuple immutability
- Sets in Python
- Set union
- Set intersection
- Set difference
- Unique data handling
- Set comprehensions

## Practical Tasks

### Task 1: Geographic Coordinates System

- Stored city locations using tuples in the format:
  `(city_name, latitude, longitude)`
- Created a function to calculate the distance between two coordinates.
- Used the Haversine formula to calculate geographic distance.
- Created a function to find the closest city to a given coordinate.
- Demonstrated tuple immutability using `TypeError`.

### Task 2: Unique Visitor Tracker

- Used sets to store unique website visitors.
- Removed duplicate IP addresses automatically.
- Used intersection to find common visitors.
- Used difference to find unique visitors for each day.
- Used union to calculate total unique visitors.
- Calculated visitor growth rate.
- Calculated visitor retention rate.

### Task 3: Email Validation System

- Created a set of valid email domains.
- Validated email addresses using the `@` symbol and domain name.
- Used a set to store unique registered email addresses.
- Prevented duplicate email registrations.
- Used set operations to find emails from specific domains.

## Tools Used

- Python
- Jupyter Notebook
- Git
- GitHub

## Files

- `Day09_Tuples_Sets.ipynb` - Practical implementation notebook
- `README.md` - Day 9 overview and task summary
- `LEARNINGS.md` - Concepts and lessons learned