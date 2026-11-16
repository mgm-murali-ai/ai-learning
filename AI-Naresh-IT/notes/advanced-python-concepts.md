# Advanced Python Concepts

## Conditional Statements & Loops

- A computer needs some logical unit to think. It does this using specific keywords.
- Conditional statements: `if`, `else`, `if else`, nested `if`, `elif else`.
- Loops: `for` loop and `while` loop.
- Loop control: `break`, `continue`, `pass`.
- We are introduced to PyCharm for debugging, to see how every line of code executes.

## Conditional Statements

### if and else

```python
age = 20

if age >= 18:
    print("adult")
else:
    print("minor")
```

- The code under `if` runs only when the condition is `True`. Otherwise the code under `else` runs.
- The code under each keyword is indented (usually 4 spaces).

### elif (if ... elif ... else)

Use `elif` when there are more than two choices. Python checks from the top and stops at the first condition that is `True`.

```python
marks = 75

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")        # this one runs
elif marks >= 50:
    print("C")
else:
    print("Fail")
```

### Nested if

An `if` inside another `if`. The inner condition is checked only when the outer one is `True`.

```python
age = 25
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("Show your ID")
else:
    print("Not allowed")
```

| Statement | Use |
| --------- | --- |
| `if` | Run code when one condition is true |
| `if` ... `else` | Choose between two options |
| `if` ... `elif` ... `else` | Choose between many options |
| Nested `if` | A condition that depends on another condition |

## Loops

A loop repeats a block of code.

| Loop | Use when |
| ---- | -------- |
| `for` loop | We have a **sequence** and iteration (a list, a string, `range()`, the rows of data) |
| `while` loop | We can apply a **condition** and keep going until it becomes `False` |

### for loop

```python
for i in range(1, 4):
    print(i)          # 1 2 3

for n in [4, 7, 10]:
    if n % 2 == 0:
        print(n, "even")
    else:
        print(n, "odd")
# 4 even
# 7 odd
# 10 even
```

### while loop

```python
count = 1

while count <= 3:
    print(count)      # 1 2 3
    count = count + 1
```

- You must change the variable used in the condition (`count` here). If you forget, the loop never stops (an infinite loop).

## break, continue and pass

| Keyword | What it does |
| ------- | ------------ |
| `break` | Breaks the loop (stops it completely) |
| `continue` | Skips the specific condition (the current round) and continues with the next round |
| `pass` | Passes the bug: it does nothing, and the code continues |

```python
for i in range(1, 6):
    if i == 3:
        continue      # skip 3
    if i == 5:
        break         # stop the loop at 5
    print(i)
# 1 2 4
```

```python
for i in range(1, 6):
    if i == 3:
        pass          # does nothing, so 3 is still printed
    print(i)
# 1 2 3 4 5
```

- `pass` is a placeholder. It does nothing but keeps the code valid where a statement is required. It does not fix a bug, it only lets the program continue while you finish that part later.

```python
def todo():
    pass              # empty function, to be written later

for i in range(3):
    pass              # empty loop body
```

## for ... else

- A `for` loop can have an `else` part.
- The `else` runs when the loop **finishes normally** (all rounds completed).
- The `else` is **skipped** if the loop is stopped by `break`.

```python
for i in range(3):
    print(i)
else:
    print("done")
# 0
# 1
# 2
# done
```

### Searching for a value

```python
for n in [3, 5, 7]:
    if n == 4:
        print("found")
        break
else:
    print("not found")      # no break happened, so else runs
# not found

for n in [3, 4, 7]:
    if n == 4:
        print("found")
        break               # break happens, so else is skipped
else:
    print("not found")
# found
```

### Prime number check

```python
for num in (7, 9, 2):
    for i in range(2, num):
        if num % i == 0:
            print(num, "not prime")
            break
    else:
        print(num, "prime")     # no divisor found
# 7 prime
# 9 not prime
# 2 prime
```

| Loop ends by | `else` part |
| ------------ | ----------- |
| Finishing all rounds | Runs |
| `break` | Skipped |

- A `while` loop can have an `else` too, and it works the same way: it runs when the condition becomes `False`, and is skipped by `break`.

```python
count = 1
while count <= 3:
    count += 1
else:
    print("while finished, count =", count)   # while finished, count = 4
```

## Debugging in PyCharm

PyCharm is a Python IDE. Its debugger lets you run the code **one line at a time** and see how every line executes.

1. Click in the gutter (left of the line number) to set a **breakpoint**. The program pauses on that line.
2. Run with **Debug** (`Shift+F9`) instead of Run.
3. Move through the code:

| Action | Shortcut | What it does |
| ------ | -------- | ------------ |
| Step Over | `F8` | Run the current line and go to the next one |
| Step Into | `F7` | Go inside the function called on this line |
| Resume | `F9` | Run until the next breakpoint |

4. The **Variables** panel shows the current value of every variable after each step, so you can see where a value goes wrong.
