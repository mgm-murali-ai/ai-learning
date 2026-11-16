# Functions

## Function arguments

A function argument is categorised into 2 parts:

1. **Formal argument** -- defined at the time of function definition (`def`).
2. **Actual argument** -- the value passed while we call the function.

```python
def add(a, b):        # a and b are formal arguments
    return a + b

print(add(10, 20))    # 10 and 20 are actual arguments -> 30
```

Types of actual arguments:

1. Positional argument
2. Keyword argument
3. Default argument
4. Variable length argument (`*args`)
5. Keyword variable length argument (`**kwargs`)

| Type | How it looks | Matched by |
| ---- | ------------ | ---------- |
| Positional | `intro("Ravi", 25)` | Position (order) |
| Keyword | `intro(age=25, name="Ravi")` | Name |
| Default | `def greet(name, msg="Hello")` | A default value is used when nothing is passed |
| Variable length (`*args`) | `total(1, 2, 3)` | Any number of values, collected as a tuple |
| Keyword variable length (`**kwargs`) | `info(name="Ravi", age=25)` | Any number of `name=value` pairs, collected as a dictionary |

### 1. Positional argument

The values are matched to the formal arguments by **position** (order). Changing the order changes the result.

```python
def intro(name, age):
    print(name, age)

intro("Ravi", 25)     # Ravi 25
intro(25, "Ravi")     # 25 Ravi   (wrong order, wrong meaning)
```

- The number of actual arguments must match the formal arguments, or Python gives a `TypeError`:

```python
intro("Ravi")
# TypeError: intro() missing 1 required positional argument: 'age'
```

### 2. Keyword argument

The values are passed with the **name** of the argument, so the order does not matter.

```python
intro(age=25, name="Ravi")    # Ravi 25
```

- An unknown name gives a `TypeError`, for example `greet(name="A", name2="B")` gives `got an unexpected keyword argument 'name2'`.

### 3. Default argument

A formal argument can have a default value. It is used when the caller does not pass that argument.

```python
def greet(name, msg="Hello"):
    print(msg, name)

greet("Asha")                  # Hello Asha        (default used)
greet("Asha", "Hi")            # Hi Asha           (positional overrides the default)
greet("Asha", msg="Welcome")   # Welcome Asha      (keyword overrides the default)
```

- Default arguments must come **after** the arguments without a default. `def bad(a=1, b)` is a `SyntaxError`.

### 4. Variable length argument (`*args`)

Use `*args` when you don't know how many values will be passed. They are collected into a **tuple**.

```python
def total(*args):
    print(args, sum(args))

total(1, 2, 3)    # (1, 2, 3) 6
total(5)          # (5,) 5
total()           # () 0
```

### 5. Keyword variable length argument (`**kwargs`)

Use `**kwargs` when you don't know how many `name=value` pairs will be passed. They are collected into a **dictionary**.

```python
def info(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key, "=", value)

info(name="Ravi", age=25)
# {'name': 'Ravi', 'age': 25}
# name = Ravi
# age = 25
```

- `args` and `kwargs` are only names. The `*` and `**` are what matter, but `args` and `kwargs` are the usual names.

### All together

The order in the function definition is: normal arguments, default arguments, `*args`, `**kwargs`.

```python
def show(a, b=2, *args, **kwargs):
    print(a, b, args, kwargs)

show(1)                      # 1 2 () {}
show(1, 5, 6, 7, x=9)        # 1 5 (6, 7) {'x': 9}
```

## Why this matters: operator overloading and polymorphism

- Whatever we learn now about function arguments is the same concept used in **operator overloading**, which is part of **polymorphism** (poly = many, morph = form: many forms).
- Operator overloading means the same operator (like `+`) works in a different way for different types of data.

```python
print(1 + 2)          # 3        (adds numbers)
print("a" + "b")      # ab       (joins strings)
print([1] + [2])      # [1, 2]   (joins lists)
```

Your own class can define what `+` means with the special function `__add__`. It takes the two objects as its arguments:

```python
class Money:
    def __init__(self, v):
        self.v = v

    def __add__(self, other):        # called when we write  Money + Money
        return Money(self.v + other.v)

    def __str__(self):
        return f"Money({self.v})"

print(Money(5) + Money(3))           # Money(8)
```

- `Money(5) + Money(3)` is the same as calling `Money(5).__add__(Money(3))`, a function call with arguments.
