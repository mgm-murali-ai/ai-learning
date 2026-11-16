# Components of OOPs

## 1. Class

A class is a collection of 2 things:

1. Variables ✓
2. Functions ✓

## Syntax of a class

```python
class class_name:
    a = 10          # variables
    b = 20

    def A():        # functions
        return

    def B():
        return
```

The whole block above is how you **create a class**.

## Calling the class

```python
x = class_name()
```

## Types of variables in OOPs

### 1. Instance variables

- Belong to a specific object; each object has its own copy.
- Defined inside `__init__` (or any method) using `self`.

```python
class Student:
    def __init__(self, name):
        self.name = name      # instance variable

s1 = Student("Asha")
s2 = Student("Ravi")
print(s1.name, s2.name)       # Asha Ravi
```

### 2. Class variables (static variables)

- Belong to the class; shared by all objects.
- Defined directly inside the class, outside any method.

```python
class Student:
    school = "AI School"      # class variable

    def __init__(self, name):
        self.name = name

print(Student.school)         # AI School
print(Student("Asha").school) # AI School
```

Changing `Student.school = "X"` changes it for all objects.

### 3. Local variables

- Defined inside a method without `self`.
- Exist only while the method runs.

```python
class Student:
    def total(self):
        marks = 90            # local variable
        return marks
```

### Summary

| Type     | Defined where        | Belongs to | Shared? |
|----------|----------------------|------------|---------|
| Instance | inside method, `self.`| object     | No      |
| Class    | inside class body    | class      | Yes     |
| Local    | inside method        | that method call | No |
