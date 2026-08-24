# Python Syntax Dictionary

> A quick-reference dictionary for Python syntax. Use **Ctrl+F** to search for a keyword, syntax name, or topic.

---

## Table of Contents

1. [How to Use This Dictionary](#how-to-use-this-dictionary)
2. [Quick Lookup Table](#quick-lookup-table)
3. [Basic](#1-basic)
   - [Variables](#variables)
   - [Data Types](#data-types)
   - [Operators](#operators)
   - [Strings](#strings)
   - [Input / Output](#input--output)
   - [Type Conversion](#type-conversion)
   - [Comments and Docstrings](#comments-and-docstrings)
4. [Collection](#2-collection)
   - [List](#list)
   - [List Slicing](#list-slicing)
   - [List Methods](#list-methods)
   - [List Comprehension](#list-comprehension)
   - [Tuple](#tuple)
   - [Set](#set)
   - [Dictionary](#dictionary)
   - [Dictionary Comprehension](#dictionary-comprehension)
   - [Unpacking](#unpacking)
5. [Control Flow](#3-control-flow)
   - [if / elif / else](#if--elif--else)
   - [Ternary](#ternary)
   - [for](#for)
   - [range](#range)
   - [while](#while)
   - [break / continue / pass](#break--continue--pass)
   - [enumerate](#enumerate)
   - [zip](#zip)
   - [match / case](#match--case)
6. [Function](#4-function)
   - [Basic Function](#basic-function)
   - [Parameters](#parameters)
   - [Default Parameters](#default-parameters)
   - [Keyword Arguments](#keyword-arguments)
   - [*args / **kwargs](#args--kwargs)
   - [Lambda](#lambda)
   - [map / filter](#map--filter)
   - [Type Hints](#type-hints)
   - [Scope](#scope)
   - [Generator / yield](#generator--yield)
7. [OOP](#5-oop)
   - [Class](#class)
   - [Constructor](#constructor)
   - [Instance Methods](#instance-methods)
   - [Class / Static Methods](#class--static-methods)
   - [Inheritance](#inheritance)
   - [super](#super)
   - [Properties](#properties)
   - [Special Methods](#special-methods)
8. [File](#6-file)
   - [open](#open)
   - [Read](#read)
   - [Write / Append](#write--append)
   - [CSV](#csv)
   - [JSON](#json)
   - [Pathlib](#pathlib)
9. [Exception](#7-exception)
   - [try / except](#try--except)
   - [else / finally](#else--finally)
   - [raise](#raise)
   - [Custom Exceptions](#custom-exceptions)
10. [Advanced](#8-advanced)
   - [Modules / Imports](#modules--imports)
   - [__name__](#__name__)
   - [Decorators](#decorators)
   - [Context Managers](#context-managers)
   - [Walrus Operator](#walrus-operator)
   - [any / all](#any--all)
   - [sorted / key](#sorted--key)
   - [Assertions](#assertions)
   - [Dataclasses](#dataclasses)
   - [Async / Await](#async--await)
11. [Ctrl+F Keyword Index](#ctrlf-keyword-index)

---

# How to Use This Dictionary

- **Ctrl+F**: search `list`, `dict`, `for`, `async`, `try`, `class`, etc.
- Search the **syntax name** when you know what you need.
- Search a **keyword** when you remember only part of the syntax.
- Examples are intentionally short and copyable.
- Python uses **indentation** instead of `{}` for code blocks.

---

# Quick Lookup Table

| Need | Syntax | Example |
|---|---|---|
| Variable | `x = value` | `age = 20` |
| String | `str` | `name = "John"` |
| List | `[]` | `nums = [1, 2, 3]` |
| Tuple | `()` | `point = (10, 20)` |
| Set | `{}` | `ids = {1, 2, 3}` |
| Dictionary | `{key: value}` | `user = {"name": "John"}` |
| Condition | `if` | `if age >= 18:` |
| Loop | `for` | `for x in nums:` |
| Range | `range()` | `range(10)` |
| While | `while` | `while x < 10:` |
| Function | `def` | `def add(a, b):` |
| Lambda | `lambda` | `lambda x: x * 2` |
| Exception | `try/except` | `try: ... except:` |
| Class | `class` | `class User:` |
| Import | `import` | `import math` |
| File | `with open()` | `with open("a.txt") as f:` |
| Type hint | `: type` | `x: int = 10` |
| Return | `return` | `return result` |
| Generator | `yield` | `yield value` |
| Async | `async def` | `async def fetch():` |

---

# 1. Basic

## Variables

### Basic assignment

```python
name = "John"
age = 20
price = 10.5
active = True
nothing = None
```

### Multiple assignment

```python
x, y = 10, 20
a = b = c = 0
```

### Swap

```python
a, b = b, a
```

### Augmented assignment

```python
x += 1
x -= 1
x *= 2
x /= 2
x //= 2
x %= 2
x **= 2
```

---

## Data Types

| Type | Example |
|---|---|
| `int` | `10` |
| `float` | `10.5` |
| `complex` | `2 + 3j` |
| `str` | `"hello"` |
| `bool` | `True` |
| `NoneType` | `None` |
| `list` | `[1, 2, 3]` |
| `tuple` | `(1, 2, 3)` |
| `set` | `{1, 2, 3}` |
| `dict` | `{"a": 1}` |

### Check type

```python
type(value)
isinstance(value, int)
```

---

## Operators

### Arithmetic

```python
a + b       # addition
a - b       # subtraction
a * b       # multiplication
a / b       # division
a // b      # floor division
a % b       # remainder
a ** b      # exponent
```

### Comparison

```python
a == b
a != b
a > b
a < b
a >= b
a <= b
```

### Logical

```python
a and b
a or b
not a
```

### Membership

```python
x in collection
x not in collection
```

### Identity

```python
x is y
x is not y

value is None
```

> Prefer `==` for value comparison and `is` mainly for identity checks such as `value is None`.

---

## Strings

### Create

```python
text = "Hello"
text = 'Hello'
text = """Multi-line
text"""
```

### Indexing

```python
text[0]
text[-1]
```

### Slicing

```python
text[start:end]
text[:end]
text[start:]
text[:]
text[::-1]
```

### Common methods

```python
text.upper()
text.lower()
text.capitalize()
text.title()

text.strip()
text.lstrip()
text.rstrip()

text.replace("old", "new")
text.split(",")
text.startswith("Hi")
text.endswith(".")
```

### Membership

```python
"Python" in text
```

### Length

```python
len(text)
```

### f-string

```python
name = "John"
age = 20

message = f"My name is {name}. I am {age}."
```

### Formatting

```python
price = 1234.5678
formatted = f"{price:.2f}"
```

---

## Input / Output

### Input

```python
name = input("Name: ")
age = int(input("Age: "))
price = float(input("Price: "))
```

### Print

```python
print("Hello")
print(name, age)
print(f"Name: {name}")
```

### Print without newline

```python
print("Hello", end=" ")
print("World")
```

---

## Type Conversion

```python
int("10")
float("10.5")
str(100)
bool(1)

list("abc")
tuple([1, 2, 3])
set([1, 2, 2, 3])
```

---

## Comments and Docstrings

### Comment

```python
# This is a comment
```

### Docstring

```python
def add(a, b):
    """Return the sum of two numbers."""
    return a + b
```

---

# 2. Collection

# List

## Create

```python
numbers = [1, 2, 3, 4, 5]
names = ["John", "Alice"]
mixed = [1, "Hello", True, 3.14]
```

## Access

```python
numbers[0]
numbers[-1]
```

## Modify

```python
numbers[0] = 100
```

## Add

```python
numbers.append(6)
numbers.insert(0, 100)
numbers.extend([7, 8, 9])
```

## Remove

```python
numbers.remove(3)
numbers.pop()
numbers.pop(0)
del numbers[0]
numbers.clear()
```

## Search

```python
3 in numbers
numbers.index(3)
numbers.count(3)
```

## Length

```python
len(numbers)
```

---

# List Slicing

```python
numbers[start:end]
numbers[:3]
numbers[2:]
numbers[1:4]
numbers[::2]
numbers[::-1]
```

Syntax:

```text
[start : stop : step]
```

---

# List Methods

```python
numbers.append(x)
numbers.extend(iterable)
numbers.insert(index, x)

numbers.remove(x)
numbers.pop()
numbers.pop(index)
numbers.clear()

numbers.index(x)
numbers.count(x)

numbers.sort()
numbers.sort(reverse=True)

numbers.reverse()

new_list = numbers.copy()
```

### `sorted()` vs `.sort()`

```python
sorted_numbers = sorted(numbers)

numbers.sort()
```

- `sorted()` returns a new list.
- `.sort()` modifies the original list.

---

# List Comprehension

### Basic

```python
squares = [x ** 2 for x in range(5)]
```

### With condition

```python
even = [x for x in range(10) if x % 2 == 0]
```

### if / else

```python
result = [
    "even" if x % 2 == 0 else "odd"
    for x in range(10)
]
```

### Nested

```python
pairs = [
    (x, y)
    for x in range(3)
    for y in range(3)
]
```

---

# Tuple

## Create

```python
point = (10, 20)
colors = ("red", "green", "blue")
```

Single-item tuple:

```python
value = (10,)
```

## Access

```python
point[0]
point[-1]
```

## Unpacking

```python
x, y = point
```

## Methods

```python
point.count(10)
point.index(20)
```

> Tuples are immutable: their elements cannot be reassigned.

---

# Set

## Create

```python
numbers = {1, 2, 3}
empty_set = set()
```

> `{}` creates an empty dictionary, not an empty set.

## Add / Remove

```python
numbers.add(4)
numbers.update([5, 6])

numbers.remove(2)
numbers.discard(2)
numbers.pop()
numbers.clear()
```

## Set operations

```python
a | b       # union
a & b       # intersection
a - b       # difference
a ^ b       # symmetric difference
```

Methods:

```python
a.union(b)
a.intersection(b)
a.difference(b)
a.symmetric_difference(b)
```

## Membership

```python
3 in numbers
```

---

# Dictionary

## Create

```python
user = {
    "name": "John",
    "age": 20,
    "major": "IT"
}
```

## Access

```python
user["name"]
user.get("name")
user.get("email", "Not found")
```

## Add / Update

```python
user["age"] = 21
user["email"] = "john@example.com"

user.update({
    "age": 22,
    "city": "Hanoi"
})
```

## Remove

```python
del user["age"]
user.pop("age")
user.popitem()
user.clear()
```

## Keys / Values / Items

```python
user.keys()
user.values()
user.items()
```

## Membership

```python
"name" in user
```

## Loop

```python
for key in user:
    print(key)

for value in user.values():
    print(value)

for key, value in user.items():
    print(key, value)
```

---

# Dictionary Comprehension

```python
squares = {
    x: x ** 2
    for x in range(5)
}
```

With condition:

```python
even_squares = {
    x: x ** 2
    for x in range(10)
    if x % 2 == 0
}
```

---

# Unpacking

## List / Tuple

```python
numbers = [1, 2, 3]

a, b, c = numbers
```

### Star unpacking

```python
first, *middle, last = [1, 2, 3, 4, 5]
```

Result:

```text
first  = 1
middle = [2, 3, 4]
last   = 5
```

## Function arguments

```python
numbers = [1, 2, 3]

print(*numbers)
```

## Dictionary unpacking

```python
a = {"name": "John"}
b = {"age": 20}

user = {**a, **b}
```

---

# 3. Control Flow

# if / elif / else

```python
if condition:
    ...
elif another_condition:
    ...
else:
    ...
```

Example:

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"
```

---

# Ternary

```python
result = value_if_true if condition else value_if_false
```

Example:

```python
status = "Adult" if age >= 18 else "Minor"
```

---

# for

```python
for item in collection:
    print(item)
```

Example:

```python
numbers = [1, 2, 3]

for number in numbers:
    print(number)
```

---

# range

```python
range(stop)
range(start, stop)
range(start, stop, step)
```

Examples:

```python
range(5)
range(1, 5)
range(0, 10, 2)
range(10, 0, -1)
```

---

# while

```python
while condition:
    ...
```

Example:

```python
i = 0

while i < 5:
    print(i)
    i += 1
```

---

# break / continue / pass

### break

Stop the loop:

```python
for i in range(10):
    if i == 5:
        break
```

### continue

Skip the current iteration:

```python
for i in range(5):
    if i == 2:
        continue

    print(i)
```

### pass

Do nothing:

```python
def future_function():
    pass
```

---

# enumerate

Get index + value:

```python
names = ["John", "Alice", "Bob"]

for index, name in enumerate(names):
    print(index, name)
```

Custom start:

```python
for index, name in enumerate(names, start=1):
    print(index, name)
```

---

# zip

Iterate over multiple iterables:

```python
names = ["John", "Alice"]
ages = [20, 21]

for name, age in zip(names, ages):
    print(name, age)
```

---

# match / case

Python's pattern matching:

```python
match command:
    case "start":
        print("Starting")
    case "stop":
        print("Stopping")
    case _:
        print("Unknown command")
```

`_` is the default/wildcard case.

---

# 4. Function

# Basic Function

```python
def greet():
    print("Hello")
```

Call:

```python
greet()
```

---

# Parameters

```python
def add(a, b):
    return a + b
```

Call:

```python
result = add(10, 20)
```

---

# Default Parameters

```python
def greet(name="John"):
    print(f"Hello {name}")
```

```python
greet()
greet("Alice")
```

---

# Keyword Arguments

```python
def introduce(name, age):
    print(name, age)

introduce(name="John", age=20)
```

Positional + keyword:

```python
introduce("John", age=20)
```

---

# *args / **kwargs

## `*args`

Accept multiple positional arguments:

```python
def add(*numbers):
    return sum(numbers)

add(1, 2, 3, 4)
```

Inside the function, `args` is a tuple.

## `**kwargs`

Accept multiple keyword arguments:

```python
def print_info(**info):
    for key, value in info.items():
        print(key, value)

print_info(name="John", age=20)
```

Inside the function, `kwargs` is a dictionary.

---

# Lambda

Syntax:

```python
lambda arguments: expression
```

Example:

```python
square = lambda x: x ** 2

print(square(5))
```

Common usage:

```python
sorted(users, key=lambda user: user["age"])
```

---

# map / filter

## map

Apply a function to every item:

```python
numbers = [1, 2, 3]

result = list(
    map(lambda x: x * 2, numbers)
)
```

## filter

Keep items satisfying a condition:

```python
numbers = [1, 2, 3, 4, 5]

result = list(
    filter(lambda x: x % 2 == 0, numbers)
)
```

> List comprehensions are often more readable for simple cases.

---

# Type Hints

## Variables

```python
name: str = "John"
age: int = 20
price: float = 10.5
active: bool = True
```

## Function

```python
def add(a: int, b: int) -> int:
    return a + b
```

## Collections

```python
numbers: list[int] = [1, 2, 3]

users: dict[str, int] = {
    "John": 20
}
```

## Optional / None

Modern Python:

```python
def find_user(user_id: int) -> str | None:
    ...
```

---

# Scope

## Local variable

```python
def test():
    x = 10
```

`x` exists inside the function.

## Global variable

```python
x = 10

def test():
    print(x)
```

## global

```python
x = 10

def change():
    global x
    x = 20
```

Use `global` sparingly.

---

# Generator / yield

```python
def numbers():
    yield 1
    yield 2
    yield 3
```

Use:

```python
for number in numbers():
    print(number)
```

`yield` produces values lazily instead of returning all values at once.

---

# 5. OOP

# Class

```python
class Student:
    pass
```

---

# Constructor

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Create object:

```python
student = Student("John", 20)
```

Access attributes:

```python
print(student.name)
print(student.age)
```

---

# Instance Methods

```python
class Student:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"My name is {self.name}"
```

```python
student = Student("John")

print(student.introduce())
```

---

# Class / Static Methods

## Class variable

```python
class Student:
    school = "ABC University"
```

## `@classmethod`

```python
class Student:

    count = 0

    @classmethod
    def get_count(cls):
        return cls.count
```

Call:

```python
Student.get_count()
```

## `@staticmethod`

```python
class Math:

    @staticmethod
    def add(a, b):
        return a + b
```

Call:

```python
Math.add(10, 20)
```

---

# Inheritance

```python
class Animal:

    def speak(self):
        print("Animal sound")


class Dog(Animal):

    def bark(self):
        print("Woof")
```

```python
dog = Dog()

dog.speak()
dog.bark()
```

---

# super

Call parent implementation:

```python
class Animal:

    def __init__(self, name):
        self.name = name


class Dog(Animal):

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
```

---

# Properties

```python
class Person:

    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value
```

Usage:

```python
person = Person(20)

print(person.age)

person.age = 21
```

---

# Special Methods

Common dunder methods:

```python
__init__      # constructor
__str__       # string representation
__repr__      # developer representation
__len__       # len(object)
__eq__        # ==
__lt__        # <
__add__       # +
__iter__      # iteration
__next__      # next()
```

Example:

```python
class User:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
```

---

# 6. File

# open

Basic:

```python
file = open("file.txt", "r")
```

Preferred:

```python
with open("file.txt", "r") as file:
    ...
```

Modes:

| Mode | Meaning |
|---|---|
| `r` | Read |
| `w` | Write / overwrite |
| `a` | Append |
| `x` | Create |
| `b` | Binary |
| `t` | Text |
| `+` | Read + write |

Examples:

```python
open("file.txt", "r")
open("file.txt", "w")
open("file.txt", "a")
open("image.png", "rb")
```

---

# Read

Read everything:

```python
with open("file.txt", "r") as file:
    content = file.read()
```

Read one line:

```python
line = file.readline()
```

Read all lines:

```python
lines = file.readlines()
```

Iterate:

```python
with open("file.txt", "r") as file:
    for line in file:
        print(line.strip())
```

---

# Write / Append

Write:

```python
with open("file.txt", "w") as file:
    file.write("Hello")
```

Append:

```python
with open("file.txt", "a") as file:
    file.write("\nWorld")
```

---

# CSV

Using the standard library:

```python
import csv
```

Read:

```python
with open("users.csv", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
```

Dictionary rows:

```python
with open("users.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["name"])
```

Write:

```python
with open("users.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow(["name", "age"])
    writer.writerow(["John", 20])
```

---

# JSON

```python
import json
```

Python object -> JSON:

```python
data = {
    "name": "John",
    "age": 20
}

json_string = json.dumps(data)
```

JSON -> Python object:

```python
data = json.loads(json_string)
```

Read JSON file:

```python
with open("data.json", "r", encoding="utf-8") as file:
    data = json.load(file)
```

Write JSON file:

```python
with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)
```

---

# pathlib

Modern path handling:

```python
from pathlib import Path

path = Path("data/file.txt")
```

Check:

```python
path.exists()
path.is_file()
path.is_dir()
```

Read:

```python
content = path.read_text(encoding="utf-8")
```

Write:

```python
path.write_text("Hello", encoding="utf-8")
```

Join paths:

```python
path = Path("data") / "users" / "file.txt"
```

---

# 7. Exception

# try / except

```python
try:
    number = int(input("Number: "))
except ValueError:
    print("Invalid number")
```

Multiple exceptions:

```python
try:
    ...
except ValueError:
    ...
except TypeError:
    ...
```

Catch as variable:

```python
try:
    ...
except ValueError as e:
    print(e)
```

---

# else / finally

## else

Runs when no exception occurs:

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print(result)
```

## finally

Always runs:

```python
try:
    ...
except Exception:
    ...
finally:
    print("Finished")
```

---

# raise

Manually raise an exception:

```python
raise ValueError("Invalid value")
```

Example:

```python
def divide(a, b):

    if b == 0:
        raise ValueError("Cannot divide by zero")

    return a / b
```

---

# Custom Exceptions

```python
class InvalidAgeError(Exception):
    pass
```

Use:

```python
def validate_age(age):

    if age < 0:
        raise InvalidAgeError("Age cannot be negative")
```

---

# 8. Advanced

# Modules / Imports

## Import module

```python
import math

math.sqrt(25)
```

## Import specific function

```python
from math import sqrt

sqrt(25)
```

## Alias

```python
import numpy as np
```

## Multiple imports

```python
from math import sqrt, ceil, floor
```

---

# __name__

Common entry point:

```python
def main():
    print("Hello")


if __name__ == "__main__":
    main()
```

This lets a file behave differently when:

1. Run directly.
2. Imported by another file.

---

# Decorators

Basic syntax:

```python
@decorator
def function():
    ...
```

Example:

```python
def log(func):

    def wrapper():
        print("Before")
        func()
        print("After")

    return wrapper


@log
def hello():
    print("Hello")
```

---

# Context Managers

Typical:

```python
with open("file.txt") as file:
    data = file.read()
```

The `with` statement manages setup and cleanup automatically.

Custom context manager:

```python
from contextlib import contextmanager

@contextmanager
def managed_resource():
    print("Open")
    try:
        yield
    finally:
        print("Close")
```

---

# Walrus Operator `:=`

Assign inside an expression:

```python
if (n := len(numbers)) > 3:
    print(n)
```

Another example:

```python
while (line := file.readline()):
    print(line)
```

Use when it makes the code clearer; don't force it into every expression.

---

# any / all

## any

Returns `True` if at least one item is truthy:

```python
numbers = [False, False, True]

any(numbers)
```

## all

Returns `True` if every item is truthy:

```python
values = [True, True, True]

all(values)
```

With conditions:

```python
if any(x > 10 for x in numbers):
    print("Found")
```

```python
if all(x > 0 for x in numbers):
    print("All positive")
```

---

# sorted / key

Basic:

```python
numbers = [3, 1, 5, 2]

sorted(numbers)
sorted(numbers, reverse=True)
```

Sort objects by a field:

```python
users = [
    {"name": "John", "age": 20},
    {"name": "Alice", "age": 18}
]

users_sorted = sorted(
    users,
    key=lambda user: user["age"]
)
```

---

# Assertions

Basic:

```python
assert age >= 18
```

With message:

```python
assert age >= 18, "Age must be at least 18"
```

Useful for checking assumptions during development/testing.

---

# Dataclasses

Useful for data-focused classes:

```python
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
```

Create:

```python
user = User("John", 20)
```

---

# Async / Await

Define async function:

```python
async def fetch_data():
    ...
```

Wait for async operation:

```python
result = await fetch_data()
```

Run from an async function:

```python
async def main():
    result = await fetch_data()
```

With asyncio:

```python
import asyncio

asyncio.run(main())
```

---

# Ctrl+F Keyword Index

Use **Ctrl+F** with these terms.

## Basic

```text
variable
assignment
int
float
str
bool
None
type
isinstance
operator
arithmetic
comparison
logical
and
or
not
in
not in
is
is not
string
str
f-string
input
print
len
type conversion
int()
float()
str()
bool()
comment
docstring
```

## Collection

```text
list
list()
append
insert
extend
remove
pop
clear
index
count
sort
sorted
reverse
copy
slice
slicing
list comprehension
tuple
tuple()
set
set()
add
discard
union
intersection
difference
dictionary
dict
dict()
get
keys
values
items
update
popitem
dictionary comprehension
unpacking
*
**
```

## Control Flow

```text
if
elif
else
ternary
for
while
range
break
continue
pass
enumerate
zip
match
case
```

## Function

```text
def
function
parameter
argument
return
default parameter
keyword argument
*args
**kwargs
lambda
map
filter
type hints
scope
local
global
yield
generator
```

## OOP

```text
class
object
__init__
constructor
self
method
attribute
class variable
classmethod
staticmethod
@property
@property.setter
inheritance
super
parent
child
special method
dunder
__str__
__repr__
__len__
__eq__
__add__
```

## File

```text
open
with
read
readline
readlines
write
append
CSV
csv
csv.reader
csv.writer
DictReader
JSON
json
json.load
json.dump
json.loads
json.dumps
Path
pathlib
Path.exists
Path.read_text
Path.write_text
```

## Exception

```text
try
except
Exception
ValueError
TypeError
KeyError
IndexError
FileNotFoundError
ZeroDivisionError
else
finally
raise
custom exception
```

## Advanced

```text
import
from
as
module
package
__name__
__main__
decorator
@
context manager
with
contextlib
@contextmanager
walrus
:=
any
all
sorted
key
assert
dataclass
@dataclass
async
await
asyncio
async def
asyncio.run
```

---

# Ultra Quick Reference

```python
# VARIABLE
x = 10

# STRING
name = "John"
f"Hello {name}"

# LIST
items = [1, 2, 3]
items.append(4)

# TUPLE
point = (10, 20)

# SET
items = {1, 2, 3}
items.add(4)

# DICT
user = {"name": "John", "age": 20}
user["name"]
user.get("email")

# IF
if condition:
    ...
elif condition:
    ...
else:
    ...

# FOR
for item in items:
    ...

# RANGE
for i in range(10):
    ...

# WHILE
while condition:
    ...

# BREAK / CONTINUE
break
continue

# FUNCTION
def add(a, b):
    return a + b

# LAMBDA
lambda x: x * 2

# COMPREHENSION
[x * 2 for x in numbers]

# EXCEPTION
try:
    ...
except Exception as e:
    ...
finally:
    ...

# CLASS
class User:

    def __init__(self, name):
        self.name = name

# INHERITANCE
class Admin(User):
    pass

# IMPORT
import math
from math import sqrt

# FILE
with open("file.txt", "r") as file:
    data = file.read()

# JSON
import json
data = json.loads(text)

# TYPE HINT
def add(a: int, b: int) -> int:
    return a + b

# GENERATOR
def numbers():
    yield 1

# DECORATOR
@decorator
def function():
    ...

# ASYNC
async def fetch():
    result = await other_function()

# ENTRY POINT
if __name__ == "__main__":
    main()
```

---

## Recommended Ctrl+F Search Strategy

If you are coding and know **what you want to do**, search using:

| I want to... | Ctrl+F |
|---|---|
| Add an item to a list | `append` |
| Remove an item | `remove` / `pop` |
| Get dictionary value safely | `get` |
| Loop through a list | `for` |
| Get index + value | `enumerate` |
| Loop two lists together | `zip` |
| Loop N times | `range` |
| Filter a list | `filter` / `list comprehension` |
| Transform a list | `map` / `list comprehension` |
| Sort data | `sorted` / `sort` |
| Write a function | `def` |
| Accept unlimited arguments | `*args` |
| Accept unlimited keyword arguments | `**kwargs` |
| Handle errors | `try` |
| Create a class | `class` |
| Inherit a class | `inheritance` |
| Read a file | `open` / `read` |
| Work with JSON | `json` |
| Work with CSV | `csv` |
| Import code | `import` |
| Make async code | `async` / `await` |
| Run a file directly | `__main__` |
| Create a decorator | `decorator` |
| Create a generator | `yield` |
| Add type information | `type hints` |

---

## End

This file is intended as a **quick Python syntax lookup reference**, not a replacement for the official Python documentation.
