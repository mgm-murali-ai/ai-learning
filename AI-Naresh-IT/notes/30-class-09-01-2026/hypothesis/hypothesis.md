# Hypothesis

## What is a hypothesis?

A **hypothesis** is a proposed explanation or prediction that can be tested with evidence. It is an educated guess, stated so that it can be proven wrong.

**Example:** "Students who sleep 8+ hours score higher on exams than students who sleep less."

A good hypothesis is:

- **Testable:** you can collect data to check it.
- **Falsifiable:** some result could show it is wrong.
- **Specific:** it names what is being compared or measured.

---

## Hypothesis in statistics and data science

A hypothesis test uses two competing hypotheses.

| Hypothesis | Symbol | Meaning | Example |
|------------|--------|---------|---------|
| Null | H₀ | No effect or no difference | Sleep has no effect on marks |
| Alternative | H₁ | There is an effect or difference | Sleep affects marks |

### Example: testing a mean

**H₀: μ₀ = $113,000** (the claimed average salary)

- **Accept** (fail to reject) H₀ if μ₀ is close enough to the true mean μ.
- **Reject** H₀ if μ₀ is too far from the true mean μ.

"Close enough" and "too far" are decided using the significance level (α) and the p-value.

### Steps of a hypothesis test

1. State H₀ and H₁.
2. Choose a significance level (α), commonly 0.05.
3. Collect data and compute a test statistic.
4. Compute the **p-value**.
5. Decide:
   - p-value < α: **reject H₀** (evidence supports H₁).
   - p-value ≥ α: **fail to reject H₀** (not enough evidence).

### Types of errors

| Error | Meaning |
|-------|---------|
| Type I (false positive) | Rejecting H₀ when it is actually true |
| Type II (false negative) | Failing to reject H₀ when it is actually false |

### Example in Python (t-test)

```python
from scipy import stats

sleep_8h = [88, 92, 85, 90, 87, 91]
sleep_5h = [75, 80, 72, 78, 74, 79]

t_stat, p_value = stats.ttest_ind(sleep_8h, sleep_5h)
print("p-value:", p_value)

if p_value < 0.05:
    print("Reject H0: sleep affects marks")
else:
    print("Fail to reject H0: no evidence of an effect")
```

---

## Hypothesis in Python (the `hypothesis` library)

`hypothesis` is a **property-based testing** library, related to the unit testing topic. Instead of writing test cases by hand, you describe the kind of input and the library generates many cases, including edge cases (0, negatives, empty lists, huge numbers).

Install: `pip install hypothesis`

### Example 1: property of addition

```python
from hypothesis import given, strategies as st

@given(st.integers(), st.integers())
def test_add_is_commutative(a, b):
    assert a + b == b + a
```

### Example 2: finding a bug

```python
from hypothesis import given, strategies as st

def average(numbers):
    return sum(numbers) / len(numbers)

@given(st.lists(st.integers()))
def test_average_in_range(numbers):
    assert min(numbers) <= average(numbers) <= max(numbers)
```

Hypothesis will find the failing input `[]` (empty list), which raises an error, showing the function needs handling for empty input.

### Example 3: sort property

```python
@given(st.lists(st.integers()))
def test_sorted_is_ordered(xs):
    result = sorted(xs)
    assert all(result[i] <= result[i + 1] for i in range(len(result) - 1))
```

Run with `pytest`:

```bash
pytest -v
```

### Example-based vs property-based testing

| Feature | Example-based (unittest) | Property-based (hypothesis) |
|---------|--------------------------|-----------------------------|
| Inputs | Chosen by you | Generated automatically |
| Edge cases | Only the ones you think of | Finds many you did not think of |
| Failing input | As written | Shrunk to the smallest failing case |

---

## Error terms and metrics (class notes)

**Error** = actual − predicted

In class these names were used for the same idea: **error = residual = loss function = cost function**. (Strictly, "loss" is usually the error for one data point and "cost" is the loss averaged over all points, but the notes treat them together.)

| Metric | Full name | Formula |
|--------|-----------|---------|
| MAE | Mean Absolute Error | mean of \|actual − predicted\| |
| MSE | Mean Squared Error | mean of (actual − predicted)² |
| RMSE | Root Mean Squared Error | √ of mean of (actual − predicted)² |

```python
import numpy as np

A = np.array([100, 200, 300])   # actual
P = np.array([110, 190, 330])   # predicted

mae  = np.mean(np.abs(A - P))        # 16.67
mse  = np.mean((A - P) ** 2)         # 366.67
rmse = np.sqrt(mse)                  # 19.15
```

---

## MAE (Mean Absolute Error)

**MAE** is the average size of the errors between predicted and actual values, ignoring whether each error is too high or too low.

**Formula:** MAE = (1/n) × Σ |yᵢ − ŷᵢ|

- yᵢ = actual value
- ŷᵢ = predicted value
- n = number of data points
- |…| = absolute value (drops the minus sign)

### Example

| Actual | Predicted | Error | \|Error\| |
|--------|-----------|-------|-----------|
| 100 | 110 | −10 | 10 |
| 200 | 190 | +10 | 10 |
| 300 | 330 | −30 | 30 |

MAE = (10 + 10 + 30) / 3 = **16.67**. On average, the predictions are off by about 16.67 units.

### In Python

```python
from sklearn.metrics import mean_absolute_error
import numpy as np

actual    = [100, 200, 300]
predicted = [110, 190, 330]

print(mean_absolute_error(actual, predicted))   # 16.666...

# or with NumPy
print(np.mean(np.abs(np.array(actual) - np.array(predicted))))
```

### Key points

- Same unit as the data (MAE of 16.67 on dollar prices means about $16.67 off on average).
- Lower is better; 0 means perfect predictions.
- Treats all errors equally, so one large error does not dominate it the way it does with MSE or RMSE.
- Commonly used to evaluate regression models.

### Compared with similar metrics

| Metric | Formula idea | Penalizes big errors? |
|--------|-------------|-----------------------|
| MAE | average of \|error\| | No (linear) |
| MSE | average of error² | Yes |
| RMSE | √MSE | Yes, and back in the original unit |

---

## MSE (Mean Squared Error)

**MSE** is the average of the squared differences between predicted and actual values. Squaring makes every error positive and penalizes large errors much more than small ones.

**Formula:** MSE = (1/n) × Σ (yᵢ − ŷᵢ)²

### Example

Using the same data as the MAE example:

| Actual | Predicted | Error | Error² |
|--------|-----------|-------|--------|
| 100 | 110 | −10 | 100 |
| 200 | 190 | +10 | 100 |
| 300 | 330 | −30 | 900 |

MSE = (100 + 100 + 900) / 3 = **366.67** (the MAE for the same data was 16.67). The single error of 30 contributes 900 of the 1100 total, so MSE is dominated by it.

### In Python

```python
from sklearn.metrics import mean_squared_error
import numpy as np

actual    = [100, 200, 300]
predicted = [110, 190, 330]

print(mean_squared_error(actual, predicted))   # 366.666...

# or with NumPy
print(np.mean((np.array(actual) - np.array(predicted)) ** 2))

# RMSE is the square root of MSE
print(np.sqrt(mean_squared_error(actual, predicted)))   # 19.15...
```

### Key points

- Its unit is the square of the data unit (dollars become dollars²), which is hard to interpret. RMSE (√MSE) brings it back to the original unit.
- Lower is better; 0 means perfect predictions.
- It penalizes large errors heavily, so it is sensitive to outliers. Use it when big mistakes are especially costly.
- Squaring makes the function smooth and easy to differentiate, which is why many models use it as their training loss (for example, linear regression).

### MAE vs MSE vs RMSE

| Metric | Formula idea | Unit | Outlier sensitivity |
|--------|-------------|------|---------------------|
| MAE | average of \|error\| | same as data | Low |
| MSE | average of error² | data unit squared | High |
| RMSE | √MSE | same as data | High |

---

## Confusion Matrix (classification models)

MAE, MSE and RMSE are for **regression** models (predicting numbers). For a **classification** model (predicting a class such as spam / not spam) we must check the **confusion matrix**.

A **confusion matrix** (in ML) is a table that compares the model's predicted classes with the actual classes.

| Term | Meaning | Example (disease test) |
|------|---------|------------------------|
| **TP** (True Positive) | Actual positive, predicted positive | Sick, test says sick |
| **TN** (True Negative) | Actual negative, predicted negative | Healthy, test says healthy |
| **FP** (False Positive) | Actual negative, predicted positive | Healthy, test says sick |
| **FN** (False Negative) | Actual positive, predicted negative | Sick, test says healthy |

The first word (True / False) says whether the prediction was right. The second (positive / negative) says what the model predicted.

### Layout

|  | Predicted Positive | Predicted Negative |
|--|--------------------|--------------------|
| **Actual Positive** | TP | FN |
| **Actual Negative** | FP | TN |

### Metrics from the matrix

| Metric | Formula | Meaning |
|--------|---------|---------|
| Accuracy | (TP + TN) / (TP + TN + FP + FN) | Overall share of correct predictions |
| Precision | TP / (TP + FP) | Of predicted positives, how many were really positive |
| Recall | TP / (TP + FN) | Of actual positives, how many were found |
| F1 score | 2 × Precision × Recall / (Precision + Recall) | Balance of precision and recall |

Worked example with TP = 50, TN = 35, FP = 5, FN = 10 (100 cases):

- Accuracy = (50 + 35) / 100 = **0.85**
- Precision = 50 / 55 = **0.91**
- Recall = 50 / 60 = **0.83**
- F1 = 100 / 115 = **0.87**

### In Python

```python
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

y_true = [1, 1, 1, 0, 0, 0, 1, 0]   # actual
y_pred = [1, 0, 1, 0, 1, 0, 1, 0]   # predicted

cm = confusion_matrix(y_true, y_pred)
print(cm)
# [[3 1]     rows = actual (0, 1), columns = predicted (0, 1)
#  [1 3]]    i.e. [[TN, FP], [FN, TP]]

tn, fp, fn, tp = cm.ravel()
print(tp, tn, fp, fn)                      # 3 3 1 1

print(accuracy_score(y_true, y_pred))      # 0.75
print(precision_score(y_true, y_pred))     # 0.75
print(recall_score(y_true, y_pred))        # 0.75
print(f1_score(y_true, y_pred))            # 0.75
```

Note that sklearn orders the matrix as `[[TN, FP], [FN, TP]]`, which differs from the layout table above.

### Which error matters more?

- **FP is costly:** marking a good email as spam. Aim for high precision.
- **FN is costly:** missing a sick patient. Aim for high recall.

---

## Quick summary

- A hypothesis is a testable, falsifiable prediction.
- Statistics: H₀ (no effect) vs H₁ (effect), decided using the p-value and α.
- Python `hypothesis` library: generates test inputs automatically to check properties of your code.
- MAE: average absolute difference between predicted and actual values; lower is better.
- MSE: average squared difference; penalizes large errors and outliers more. RMSE = √MSE.
- Confusion matrix (classification): TP, TN, FP, FN, from which accuracy, precision, recall and F1 are calculated.
