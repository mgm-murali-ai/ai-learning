# Advanced Python

## NumPy

- NumPy is a library (package) that handles multidimensional arrays: 1D, 2D and nD.
- Install: `pip install numpy`. Import: `import numpy as np`.
- A NumPy array holds items of one data type, so it is faster and uses less memory than a Python list.
- 1D array = vector, 2D array = matrix, nD array = tensor (see the Scalar, Vector, Matrix and Tensor section).

```python
import numpy as np

a1 = np.array([1, 2, 3])                 # 1D
a2 = np.array([[1, 2], [3, 4]])          # 2D
a3 = np.zeros((2, 2, 2))                 # nD (here 3D)

print(a1.ndim, a1.shape)   # 1 (3,)
print(a2.ndim, a2.shape)   # 2 (2, 2)
print(a3.ndim, a3.shape)   # 3 (2, 2, 2)
```

### Usages of NumPy

1. Arithmetic operation
2. Statistical operation
3. Bitwise operator
4. Copy & view array
5. Stacking
6. Searching, sorting, counting
7. Math operations
8. Linear algebra
9. Broadcasting
10. Matrix operation

### 1. Arithmetic operation

Operators work element by element.

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)    # [5 7 9]
print(a * b)    # [ 4 10 18]
print(a ** 2)   # [1 4 9]
```

### 2. Statistical operation

```python
x = np.array([1, 2, 3, 4, 5])

print(np.sum(x))      # 15
print(np.mean(x))     # 3.0
print(np.median(x))   # 3.0
print(np.min(x))      # 1
print(np.max(x))      # 5
print(np.std(x))      # 1.414... (standard deviation)
```

### 3. Bitwise operator

```python
print(np.bitwise_and(5, 3))    # 1
print(np.bitwise_or(5, 3))     # 7
print(np.bitwise_xor(5, 3))    # 6
print(np.invert(5))            # -6   (complement ~)
print(np.left_shift(5, 1))     # 10
print(np.right_shift(5, 1))    # 2
```

### 4. Copy & view array

- `view()` -- a new array object that **shares the same data**. Changing the view changes the original.
- `copy()` -- a new array with its **own data**. Changing the copy does not change the original.

```python
a = np.array([1, 2, 3])

v = a.view()
v[0] = 99
print(a)    # [99  2  3]   (original changed)

c = a.copy()
c[1] = 50
print(a)    # [99  2  3]   (original not changed)
print(c)    # [99 50  3]
```

### 5. Stacking (joining arrays)

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.vstack((a, b)))   # [[1 2 3]
                           #  [4 5 6]]   (vertical, as rows)
print(np.hstack((a, b)))   # [1 2 3 4 5 6]   (horizontal)
```

### 6. Searching, sorting, counting

```python
x = np.array([3, 1, 2, 3])

print(np.where(x == 3))          # (array([0, 3]),)  (indexes where value is 3)
print(np.sort(x))                # [1 2 3 3]
print(np.count_nonzero(x == 3))  # 2  (how many 3s)
```

### 7. Math operations

```python
print(np.sqrt([1, 4, 9]))   # [1. 2. 3.]
print(np.power(2, 3))       # 8
print(np.exp(0))            # 1.0
print(np.log(1))            # 0.0
print(np.sin(0))            # 0.0
```

### 8. Linear algebra

```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(np.dot(A, B))        # [[19 22]
                           #  [43 50]]   (matrix multiplication)
print(A.T)                 # [[1 3]
                           #  [2 4]]     (transpose)
print(np.linalg.det(A))    # about -2.0  (determinant)
```

### 9. Broadcasting

Broadcasting lets NumPy do operations on arrays of different shapes by stretching the smaller array to match the bigger one.

```python
a = np.array([1, 2, 3])
print(a + 10)    # [11 12 13]   (10 is stretched to every element)

m = np.array([[1, 2, 3], [4, 5, 6]])
print(m + np.array([10, 20, 30]))   # [[11 22 33]
                                    #  [14 25 36]]   (the row is added to each row)
```

### 10. Matrix operation

```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(A + B)               # [[ 6  8]
                           #  [10 12]]   (addition)
print(A * B)               # [[ 5 12]
                           #  [21 32]]   (element-wise multiplication)
print(A @ B)               # [[19 22]
                           #  [43 50]]   (matrix multiplication, same as np.dot)
print(A.T)                 # [[1 3]
                           #  [2 4]]     (transpose)
print(np.linalg.inv(A))    # [[-2.   1. ]
                           #  [ 1.5 -0.5]]   (inverse)
```

- `*` multiplies element by element. `@` (or `np.dot`) is true matrix multiplication (rows x columns).
- Example: `A @ B` first value = (1 x 5) + (2 x 7) = 19.
- Matrix multiplication needs the columns of the 1st matrix to equal the rows of the 2nd.

## NumPy Practice Topics

Topics: return a row, find a column, reverse an array, specify a position, slicing, `reshape()`, `arange()`, `random.randint()`, `rand()`, min | max, mask (filter).

```python
import numpy as np

m = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
```

### How to return a row and find a column in a matrix

```python
print(m[0])      # [1 2 3]     (row 0)
print(m[1])      # [4 5 6]     (row 1)
print(m[:, 1])   # [2 5 8]     (column 1: all rows, column 1)
print(m[:, 0])   # [1 4 7]     (column 0)
```

- Format: `m[row, column]`. A `:` means "all".

### How to specify a position (indexing)

```python
x = np.array([1, 2, 3, 4])

print(x[0])      # 1   (first)
print(x[-1])     # 4   (last)
print(m[1, 2])   # 6   (row 1, column 2)
```

### Slicing in an array

Same rule as string slicing: `start:stop:step`, and the stop index is not included (`n-1`).

```python
print(x[1:3])        # [2 3]
print(m[0:2, 1:3])   # [[2 3]
                     #  [5 6]]   (rows 0-1, columns 1-2)
```

### How to reverse the array

```python
print(x[::-1])        # [4 3 2 1]
print(np.flip(x))     # [4 3 2 1]
```

### reshape() -- the size must match

- `reshape()` changes the shape of an array without changing its data.
- The number of elements must stay the same (rows x columns = total elements).

```python
a = np.arange(6)

print(a.reshape(2, 3))    # [[0 1 2]
                          #  [3 4 5]]
print(a.reshape(3, -1))   # shape (3, 2)  (-1 means "work it out")
print(a.reshape(4, 2))    # ValueError: cannot reshape array of size 6 into shape (4,2)
```

### arange()

- Like `range()`, but it returns a NumPy array and also accepts decimal steps.

```python
print(np.arange(5))           # [0 1 2 3 4]
print(np.arange(1, 10, 2))    # [1 3 5 7 9]
print(np.arange(0, 1, 0.25))  # [0.   0.25 0.5  0.75]
```

### random.randint() and rand()

- `np.random.randint(low, high, size)` -- random whole numbers from `low` up to `high - 1`.
- `np.random.rand(rows, columns)` -- random decimal numbers **between 0 and 1** (0 included, 1 not included).

```python
print(np.random.randint(10, 40, (2, 3)))   # e.g. [[28 15 33]
                                           #       [12 37 21]]
print(np.random.rand(2, 3))                # e.g. [[0.37 0.95 0.73]
                                           #       [0.60 0.16 0.16]]
```

- The output is random, so your numbers will be different each time.

### min | max

```python
print(np.min(m))          # 1
print(np.max(m))          # 9
print(np.max(m, axis=0))  # [7 8 9]   (max of each column)
print(np.max(m, axis=1))  # [3 6 9]   (max of each row)
```

- `axis=0` works down the columns. `axis=1` works across the rows.

### mask (filter)

A mask is a True/False array. Using it as an index keeps only the elements where the mask is `True`.

```python
x = np.array([5, 12, 8, 20, 3])

mask = x > 7
print(mask)                   # [False  True  True  True False]
print(x[mask])                # [12  8 20]
print(x[x > 7])               # [12  8 20]   (same, in one line)
print(x[(x > 7) & (x < 15)])  # [12  8]      (two conditions, use & not "and")
```

## NumPy Array Manipulation Functions

Array manipulation functions change the shape, order or contents of an array.

```python
import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]])
y = np.array([1, 2, 3])
```

### Changing the shape

| Function                 | What it does                                                                 |
| ------------------------ | ---------------------------------------------------------------------------- |
| `reshape()`            | Changes the shape. The total number of elements must stay the same           |
| `resize()`             | Changes the shape and the size. Extra spots are filled by repeating the data |
| `flatten()`            | Converts to 1D and returns a **copy**                                  |
| `ravel()`              | Converts to 1D and returns a **view** (shares data when possible)      |
| `transpose()` / `.T` | Swaps rows and columns                                                       |

```python
print(a.reshape(3, 2))        # [[1 2]
                              #  [3 4]
                              #  [5 6]]
print(np.resize(y, (2, 3)))   # [[1 2 3]
                              #  [1 2 3]]   (data repeated to fill 6 spots)
print(a.flatten())            # [1 2 3 4 5 6]
print(a.ravel())              # [1 2 3 4 5 6]
print(a.T)                    # [[1 4]
                              #  [2 5]
                              #  [3 6]]
```

### Joining arrays

| Function                    | What it does                                      |
| --------------------------- | ------------------------------------------------- |
| `concatenate()`           | Joins arrays along an existing axis               |
| `vstack()` / `hstack()` | Stacks vertically (rows) / horizontally (columns) |

```python
b = np.array([[7, 8, 9]])
c = np.array([[10], [11]])

print(np.concatenate((a, b), axis=0))   # [[1 2 3]
                                        #  [4 5 6]
                                        #  [7 8 9]]   (adds a row)
print(np.concatenate((a, c), axis=1))   # [[ 1  2  3 10]
                                        #  [ 4  5  6 11]]   (adds a column)
```

- The shapes must match on the other axis, e.g. joining on `axis=0` needs the same number of columns.

### Splitting arrays

```python
x = np.arange(6)                  # [0 1 2 3 4 5]

print(np.split(x, 3))             # [array([0, 1]), array([2, 3]), array([4, 5])]
print(np.split(x, [2, 4]))        # [array([0, 1]), array([2, 3]), array([4, 5])]
                                  # (split at index 2 and index 4)
print(np.array_split(np.arange(7), 3))
                                  # [array([0, 1, 2]), array([3, 4]), array([5, 6])]
```

- `split()` needs equal parts, or it raises an error. `array_split()` allows unequal parts.

### Adding and removing elements

```python
print(np.append(y, 4))       # [1 2 3 4]      (add at the end)
print(np.insert(y, 1, 99))   # [ 1 99  2  3]  (insert 99 before index 1)
print(np.delete(y, 0))       # [2 3]          (delete the item at index 0)
```

- These return a **new array**. The original `y` is not changed.

### Finding unique values

```python
z = np.array([3, 1, 2, 3, 1])

print(np.unique(z))                       # [1 2 3]
values, counts = np.unique(z, return_counts=True)
print(values)                             # [1 2 3]
print(counts)                             # [2 1 2]   (1 appears twice, 2 once, 3 twice)
```

### Repeating

```python
print(np.repeat([1, 2], 3))   # [1 1 1 2 2 2]   (each item repeated)
print(np.tile([1, 2], 3))     # [1 2 1 2 1 2]   (the whole array repeated)
```

### Quick summary

| Need                  | Function                                      |
| --------------------- | --------------------------------------------- |
| Change shape          | `reshape()`, `resize()`                   |
| Make 1D               | `flatten()`, `ravel()`                    |
| Swap rows and columns | `transpose()`, `.T`                       |
| Join                  | `concatenate()`, `vstack()`, `hstack()` |
| Split                 | `split()`, `array_split()`                |
| Add / remove items    | `append()`, `insert()`, `delete()`      |
| Remove duplicates     | `unique()`                                  |
| Repeat                | `repeat()`, `tile()`                      |

## Plotting NumPy Data with Matplotlib

- Matplotlib is a library for drawing graphs (line plots, bar charts and so on). It works well with NumPy arrays.
- Install: `pip install matplotlib`. Import: `import matplotlib.pyplot as plt`.

```python
import matplotlib.pyplot as plt

plt.plot([1, 27, 64, 8])
plt.ylabel('Numbers')
plt.show()
```

| Line                                | What it does                                                             |
| ----------------------------------- | ------------------------------------------------------------------------ |
| `import matplotlib.pyplot as plt` | Imports the plotting module with the short name `plt`                  |
| `plt.plot([1, 27, 64, 8])`        | Draws a line through the values. They are used as the **y** values |
| `plt.ylabel('Numbers')`           | Writes the label `Numbers` on the y axis                               |
| `plt.show()`                      | Opens the window with the graph. Nothing is shown until this is called   |

- With only one list, Matplotlib uses the positions `0, 1, 2, 3` as the **x** values. So the points are `(0, 1)`, `(1, 27)`, `(2, 64)` and `(3, 8)`.
- To give your own x values, pass two lists: `plt.plot(x, y)`.

### With a NumPy array

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 5)          # [0 1 2 3 4]
y = x ** 2                   # [ 0  1  4  9 16]

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('x squared')
plt.title('Square of numbers')
plt.show()
```

| Function         | What it does         |
| ---------------- | -------------------- |
| `plt.xlabel()` | Label for the x axis |
| `plt.ylabel()` | Label for the y axis |
| `plt.title()`  | Title of the graph   |
| `plt.show()`   | Displays the graph   |
