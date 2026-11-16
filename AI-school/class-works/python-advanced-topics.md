# Python: OOPS and Advanced Topics (with Examples)

## Table of Contents

1. [OOPS](#1-oops)
2. [Exception Handling](#2-exception-handling)
3. [File Handling](#3-file-handling)
4. [Serialization](#4-serialization)
5. [Regular Expression and Web Scraping](#5-regular-expression-and-web-scraping)
6. [Multithreading](#6-multithreading)
7. [Python Database Connectivity (PDBC)](#7-python-database-connectivity-pdbc)
8. [Decorators](#8-decorators)
9. [Generators](#9-generators)
10. [Logging Module](#10-logging-module)
11. [Assertions](#11-assertions)
12. [NumPy](#12-numpy)
13. [Pandas](#13-pandas)
14. [Unit Testing](#14-unit-testing)

---

## 1. OOPS

Object Oriented Programming organizes code around **objects**: things that bundle data (variables) and behaviour (functions) together.

### 1.1 Class and Object

- **Class**: a blueprint. A collection of variables and functions.
- **Object**: a real instance created from the class.

```python
class Student:
    school = "ABC School"          # class variable (shared by all objects)

    def __init__(self, name, marks):   # constructor, runs when object is created
        self.name = name               # instance variable (separate per object)
        self.marks = marks

    def show(self):                    # instance method
        print(f"{self.name} scored {self.marks}")

s1 = Student("Asha", 90)   # creating objects (calling the class)
s2 = Student("Ravi", 75)
s1.show()                  # Asha scored 90
s2.show()                  # Ravi scored 75
print(Student.school)      # ABC School
```

Key points:

- `self` refers to the current object. It is passed automatically.
- `__init__` is the constructor. It initializes instance variables.
- Instance variables belong to one object; class variables are shared by all.

### 1.2 Types of Variables

**Instance variables**: belong to one object; each object has its own copy. Defined with `self`.

**Class variables**: belong to the class; shared by all objects. Defined in the class body, outside any method.

**Local variables**: defined inside a method without `self`; exist only while the method runs.

```python
class Student:
    school = "ABC School"          # class variable

    def __init__(self, name):
        self.name = name           # instance variable

    def total(self):
        marks = 90                 # local variable
        return marks

s1 = Student("Asha")
s2 = Student("Ravi")
print(s1.name, s2.name)    # Asha Ravi
print(Student.school)      # ABC School

Student.school = "XYZ"     # changes it for every object
print(s1.school)           # XYZ
```

| Type     | Defined where          | Belongs to       | Shared? |
|----------|------------------------|------------------|---------|
| Instance | inside method, `self.` | object           | No      |
| Class    | inside class body      | class            | Yes     |
| Local    | inside method          | that method call | No      |

### 1.3 Types of Methods

```python
class Account:
    bank = "XYZ Bank"
    count = 0

    def __init__(self, balance):
        self.balance = balance
        Account.count += 1

    def deposit(self, amount):          # instance method: uses self
        self.balance += amount

    @classmethod
    def total_accounts(cls):            # class method: uses cls
        return cls.count

    @staticmethod
    def is_valid(amount):               # static method: uses neither
        return amount > 0

a = Account(1000)
b = Account(500)
a.deposit(200)
print(a.balance)                 # 1200
print(Account.total_accounts())  # 2
print(Account.is_valid(-5))      # False
```

### 1.4 Inheritance

A child class reuses the variables and methods of a parent class.

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I am {self.name}")

class Employee(Person):                  # single inheritance
    def __init__(self, name, salary):
        super().__init__(name)           # call parent constructor
        self.salary = salary

    def info(self):
        print(f"{self.name} earns {self.salary}")

e = Employee("Kiran", 50000)
e.greet()    # Hello, I am Kiran   (inherited)
e.info()     # Kiran earns 50000
```

Types of inheritance:

```python
class A: pass
class B(A): pass          # single:       A -> B
class C(B): pass          # multilevel:   A -> B -> C
class D(A): pass          # hierarchical: A -> B and A -> D
class E(B, D): pass       # multiple:     E inherits from B and D
```

**MRO (Method Resolution Order)**: the order Python searches classes for a method.

```python
print(E.__mro__)   # E, B, D, A, object
```

### 1.5 Polymorphism ("many forms")

**Method overriding**: the child redefines a parent method.

```python
class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

for animal in (Dog(), Cat(), Animal()):
    animal.sound()      # Bark, Meow, Some sound
```

**Duck typing**: if it has the method, it works, no common parent needed.

```python
class Duck:
    def speak(self): print("Quack")

class Robot:
    def speak(self): print("Beep")

for thing in (Duck(), Robot()):
    thing.speak()
```

**Operator overloading**: give operators meaning for your own classes.

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

print(Point(1, 2) + Point(3, 4))   # (4, 6)
```

Python has no true method overloading. The last definition wins, so use default arguments instead:

```python
class Calc:
    def add(self, a, b=0, c=0):
        return a + b + c

print(Calc().add(1), Calc().add(1, 2), Calc().add(1, 2, 3))   # 1 3 6
```

### 1.6 Encapsulation

Wrapping data and methods together and controlling access to the data.

| Style    | Syntax    | Meaning                                        |
| -------- | --------- | ---------------------------------------------- |
| Public   | `name`    | Accessible everywhere                          |
| Protected| `_name`   | By convention, use inside class and subclasses |
| Private  | `__name`  | Name-mangled to `_Class__name`                 |

```python
class Bank:
    def __init__(self, balance):
        self.__balance = balance       # private

    @property
    def balance(self):                 # getter
        return self.__balance

    @balance.setter
    def balance(self, value):          # setter with validation
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = value

acc = Bank(1000)
print(acc.balance)       # 1000
acc.balance = 2000       # goes through the setter
# print(acc.__balance)   # AttributeError
```

### 1.7 Abstraction

Hide implementation details and expose only what is needed. An **abstract class** cannot be instantiated and forces children to implement certain methods.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14159 * self.r ** 2

class Square(Shape):
    def __init__(self, s):
        self.s = s

    def area(self):
        return self.s ** 2

# Shape()             # TypeError: can't instantiate abstract class
print(Circle(2).area())   # 12.56636
print(Square(3).area())   # 9
```

### 1.8 Useful Special (Dunder) Methods

| Method      | Called when                    |
| ----------- | ------------------------------ |
| `__init__`  | object is created              |
| `__str__`   | `print(obj)` / `str(obj)`      |
| `__repr__`  | debugging representation       |
| `__len__`   | `len(obj)`                     |
| `__eq__`    | `obj1 == obj2`                 |
| `__del__`   | object is destroyed            |

---

## 2. Exception Handling

An **exception** is a runtime error that stops the program unless handled.

### 2.1 try / except / else / finally

```python
try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    result = a / b
except ValueError:
    print("Please enter integers only")
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:           # catch-all, keep it last
    print("Unexpected error:", e)
else:
    print("Result:", result)     # runs only if NO exception
finally:
    print("Done")                # ALWAYS runs (cleanup)
```

### 2.2 Common Built-in Exceptions

| Exception           | Cause                          |
| ------------------- | ------------------------------ |
| `ValueError`        | right type, wrong value        |
| `TypeError`         | wrong type for the operation   |
| `ZeroDivisionError` | division by zero               |
| `IndexError`        | list index out of range        |
| `KeyError`          | missing dictionary key         |
| `FileNotFoundError` | file does not exist            |
| `ImportError`       | import fails                   |

### 2.3 Raising Exceptions

```python
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient balance")
    return balance - amount

try:
    withdraw(100, 500)
except ValueError as e:
    print(e)           # Insufficient balance
```

### 2.4 Custom Exceptions

```python
class AgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise AgeError("Must be 18 or older")
    return "Allowed"

try:
    check_age(15)
except AgeError as e:
    print("Error:", e)
```

---

## 3. File Handling

Use `open()` to read and write files. Always use `with` so the file closes automatically.

### 3.1 Modes

| Mode | Meaning                                   |
| ---- | ----------------------------------------- |
| `r`  | read (default), error if file missing     |
| `w`  | write, creates the file or **overwrites** |
| `a`  | append to the end                         |
| `r+` | read and write                            |
| `b`  | binary, e.g. `rb`, `wb`                   |

### 3.2 Writing and Reading

```python
# Write (overwrites)
with open("notes.txt", "w") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")

# Append
with open("notes.txt", "a") as f:
    f.write("Line 3\n")

# Read everything
with open("notes.txt", "r") as f:
    print(f.read())

# Read line by line (memory friendly)
with open("notes.txt") as f:
    for line in f:
        print(line.strip())

# Read into a list
with open("notes.txt") as f:
    lines = f.readlines()
```

### 3.3 Handling a Missing File

```python
try:
    with open("missing.txt") as f:
        data = f.read()
except FileNotFoundError:
    print("File not found")
```

### 3.4 CSV Files

```python
import csv

with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "marks"])
    writer.writerow(["Asha", 90])
    writer.writerow(["Ravi", 75])

with open("students.csv") as f:
    for row in csv.DictReader(f):
        print(row["name"], row["marks"])
```

### 3.5 Working with Paths

```python
import os
from pathlib import Path

print(os.path.exists("notes.txt"))
print(os.listdir("."))

p = Path("notes.txt")
print(p.exists(), p.suffix, p.stem)
```

---

## 4. Serialization

Converting an object into a storable or transmittable form (**serialization / pickling**) and back (**deserialization / unpickling**).

### 4.1 pickle (Python-specific, binary)

```python
import pickle

class Student:
    def __init__(self, name, marks):
        self.name, self.marks = name, marks

s = Student("Asha", 90)

with open("student.pkl", "wb") as f:      # serialize
    pickle.dump(s, f)

with open("student.pkl", "rb") as f:      # deserialize
    obj = pickle.load(f)

print(obj.name, obj.marks)   # Asha 90
```

> Never unpickle data from an untrusted source. It can execute arbitrary code.

### 4.2 JSON (text, works across languages)

```python
import json

data = {"name": "Asha", "marks": [90, 85], "passed": True}

text = json.dumps(data, indent=2)   # dict -> JSON string
back = json.loads(text)             # JSON string -> dict

with open("data.json", "w") as f:
    json.dump(data, f)              # write to file

with open("data.json") as f:
    print(json.load(f))             # read from file
```

| Feature        | pickle                   | json                    |
| -------------- | ------------------------ | ----------------------- |
| Format         | binary                   | text                    |
| Python objects | almost all               | basic types only        |
| Cross-language | no                       | yes                     |
| Safe to load   | no (untrusted data)      | yes                     |

---

## 5. Regular Expression and Web Scraping

### 5.1 Regular Expressions (`re` module)

A regex is a pattern used to search, match, and replace text.

Common patterns:

| Pattern  | Meaning                         |
| -------- | ------------------------------- |
| `.`      | any character except newline    |
| `\d`     | a digit                         |
| `\w`     | letter, digit or underscore     |
| `\s`     | whitespace                      |
| `^` `$`  | start / end of string           |
| `*`      | 0 or more                       |
| `+`      | 1 or more                       |
| `?`      | 0 or 1                          |
| `{n}`    | exactly n times                 |
| `[abc]`  | one of a, b, c                  |
| `(...)`  | capture group                   |
| `\|`     | OR                              |

```python
import re

text = "Call 9876543210 or 9123456780. Mail: asha@example.com"

print(re.findall(r"\d{10}", text))              # ['9876543210', '9123456780']
print(re.search(r"\w+@\w+\.\w+", text).group()) # asha@example.com
print(re.match(r"Call", text) is not None)      # True (must match at start)
print(re.sub(r"\d", "#", "a1b22"))              # a#b##
print(re.split(r"[,;]", "a,b;c"))               # ['a', 'b', 'c']
```

Validation example:

```python
def valid_mobile(num):
    return bool(re.fullmatch(r"[6-9]\d{9}", num))

print(valid_mobile("9876543210"))   # True
print(valid_mobile("1234567890"))   # False
```

Groups:

```python
m = re.search(r"(\d{2})-(\d{2})-(\d{4})", "Date: 26-10-2026")
print(m.group(1), m.group(2), m.group(3))   # 26 10 2026
```

### 5.2 Web Scraping

Extracting data from web pages. Install first: `pip install requests beautifulsoup4`

```python
import requests
from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url, timeout=10)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    print(soup.title.text)                      # page title

    for link in soup.find_all("a"):             # all links
        print(link.get("href"), link.text)

    for p in soup.select("p"):                  # CSS selector
        print(p.get_text(strip=True))
```

Good practice:

- Check the site's `robots.txt` and terms of service before scraping.
- Add delays between requests so you do not overload the server.
- Prefer an official API if one exists.

---

## 6. Multithreading

A **thread** is a lightweight unit of execution inside a process. Threads let a program do several things at once, which is most useful for **I/O-bound** work (network, files). Because of the GIL (Global Interpreter Lock), threads do not speed up CPU-bound Python code. Use `multiprocessing` for that.

### 6.1 Basic Threads

```python
import threading
import time

def task(name):
    for i in range(3):
        print(f"{name}: {i}")
        time.sleep(1)

t1 = threading.Thread(target=task, args=("T1",))
t2 = threading.Thread(target=task, args=("T2",))

t1.start()
t2.start()
t1.join()      # wait for t1 to finish
t2.join()
print("All done")
```

### 6.2 Race Condition and Lock

```python
import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        with lock:             # only one thread at a time
            counter += 1

threads = [threading.Thread(target=increment) for _ in range(4)]
for t in threads: t.start()
for t in threads: t.join()

print(counter)    # 400000 (without the lock the result can be wrong)
```

### 6.3 ThreadPoolExecutor (recommended)

```python
from concurrent.futures import ThreadPoolExecutor
import time

def download(n):
    time.sleep(1)
    return f"file {n} done"

with ThreadPoolExecutor(max_workers=3) as pool:
    results = list(pool.map(download, range(5)))

print(results)
```

### 6.4 Daemon Threads

```python
t = threading.Thread(target=task, args=("bg",), daemon=True)
# daemon threads stop automatically when the main program exits
```

---

## 7. Python Database Connectivity (PDBC)

Python talks to databases through a driver that follows the DB-API standard. The steps are the same for every database.

1. Import the driver
2. Connect
3. Create a cursor
4. Execute SQL
5. Commit (for changes) and fetch (for queries)
6. Close

### 7.1 SQLite (built in, no install)

```python
import sqlite3

conn = sqlite3.connect("school.db")
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        marks INTEGER
    )
""")

# Insert (use ? placeholders, never string formatting)
cur.execute("INSERT INTO students (name, marks) VALUES (?, ?)", ("Asha", 90))
cur.executemany(
    "INSERT INTO students (name, marks) VALUES (?, ?)",
    [("Ravi", 75), ("Meena", 88)],
)
conn.commit()

# Select
cur.execute("SELECT * FROM students WHERE marks > ?", (80,))
for row in cur.fetchall():
    print(row)              # (1, 'Asha', 90) ...

# Update and Delete
cur.execute("UPDATE students SET marks = ? WHERE name = ?", (95, "Asha"))
cur.execute("DELETE FROM students WHERE name = ?", ("Ravi",))
conn.commit()

conn.close()
```

> Always use placeholders. Building SQL with f-strings opens the door to **SQL injection**.

### 7.2 MySQL (needs `pip install mysql-connector-python`)

```python
import mysql.connector

conn = mysql.connector.connect(
    host="localhost", user="root", password="your_password", database="school"
)
cur = conn.cursor()
cur.execute("SELECT * FROM students WHERE marks > %s", (80,))   # note %s here
print(cur.fetchall())
conn.close()
```

### 7.3 Using a Context Manager and Error Handling

```python
import sqlite3
from contextlib import closing

try:
    with closing(sqlite3.connect("school.db")) as conn:
        with conn:                    # auto commit / rollback
            conn.execute("INSERT INTO students (name, marks) VALUES (?, ?)", ("Zoya", 70))
except sqlite3.Error as e:
    print("Database error:", e)
```

---

## 8. Decorators

A **decorator** is a function that takes another function, adds behaviour, and returns it, without changing the original code. It builds on the fact that functions are first-class objects in Python.

### 8.1 Basic Decorator

```python
def my_decorator(func):
    def wrapper():
        print("Before the function")
        func()
        print("After the function")
    return wrapper

@my_decorator            # same as: say_hi = my_decorator(say_hi)
def say_hi():
    print("Hi!")

say_hi()
# Before the function
# Hi!
# After the function
```

### 8.2 With Arguments and Return Values

```python
import functools

def log_call(func):
    @functools.wraps(func)          # keeps the original name and docstring
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"Returned {result}")
        return result
    return wrapper

@log_call
def add(a, b):
    return a + b

add(2, 3)
```

### 8.3 Practical Example: Timing

```python
import time, functools

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.perf_counter() - start:.4f}s")
        return result
    return wrapper

@timer
def slow():
    time.sleep(1)

slow()
```

### 8.4 Decorator with Its Own Arguments

```python
def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def hello():
    print("Hello")

hello()   # prints Hello three times
```

### 8.5 Built-in Decorators

`@staticmethod`, `@classmethod`, `@property`, `@functools.lru_cache` (caching):

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)

print(fib(50))   # fast, thanks to caching
```

---

## 9. Generators

A **generator** produces values one at a time, on demand, instead of building the whole collection in memory. It uses `yield` instead of `return` and remembers its state between calls.

### 9.1 Generator Function

```python
def count_up(n):
    i = 1
    while i <= n:
        yield i          # pause here, hand back i
        i += 1

gen = count_up(3)
print(next(gen))   # 1
print(next(gen))   # 2
print(next(gen))   # 3
# next(gen) now raises StopIteration

for x in count_up(3):    # a for loop handles StopIteration for you
    print(x)
```

### 9.2 Generator Expression

```python
squares_list = [x * x for x in range(1_000_000)]   # builds a million items in memory
squares_gen  = (x * x for x in range(1_000_000))   # lazy, tiny memory

print(sum(squares_gen))
```

### 9.3 Why Use Generators

```python
import sys
print(sys.getsizeof([x for x in range(100000)]))   # large
print(sys.getsizeof(x for x in range(100000)))     # small and constant
```

### 9.4 Practical Example: Reading a Huge File

```python
def read_large_file(path):
    with open(path) as f:
        for line in f:
            yield line.strip()

for line in read_large_file("notes.txt"):
    print(line)
```

### 9.5 Infinite Generator

```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen = fibonacci()
print([next(gen) for _ in range(8)])   # [0, 1, 1, 2, 3, 5, 8, 13]
```

| Feature | Iterator/List       | Generator          |
| ------- | ------------------- | ------------------ |
| Memory  | stores all values   | one value at a time|
| Reuse   | can iterate again   | single pass        |
| Syntax  | return / list       | yield              |

---

## 10. Logging Module

`logging` records what a program is doing. It is better than `print` because it has levels, timestamps, and can write to files.

### 10.1 Levels (lowest to highest)

| Level      | Value | Use                           |
| ---------- | ----- | ----------------------------- |
| `DEBUG`    | 10    | detailed diagnostic info      |
| `INFO`     | 20    | normal progress               |
| `WARNING`  | 30    | something unexpected (default threshold) |
| `ERROR`    | 40    | a task failed                 |
| `CRITICAL` | 50    | the program may stop          |

### 10.2 Basic Setup

```python
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(message)s",
    filename="app.log",          # omit to log to the console
)

logging.debug("Debugging details")
logging.info("Program started")
logging.warning("Disk space low")
logging.error("Could not open file")
logging.critical("System crash")
```

### 10.3 Logging Exceptions

```python
try:
    1 / 0
except ZeroDivisionError:
    logging.exception("Math error")    # logs the message plus the full traceback
```

### 10.4 Named Loggers with Handlers

```python
import logging

logger = logging.getLogger("myapp")
logger.setLevel(logging.DEBUG)

console = logging.StreamHandler()
console.setLevel(logging.INFO)

file = logging.FileHandler("myapp.log")
file.setLevel(logging.DEBUG)

fmt = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
console.setFormatter(fmt)
file.setFormatter(fmt)

logger.addHandler(console)
logger.addHandler(file)

logger.info("Shown in console and file")
logger.debug("Only in the file")
```

---

## 11. Assertions

An **assertion** checks that a condition is true. If it is false, Python raises `AssertionError`. Use assertions to catch **programmer mistakes** while developing. Do not use them to validate user input.

```python
assert condition, "optional error message"
```

```python
def average(numbers):
    assert len(numbers) > 0, "List must not be empty"
    return sum(numbers) / len(numbers)

print(average([10, 20, 30]))   # 20.0
print(average([]))             # AssertionError: List must not be empty
```

```python
x = 10
assert x > 5            # passes silently
assert x > 50, "x is too small"   # AssertionError: x is too small
```

Notes:

- Assertions are removed when Python runs with the `-O` flag (`python -O script.py`), so never rely on them for security or required checks.
- For user input use `if` plus `raise ValueError` instead.

---

## 12. NumPy

NumPy provides fast multi-dimensional arrays and math functions. Install: `pip install numpy`

### 12.1 Creating Arrays

```python
import numpy as np

a = np.array([1, 2, 3, 4])
m = np.array([[1, 2, 3], [4, 5, 6]])

print(a.shape, m.shape)         # (4,) (2, 3)
print(m.ndim, m.dtype, m.size)  # 2 int64 6

np.zeros((2, 3))         # 2x3 of zeros
np.ones((2, 2))          # 2x2 of ones
np.arange(0, 10, 2)      # [0 2 4 6 8]
np.linspace(0, 1, 5)     # [0. 0.25 0.5 0.75 1.]
np.random.rand(2, 2)     # random values in [0, 1)
np.eye(3)                # identity matrix
```

### 12.2 Vectorized Operations (no loops needed)

```python
a = np.array([1, 2, 3, 4])

print(a + 10)       # [11 12 13 14]
print(a * 2)        # [2 4 6 8]
print(a ** 2)       # [ 1  4  9 16]
print(a * a)        # element-wise: [ 1  4  9 16]
print(np.sqrt(a))
```

### 12.3 Indexing, Slicing, Boolean Masks

```python
m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(m[0, 1])       # 2
print(m[:, 0])       # first column: [1 4 7]
print(m[1])          # second row:   [4 5 6]
print(m[:2, 1:])     # [[2 3] [5 6]]

a = np.array([5, 12, 7, 20])
print(a[a > 6])      # [12  7 20]
```

### 12.4 Statistics and Aggregations

```python
a = np.array([[1, 2], [3, 4]])

print(a.sum(), a.mean(), a.max(), a.min(), a.std())
print(a.sum(axis=0))   # column sums: [4 6]
print(a.sum(axis=1))   # row sums:    [3 7]
```

### 12.5 Reshape and Matrix Math

```python
a = np.arange(6).reshape(2, 3)    # [[0 1 2] [3 4 5]]
print(a.T)                        # transpose

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(A @ B)                      # matrix multiplication
print(np.linalg.inv(A))           # inverse
```

### 12.6 Broadcasting

```python
m = np.array([[1, 2, 3], [4, 5, 6]])
row = np.array([10, 20, 30])
print(m + row)        # row is added to every row of m
```

### 12.7 Why NumPy over Lists

- Much faster (compiled C under the hood, vectorized)
- Uses less memory
- Rich math and linear algebra functions

---

## 13. Pandas

Pandas is for tabular data analysis. Its two main structures are **Series** (1D) and **DataFrame** (2D table). Install: `pip install pandas`

### 13.1 Creating Data

```python
import pandas as pd

s = pd.Series([10, 20, 30], index=["a", "b", "c"])

df = pd.DataFrame({
    "name":   ["Asha", "Ravi", "Meena", "Zoya"],
    "age":    [21, 22, 21, 23],
    "marks":  [90, 75, 88, None],
    "city":   ["Pune", "Delhi", "Pune", "Chennai"],
})
print(df)
```

### 13.2 Reading and Writing Files

```python
df = pd.read_csv("students.csv")
df.to_csv("out.csv", index=False)
df = pd.read_excel("students.xlsx")     # needs openpyxl
df = pd.read_json("data.json")
```

### 13.3 Inspecting

```python
df.head()        # first 5 rows
df.tail(3)
df.shape         # (rows, columns)
df.info()        # columns, types, non-null counts
df.describe()    # count, mean, std, min, max for numeric columns
df.columns
```

### 13.4 Selecting

```python
df["name"]                    # one column (Series)
df[["name", "marks"]]         # several columns (DataFrame)
df.loc[0]                     # row by label
df.loc[0, "name"]             # single value
df.iloc[0:2, 0:2]             # by position

df[df["marks"] > 80]                         # filter
df[(df["city"] == "Pune") & (df["age"] > 20)] # multiple conditions (use & |, with brackets)
```

### 13.5 Cleaning Missing Data

```python
df.isnull().sum()                          # count missing per column
df["marks"] = df["marks"].fillna(df["marks"].mean())
df = df.dropna()                           # drop rows with missing values
df = df.drop_duplicates()
```

### 13.6 Adding, Changing, Sorting

```python
df["grade"] = df["marks"].apply(lambda m: "A" if m >= 85 else "B")
df["age_next_year"] = df["age"] + 1
df = df.rename(columns={"name": "student"})
df = df.sort_values("marks", ascending=False)
df = df.drop(columns=["age_next_year"])
```

### 13.7 GroupBy and Aggregation

```python
print(df.groupby("city")["marks"].mean())

print(df.groupby("city").agg(
    students=("name", "count"),
    avg_marks=("marks", "mean"),
))
```

### 13.8 Merging

```python
a = pd.DataFrame({"id": [1, 2, 3], "name": ["A", "B", "C"]})
b = pd.DataFrame({"id": [1, 2, 4], "score": [50, 60, 70]})

print(pd.merge(a, b, on="id", how="inner"))   # rows with matching id
print(pd.merge(a, b, on="id", how="left"))    # keep all of a
print(pd.concat([a, a]))                      # stack vertically
```

---

## 14. Unit Testing

Unit testing checks that small pieces of code (units) work correctly, automatically and repeatedly.

### 14.1 Code to Test (`calculator.py`)

```python
def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

### 14.2 unittest (built in) (`test_calculator.py`)

```python
import unittest
from calculator import add, divide

class TestCalculator(unittest.TestCase):

    def setUp(self):
        # runs before EACH test (prepare data or connections)
        self.x, self.y = 10, 5

    def tearDown(self):
        # runs after EACH test (cleanup)
        pass

    def test_add(self):
        self.assertEqual(add(self.x, self.y), 15)

    def test_add_negative(self):
        self.assertEqual(add(-1, -1), -2)

    def test_divide(self):
        self.assertEqual(divide(self.x, self.y), 2)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(1, 0)

if __name__ == "__main__":
    unittest.main()
```

Run it:

```bash
python -m unittest test_calculator.py -v
```

Common assertion methods:

| Method                         | Checks            |
| ------------------------------ | ----------------- |
| `assertEqual(a, b)`            | `a == b`          |
| `assertNotEqual(a, b)`         | `a != b`          |
| `assertTrue(x)` / `assertFalse(x)` | truthiness    |
| `assertIn(a, b)`               | `a in b`          |
| `assertIsNone(x)`              | `x is None`       |
| `assertAlmostEqual(a, b)`      | floats near-equal |
| `assertRaises(Err)`            | exception raised  |

### 14.3 pytest (popular alternative, `pip install pytest`)

Simpler: plain functions and plain `assert`.

```python
# test_calculator_pytest.py
import pytest
from calculator import add, divide

def test_add():
    assert add(2, 3) == 5

@pytest.mark.parametrize("a, b, expected", [(1, 1, 2), (0, 5, 5), (-1, 1, 0)])
def test_add_many(a, b, expected):
    assert add(a, b) == expected

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)
```

```bash
pytest -v
```

### 14.4 Mocking (isolate from external systems)

```python
from unittest.mock import patch
import requests

def get_status(url):
    return requests.get(url).status_code

@patch("requests.get")
def test_get_status(mock_get):
    mock_get.return_value.status_code = 200      # no real network call
    assert get_status("http://example.com") == 200
```

### 14.5 Good Testing Habits

- One behaviour per test, with a clear name (`test_divide_by_zero`).
- Test normal cases, edge cases (empty, zero, negative), and error cases.
- Tests must be independent of each other and repeatable.
- Mock databases, network, and files so tests are fast and stable.

---

## Quick Revision Summary

| Topic              | Remember                                                      |
| ------------------ | ------------------------------------------------------------- |
| OOPS               | class, object, inheritance, polymorphism, encapsulation, abstraction |
| Exception handling | `try / except / else / finally`, `raise`, custom exceptions   |
| File handling      | `with open(...)`, modes `r w a`, `csv`                        |
| Serialization      | `pickle` (binary, Python only), `json` (text, universal)      |
| Regex / scraping   | `re.findall/search/sub`, `requests` + `BeautifulSoup`         |
| Multithreading     | `threading`, `Lock`, `ThreadPoolExecutor`, good for I/O work  |
| PDBC               | connect, cursor, execute, commit, fetch, close; use placeholders |
| Decorators         | function wrapping a function, `@name`, use `functools.wraps`  |
| Generators         | `yield`, lazy, memory efficient                               |
| Logging            | levels DEBUG to CRITICAL, `basicConfig`, `logging.exception`  |
| Assertions         | `assert cond, msg`, for developer checks only                 |
| NumPy              | fast arrays, vectorized math, slicing, broadcasting           |
| Pandas             | Series / DataFrame, filter, clean, groupby, merge             |
| Unit testing       | `unittest` / `pytest`, test normal, edge, and error cases     |
