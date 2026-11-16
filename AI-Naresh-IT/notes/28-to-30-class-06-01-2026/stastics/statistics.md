# Statistics

Statistics is the base of data analysis and machine learning. This document is the roadmap of the topics, with a short explanation and an example for each.

The code examples read `countries_dummy.xlsx` (195 countries, column `BirthRate`). Run them from the `AI-Naresh-IT` folder, where that file is.

## Roadmap

The full course outline (all 7 parts, with the note for every topic) is in [course-outline.md](course-outline.md).

| # | Topic | In one line |
| - | ----- | ----------- |
| 1 | Population vs sample | The whole group vs a part of it |
| 2 | Descriptive statistics (`.describe`) | Describe the data we have |
| 3 | Inferential statistics | Use a sample to say something about the population |
| 4 | Advanced statistics | Measure how good a model or a difference is |
| 5 | r2, adjusted r2, ANOVA, type 1 and type 2 errors, MAE, MSE, RMSE | The advanced topics in detail |

## 1. Population vs sample

| | Population | Sample |
| - | ---------- | ------ |
| Meaning | The whole group | A part of the group |
| Its numbers are called | **Parameter** | **Statistic** |
| Mean | `μ` | `x̄` |

- **Sampling** -- from the population to the sample (you pick the sample).
- **Inference** -- from the sample to the population (you use the sample to say something about the whole group).
- **Population: parameter. Sample: statistic.** A *parameter* is a number that describes the population. A *statistic* is a number that describes the sample.
- In real work, about **90% of the data we work with is sample data**, because we rarely have the whole population.

```python
import pandas as pd

df = pd.read_excel("countries_dummy.xlsx")
population = df["BirthRate"]                       # all 195 countries
sample = population.sample(n=30, random_state=1)   # 30 countries

print(population.mean())     # 21.09   a parameter (μ)
print(sample.mean())         # 18.57   a statistic (x̄), close to μ but not the same
```

More about sampling techniques and the symbols is in `descriptive-statistics.md`.

## 2. Descriptive statistics (`.describe`)

Descriptive statistics describe the data we already have. In Pandas, `.describe()` gives most of them in one table.

```python
print(df["BirthRate"].describe().round(2))
# count    195.00
# mean      21.09
# std       10.34
# min        8.08
# 25%       13.65
# 50%       17.95
# 75%       24.88
# max       49.76
```

The descriptive statistics have three groups:

### Measure of central tendency (the middle)

| Measure | Meaning | Pandas |
| ------- | ------- | ------ |
| Mean | The average | `s.mean()` |
| Median | The middle value after sorting (the `50%` row of `describe()`) | `s.median()` |
| Mode | The value that appears most often | `s.mode()` |

#### Mean, median and mode in detail

| | Mean | Median | Mode |
| - | ---- | ------ | ---- |
| What it is | The simple average of the data. The most widely used measure of central tendency | The midpoint of the ordered data | The value that occurs most often |
| Formula | `Σx / N` or `(x1 + x2 + ... + xN) / N` | The number at position `(n + 1) / 2` | The value with the highest frequency |
| Outliers | **Easily affected** by outliers | **Not affected** by outliers, so it is often used in academia and data science | Not affected |
| Excel | `=AVERAGE()` | `=MEDIAN()` | `=MODE.SNGL()` (one mode), `=MODE.MULT()` (all the modes) |
| Pandas | `s.mean()` | `s.median()` | `s.mode()` |

- **Median position:** sort the data first. If the position `(n + 1) / 2` is not a whole number, the median is the simple average of the two numbers closest to that position.
- **Mode:** a dataset can have **0 modes** (no value repeats), **1 mode** or **multiple modes**. Use `MODE.MULT()` in Excel when there is more than one mode.

```python
s = pd.Series([2, 4, 4, 4, 5, 5, 7, 9])

print(s.mean())              # 5.0
print((len(s) + 1) / 2)      # 4.5   the position: between the 4th and 5th value
print(s.median())            # 4.5   the average of 4 and 5
print(s.mode().tolist())     # [4]

print(pd.Series([1, 2, 2, 3, 3, 4]).mode().tolist())   # [2, 3]   two modes
print(pd.Series([1, 2, 3]).mode().tolist())            # [1, 2, 3] no value repeats (Excel's MODE.SNGL gives an error)

o = pd.Series([2, 3, 4, 5, 100])                       # one outlier
print(o.mean(), o.median())                            # 22.8  4.0   the mean moves, the median does not
```

### Measure of symmetry (the shape)

| Measure | Meaning | Pandas |
| ------- | ------- | ------ |
| Skewness | Which way the data leans: +ve skew (tail on the right), -ve skew (tail on the left), 0 for symmetric | `s.skew()` |
| Kurtosis | How peaked the curve is and how heavy its tails are: 0 is a normal bell curve | `s.kurt()` |

#### Skewness: class notes (as written)

```text
+ve skew == mean >median & Mode  ( data is at left  & Outlier is at right )

0 skew == (mean = median = mode)data is at center & no outlier )
    this graph is called (normal distribution == bell curve == gausian distribution = 0 symmetric)

-ve skew == mode > median > mean ( data is at right & outlier is at left)
normal distribution == gausian distribution == bell curve
```

### Sample skewness formula

```text
            (1/n) · Σ (xᵢ − x̄)³
skew  =  ─────────────────────────────────
         [ √( (1/(n − 1)) · Σ (xᵢ − x̄)² ) ]³
```

In words: **skewness = the average of the cubed distances from the mean, divided by the cube of the sample standard deviation.**

| Symbol | Meaning |
| ------ | ------- |
| `n` | The number of values in the sample |
| `xᵢ` | Each value (`x₁, x₂ ... xₙ`) |
| `x̄` | The sample mean |
| `Σ` (with `i = 1` to `n`) | Add up for every value |
| `xᵢ − x̄` | How far one value is from the mean (the **deviation**) |
| `√( (1/(n − 1)) · Σ (xᵢ − x̄)² )` | The **sample standard deviation** `s` (it divides by `n − 1`) |

**The formula in 4 steps:**

1. **Find the mean** `x̄`.
2. **Find each deviation** `xᵢ − x̄`.
3. **Top part (the numerator):** cube each deviation, add them up, and divide by `n`. Cubing keeps the **sign**: a value above the mean gives a positive number, a value below the mean gives a negative number. Far values count much more (`6³ = 216`, but `3³ = 27`), so one outlier decides the direction.
4. **Bottom part (the denominator):** find the sample standard deviation `s` and cube it. This makes the result **unit free**, so you can compare the skew of different columns (rupees, years, marks).

**Worked example:** the data is `1, 2, 3, 10` (`n = 4`).

| x | x − x̄ (mean = 4) | (x − x̄)² | (x − x̄)³ |
| - | ------------------ | --------- | --------- |
| 1 | −3 | 9 | −27 |
| 2 | −2 | 4 | −8 |
| 3 | −1 | 1 | −1 |
| 10 | 6 | 36 | 216 |
| **Sum** | 0 | **50** | **180** |

- Top part: `180 / 4 = 45`
- Sample variance: `50 / (4 − 1) = 16.667`, so `s = √16.667 = 4.0825`
- Bottom part: `s³ = 4.0825³ = 68.04`
- **skew = 45 / 68.04 = 0.661**

The result is positive, so this is a **+ve skew**: the outlier `10` is at the right and the mean (4) is above the median (2.5), as your class notes say.

**How to read the result:**

| Result | Meaning |
| ------ | ------- |
| Greater than 0 | +ve skew: the tail (outlier) is at the right, mean > median |
| About 0 | Symmetric: mean = median = mode (a normal bell curve) |
| Less than 0 | -ve skew: the tail (outlier) is at the left, mean < median |

- A common rule of thumb: a skew between -0.5 and 0.5 is nearly symmetric, between 0.5 and 1 (or -1 and -0.5) is moderately skewed, and beyond 1 (or below -1) is highly skewed.
- The skew does not change if you multiply the data by a number or add a number to it. `10, 20, 30, 100` gives the same `0.661`. If you mirror the data (change the sign), only the sign of the skew changes.

```python
import numpy as np
import pandas as pd

def sample_skew(x):
    x = np.asarray(x, dtype=float)
    n = len(x)
    mean = x.mean()
    top = np.sum((x - mean) ** 3) / n                      # (1/n) * sum of the cubed deviations
    s = np.sqrt(np.sum((x - mean) ** 2) / (n - 1))         # sample standard deviation
    return top / s ** 3

print(round(sample_skew([1, 2, 3, 10]), 3))                # 0.661
print(round(sample_skew([1, 2, 3, 3, 3, 4, 5]), 3))        # 0.0     symmetric
print(round(sample_skew([1, 7, 8, 8, 9, 9, 9, 10]), 3))    # -1.495  -ve skew
```

**Pandas `.skew()` gives a different number.** Pandas (and Excel's `SKEW()`) use an *adjusted* version of this formula, which corrects the bias in small samples. Both always have the same sign, but the size is different:

| Data | This formula | Pandas `.skew()` |
| ---- | ------------ | ---------------- |
| `1, 2, 3, 10` | 0.661 | 1.764 |
| `1, 2, 2, 3, 3, 3, 4, 10` | 1.470 | 2.240 |
| `1, 7, 8, 8, 9, 9, 9, 10` | -1.495 | -2.278 |
| `BirthRate` (195 countries) | 1.187 | 1.205 |

- The difference gets smaller as `n` gets bigger (`BirthRate` has 195 values, so 1.187 and 1.205 are close).
- Use one method for all your columns, so the numbers can be compared. In Pandas that is `s.skew()`.

### Kurtosis: class notes (as written)

```text
+ve skew = +ve kurtois  == platykurtic
-ve skew = -ve kurtosi == leptokurtic
0skew == normal distribution == mesokurtic
```

**Read this together with the kurtosis table above.** Skewness and kurtosis are **two different measures**:

| Measure | What it tells | Positive means | Negative means |
| ------- | ------------- | -------------- | -------------- |
| **Skewness** | Which way the data leans | Tail at the right | Tail at the left |
| **Kurtosis** | How peaked the curve is and how heavy its tails are | Sharp peak, heavy tails: **leptokurtic** | Flat top, light tails: **platykurtic** |

- In the class notes the pairs are "+ve skew with platykurtic" and "-ve skew with leptokurtic". The standard names are the other way round: a **positive kurtosis is leptokurtic** and a **negative kurtosis is platykurtic**.
- The normal distribution has 0 skew **and** 0 kurtosis, and it is called **mesokurtic**. That part of the class notes is the same as the standard definition.
- A positive skew does not always come with a positive kurtosis. The data below shows that the two numbers can be different:

| Data (random, 200,000 values) | Skew (about) | Kurtosis (about) | Name |
| ---- | ---- | -------- | ---- |
| Exponential | +1.98 | +5.79 | Right tail, heavy tails (leptokurtic) |
| Beta(2, 5) | +0.60 | -0.13 | Right tail, light tails (slightly platykurtic) |
| Uniform (flat) | 0.0 | -1.20 | Symmetric, flat (platykurtic) |
| Laplace (sharp peak) | 0.0 | +3.02 | Symmetric, sharp peak (leptokurtic) |
| Normal | 0.0 | 0.0 | Symmetric bell curve (mesokurtic) |
| Mirrored exponential | -1.97 | +5.71 | Left tail, heavy tails (leptokurtic) |

```python
import numpy as np
import pandas as pd

rng = np.random.default_rng(1)
beta = pd.Series(rng.beta(2, 5, 200000))          # a right tail with light tails
print(round(beta.skew(), 2), round(beta.kurt(), 2))      # 0.59  -0.14   positive skew, negative kurtosis

laplace = pd.Series(rng.laplace(0, 1, 200000))    # symmetric with a sharp peak
print(round(laplace.skew(), 2), round(laplace.kurt(), 2))  # -0.02  2.85   about zero skew, positive kurtosis
```

(The data is random, so the numbers in the table and in the code differ a little each time. The pattern does not change.)

### Measure of variability (the spread)

| Measure | Meaning | Pandas |
| ------- | ------- | ------ |
| Variance | The spread of the data around the mean | `s.var()` |
| Standard deviation | The square root of the variance | `s.std()` |

```python
bw = df["BirthRate"]

print(bw.mean(), bw.median(), bw.mode().tolist()[:1])   # central tendency
print(round(bw.skew(), 2), round(bw.kurt(), 2))          # symmetry: 1.21 (+ve skew), 0.75
print(round(bw.var(), 2), round(bw.std(), 2))            # variability: 106.83  10.34
```

- `BirthRate` has a +ve skew (1.21) and its mean (21.09) is above its median (17.95).
- The full explanation of each measure, with formulas and examples, is in `descriptive-statistics.md`.

### Variance: population vs sample (the USA and California)

Think of a map. If you measure **every state of the USA**, you have the **population**. If you measure **only California**, you have a **sample** (a part of the USA).

```text
Population variance                      Sample variance

        Σ (xᵢ − μ)²                              Σ (xᵢ − x̄)²
σ²  =  ─────────────                    s²  =  ─────────────
            N                                       n − 1
   (i = 1 to N)                              (i = 1 to n)
```

| | Population variance | Sample variance |
| - | ------------------- | --------------- |
| In the picture | All of the USA | California, a part of the USA |
| Symbol | `σ²` | `s²` |
| Formula | `σ² = Σ(xᵢ − μ)² / N` | `s² = Σ(xᵢ − x̄)² / (n − 1)` |
| Adds up the values | from `i = 1` to `N` | from `i = 1` to `n` |
| Distance is measured from | `μ`, the population mean | `x̄`, the sample mean |
| Divide by | `N`, the population size | `n − 1`, the sample size minus 1 |

- The two formulas look the same. The differences are the **mean** (`μ` or `x̄`) and the **divisor** (`N` or `n − 1`).
- Use the population formula when you have **all** the data. Use the sample formula when you have only a part and want to estimate the variance of the whole group.

### Worked example: population variance

The population is `1, 2, 3, 4, 5`. It has **5 values**, so the **population size** is `N = 5`.

**Step 1: the mean**

```text
μ = (1 + 2 + 3 + 4 + 5) / 5 = 15 / 5 = 3.00
```

**Step 2: the formula**

```text
          Σ (xᵢ − μ)²       (1 − 3)² + (2 − 3)² + (3 − 3)² + (4 − 3)² + (5 − 3)²
σ²  =  ────────────────  =  ───────────────────────────────────────────────────────
              N                                        5
```

| Part | Meaning | In this example |
| ---- | ------- | --------------- |
| `xᵢ` | An **observation** (one value of the population) | `1`, `2`, `3`, `4`, `5`. In `(3 − 3)²` the first `3` is the observation |
| `μ` | The **mean** of the population | `3`. In `(3 − 3)²` the second `3` is the mean |
| `N` | The **population size** | `5` |

**Step 3: the table**

| x | x − μ | (x − μ)² |
| - | ----- | -------- |
| 1 | −2 | 4 |
| 2 | −1 | 1 |
| 3 | 0 | 0 |
| 4 | 1 | 1 |
| 5 | 2 | 4 |
| **Sum** | 0 | **10** |

**Step 4: the result**

```text
σ² = (4 + 1 + 0 + 1 + 4) / 5 = 10 / 5 = 2.00
σ  = √2 = 1.414
```

The **population variance is 2.00** and the population standard deviation is `√2 = 1.414`.

- The deviations (`x − μ`) always add up to 0, so we square them first. Squaring also makes a far value count more.
- If the same five values were a **sample**, the formula divides by `n − 1 = 4`: `s² = 10 / 4 = 2.5` and `s = 1.581`.

```python
import numpy as np
import pandas as pd

x = pd.Series([1, 2, 3, 4, 5])
mu = x.mean()                          # 3.0
print(((x - mu) ** 2).sum())           # 10.0     the sum of the squared deviations
print(((x - mu) ** 2).sum() / len(x))  # 2.0      population variance = 10 / 5

print(np.var(x), round(np.std(x), 3))  # 2.0  1.414    population (divide by N)
print(x.var(), round(x.std(), 3))      # 2.5  1.581    sample (divide by n - 1)
```

In Excel: `=VAR.P()` gives the population variance (2) and `=VAR.S()` gives the sample variance (2.5).

### Worked example: sample variance

Now take the same values `1, 2, 3, 4, 5`, but treat them as a **sample** (a part of a bigger group). The sample has `n = 5` values, and the sample mean is `x̄ = 3`.

```text
          Σ (xᵢ − x̄)²       (1 − 3)² + (2 − 3)² + (3 − 3)² + (4 − 3)² + (5 − 3)²
s²  =  ────────────────  =  ───────────────────────────────────────────────────────
           n − 1                                    4
```

- The top part is the same as before: `4 + 1 + 0 + 1 + 4 = 10`.
- The bottom part is different: we divide by **`n − 1 = 5 − 1 = 4`** (the circled part in the class image), not by `n = 5`.

```text
s² = 10 / 4 = 2.5
s  = √2.5 = 1.581
```

| | Population variance | Sample variance |
| - | ------------------- | --------------- |
| Symbol | `σ²` | `s²` |
| Mean used | `μ` (the population mean) | `x̄` (the sample mean) |
| Divide by | `N = 5` | `n − 1 = 4` |
| Result for `1, 2, 3, 4, 5` | `10 / 5 = 2.00` | `10 / 4 = 2.5` |

The sample variance (2.5) is a little **bigger** than the population variance (2.00), because we divide by a smaller number.

**Why `n − 1`?**

- A sample is closer to **its own** mean `x̄` than to the true mean `μ` of the population, so the squared distances come out too small. If we divided by `n`, the sample variance would usually be **too low**.
- Dividing by `n − 1` corrects this. It is called **Bessel's correction**.
- Another way to see it (degrees of freedom): the deviations `xᵢ − x̄` always add up to 0, so once `n − 1` of them are known, the last one is fixed. Only `n − 1` values are free.

You can see the correction work with a simulation: take many samples of 5 values from a population whose true variance is 100.

```python
import numpy as np
import pandas as pd

x = pd.Series([1, 2, 3, 4, 5])
print(((x - x.mean()) ** 2).sum())     # 10.0   the sum of the squared deviations
print(x.var())                         # 2.5    sample variance: 10 / 4  (Pandas divides by n - 1)
print(round(x.std(), 3))               # 1.581
print(x.var(ddof=0))                   # 2.0    divide by n: the population formula

rng = np.random.default_rng(0)
samples = rng.normal(50, 10, size=(200000, 5))      # 200,000 samples of n = 5, true variance = 100
print(samples.var(axis=1, ddof=0).mean())           # about 80   divide by n: too low
print(samples.var(axis=1, ddof=1).mean())           # about 100  divide by n - 1: correct on average
```

In Excel: `=VAR.S()` gives the sample variance (2.5) and `=STDEV.S()` gives the sample standard deviation (1.581).

### Standard deviation formulas

The standard deviation is the **square root of the variance**. There is one formula for the population and one for the sample.

```text
Population standard deviation          Sample standard deviation

   σ  =  √σ²                              s  =  √s²
```

| | Population standard deviation | Sample standard deviation |
| - | ----------------------------- | ------------------------- |
| Symbol | `σ` (sigma) | `s` |
| Formula | `σ = √σ²` | `s = √s²` |
| In full | `σ = √( Σ(xᵢ − μ)² / N )` | `s = √( Σ(xᵢ − x̄)² / (n − 1) )` |
| Starts from | The population variance `σ²` | The sample variance `s²` |
| For `1, 2, 3, 4, 5` | `σ = √2 = 1.414` | `s = √2.5 = 1.581` |

- **Why take the square root?** The variance is in **squared units** (if the data is in years, the variance is in years²). The square root brings it back to the **same unit as the data**, so it is easier to read and to compare with the mean.
- The sample standard deviation is bigger than the population one for the same numbers, because the sample variance divides by `n − 1`.

```python
import numpy as np
import pandas as pd

x = pd.Series([1, 2, 3, 4, 5])

print(np.sqrt(2.0), np.std(x))          # 1.4142...  1.4142...   σ = √σ²   (population, divide by N)
print(np.sqrt(2.5), x.std())            # 1.5811...  1.5811...   s = √s²   (sample, divide by n - 1)
```

In Excel: `=STDEV.P()` gives the population standard deviation and `=STDEV.S()` gives the sample standard deviation.

## 3. Inferential statistics

Inferential statistics use a **sample** to draw conclusions about the **population**. Two main tools:

| Tool | What it answers |
| ---- | --------------- |
| **Confidence interval** | In what range is the population value? (for example, "95% confident the mean is between 15.3 and 21.9") |
| **Hypothesis test** | Is a difference or an effect real, or only luck in the sample? |

The confidence interval is explained in `descriptive-statistics.md` (section 9).

### Null and alternative hypothesis (notation)

| Hypotheses | Notation |
| ---------- | -------- |
| **Null hypothesis** | `H₀` (H zero, written `H0`) |
| **Alternative hypothesis** | `H₁` or `Hₐ` (written `H1` or `HA`) |

| | Null hypothesis `H0` | Alternative hypothesis `H1` (or `HA`) |
| - | -------------------- | ------------------------------------- |
| Idea | "No difference", "no effect": the situation as it is now | What we suspect or want to show: the opposite of `H0` |
| Sign | Always has an equal sign (`=`, `≤`, `≥`) | `≠`, `>` or `<` |
| In a test | The hypothesis that we test, and try to find evidence **against** | Accepted only if the evidence against `H0` is strong |

**Examples**

| Question | `H0` | `H1` |
| -------- | ---- | ---- |
| Is the mean salary different from $95,000? | `μ = 95,000` | `μ ≠ 95,000` (two-sided) |
| Is the mean salary higher than $95,000? | `μ ≤ 95,000` | `μ > 95,000` (one-sided) |
| Do high income and low income countries have the same mean birth rate? | `μ_high = μ_low` | `μ_high ≠ μ_low` |
| Do all 4 income groups have the same mean birth rate (ANOVA)? | All the means are equal | At least one mean is different |

**The decision**

- Compare the p-value with the limit `α` (usually 0.05).
- `p < α`: **reject `H0`** (there is evidence for `H1`).
- `p ≥ α`: **fail to reject `H0`** (not enough evidence).
- We say "fail to reject `H0`", not "accept `H0`", because a test can show evidence against `H0`, but it can never prove `H0` is true.
- Salary example (z-test): `H0: μ = 95,000`, `z = 1.90`, `p = 0.0576`, which is above 0.05, so we **fail to reject `H0`**.
- The two ways to be wrong are the type 1 and type 2 errors (see "Type 1 and type 2 errors" below): rejecting `H0` when it is true, and failing to reject `H0` when it is false.

### The null hypothesis `H0: μ₀ = $113,000` (accept or reject)

```text
H0:  μ₀ = $113,000

Accept if:  μ₀ is close enough to the true mean μ
Reject if:  μ₀ is too far from the true mean μ
```

| Symbol | Meaning |
| ------ | ------- |
| `μ₀` (mu zero) | The mean that the null hypothesis **claims**: here `$113,000` |
| `μ` | The **true** mean of the population (we do not know it, we only have a sample) |

- Imagine a claim that the mean salary of data scientists is `$113,000`. That claim is `H0`.
- We look at a sample. If the claimed `μ₀` is **close enough** to what the data says about the true mean `μ`, we **accept** `H0` (the class wording).
- If `μ₀` is **too far** from the true mean `μ`, we **reject** `H0`.
- **Who decides "close enough" and "too far"?** The test does: the t-statistic (or z-statistic) says how many standard errors the sample mean is from `μ₀`, and the critical value from the t-table (or z-table) is the limit. Beyond the limit means "too far".

**Careful wording:** a test can never prove `H0` is true. So the exact statistical words are **"fail to reject `H0`"** (the class word is "accept"). Use "reject" and "fail to reject" in your answers when you can.

**Example with the 9 salaries** (`n = 9`, `x̄ = 92,533`, standard error `4,644`, critical t = 2.306 for 95%):

| Claim `H0: μ₀ =` | Distance from the sample mean | t-statistic | Compare with 2.306 | p-value | Decision |
| ---------------- | ----------------------------- | ----------- | ------------------ | ------- | -------- |
| **$113,000** | 20,467 higher, which is 4.41 standard errors | `(92,533 − 113,000) / 4,644 =` **−4.41** | `4.41 > 2.306`: too far | 0.0023 | **Reject `H0`** |
| $95,000 | 2,467 higher, which is 0.53 standard errors | `(92,533 − 95,000) / 4,644 =` **−0.53** | `0.53 < 2.306`: close enough | 0.610 | **Fail to reject `H0`** (accept) |

- `$113,000` is far from the sample: the 95% confidence interval `[81,824 , 103,242]` does **not** contain it, so we reject the claim.
- `$95,000` is inside that interval, so it is close enough.

```python
import numpy as np
from scipy import stats

salary = np.array([78000, 90000, 75000, 117000, 105000, 96000, 89500, 102300, 80000])

t, p = stats.ttest_1samp(salary, 113000)
print(round(t, 2), round(p, 4))        # -4.41  0.0023    p < 0.05: too far, reject H0

t, p = stats.ttest_1samp(salary, 95000)
print(round(t, 2), round(p, 4))        # -0.53  0.6097    p > 0.05: close enough, fail to reject H0
```

### Hypothesis test: the steps

1. **Null hypothesis (H0)** -- "there is no difference". For example: the mean birth rate of high income and low income countries is the same.
2. **Alternative hypothesis (H1)** -- "there is a difference".
3. Run a test and get a **p-value**: how likely the data would look like this if H0 were true.
4. If `p < 0.05` (the usual limit), **reject H0**: the difference is real. Otherwise, you cannot reject it.

```python
from scipy import stats

high = df[df["IncomeGroup"] == "High income"]["BirthRate"]
low = df[df["IncomeGroup"] == "Low income"]["BirthRate"]

print(high.mean(), low.mean())                    # 13.2   41.3
t, p = stats.ttest_ind(high, low, equal_var=False)
print(round(t, 1), p)                             # -21.5  1.8e-20   p is far below 0.05
```

- The p-value is almost 0, so we reject H0: the birth rate of high income and low income countries is really different.

### The standard normal distribution (standardization)

Standardization changes any dataset so that its **mean is 0** and its **standard deviation is 1**. The result is the **standard normal distribution**, written `N(0, 1)`. It takes two steps.

**The data:** `1, 2, 2, 3, 3, 3, 4, 4, 5` (9 values, mean = 3, standard deviation = 1.22).

| Original dataset `x` | Subtract the mean `x − μ` | Divide by the standard deviation `(x − μ) / σ` |
| -------------------- | ------------------------- | ---------------------------------------------- |
| 1 | −2 | −1.63 |
| 2 | −1 | −0.82 |
| 2 | −1 | −0.82 |
| 3 | 0 | 0.00 |
| 3 | 0 | 0.00 |
| 3 | 0 | 0.00 |
| 4 | 1 | 0.82 |
| 4 | 1 | 0.82 |
| 5 | 2 | 1.63 |
| **Mean** | **3** → **0** | **0.00** |
| **St. dev** | **1.22** → **1.22** | **1.00** |

| Step | Formula | Mean | Standard deviation | Distribution |
| ---- | ------- | ---- | ------------------ | ------------ |
| Original data | `x` | 3 | 1.22 | `N(3, 1.22)` |
| 1. Subtract the mean | `x − μ` | 0 | 1.22 | `N(0, 1.22)` |
| 2. Divide by the standard deviation | `(x − μ) / σ` | 0 | **1** | **`N(0, 1)`** |

- **Subtracting the mean** moves the whole distribution so that it is centred on 0. It does not change the spread.
- **Dividing by the standard deviation** shrinks or stretches the spread to 1. Now one unit means "one standard deviation".
- The new value `z = (x − μ) / σ` is called the **z-score**. It tells how many standard deviations a value is from the mean. For example, `5` is `+1.63` standard deviations above the mean, and `1` is `−1.63` below it.
- This is the distribution behind the **z-table** (see the confidence interval example): the table gives the area to the left of a z-score.

**Standardization in one line**

```text
N ~ (μ, σ²)   ──── standardize ────▶   N ~ (0, 1)

standardized variable  =  (original variable − mean) / standard deviation

z-score  =  (x − μ) / σ
```

| Part | Meaning |
| ---- | ------- |
| `N ~ (μ, σ²)` | **Any** normal distribution: it has mean `μ` and variance `σ²` |
| `N ~ (0, 1)` | The **standard normal distribution**: mean 0 and variance 1 (so also standard deviation 1) |
| `x` | The original value (the original variable) |
| `μ` | The mean |
| `σ` | The standard deviation |
| `z` | The standardized variable, called the **z-score** |

- Standardizing turns any normal distribution into `N ~ (0, 1)`. After that, all values are on the same scale, so you can compare them and look them up in one z-table.
- To go back, use the reverse formula `x = μ + z · σ`. In the example above, `z = 1.63` gives `x = 3 + 1.63 × 1.22 ≈ 5`.

**A note on the notation.** `N ~ (μ, σ²)` has the **variance** `σ²` as the second number. In the example table above, the class notes write `N ~ (3, 1.22)` with the **standard deviation** (1.22) as the second number. As a variance it would be `1.22² = 1.5`, so the same distribution is `N ~ (3, 1.5)`. For `N ~ (0, 1)` there is no difference, because `1² = 1`.

```python
import pandas as pd

x = pd.Series([1, 2, 2, 3, 3, 3, 4, 4, 5])

print(x.mean(), round(x.std(), 2))          # 3.0  1.22

sub = x - x.mean()                          # step 1: subtract the mean
print(sub.tolist())                         # [-2.0, -1.0, -1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 2.0]
print(sub.mean(), round(sub.std(), 2))      # 0.0  1.22

z = sub / x.std()                           # step 2: divide by the standard deviation
print(z.round(2).tolist())                  # [-1.63, -0.82, -0.82, 0.0, 0.0, 0.0, 0.82, 0.82, 1.63]
print(round(z.mean(), 2), round(z.std(), 2))   # 0.0  1.0
```

**Which standard deviation?** The `1.22` in this example is the **sample** standard deviation (`n − 1`): `√(12 / 8) = 1.2247`. If you divide by the **population** standard deviation (`N`), `√(12 / 9) = 1.1547`, the z-scores are a little bigger (`−1.73`, `−0.87`, `0.87`, `1.73`). SciPy's `stats.zscore()` and scikit-learn's `StandardScaler` use the population version, so their numbers differ slightly from the table above. Both give a mean of 0.

### z-score, z-table and z-test (class notes)

```text
z-score == standardize technique to convert mean - 0 & standard deviation 1
           machine learning this concept we called as STANDARDIZATION ( FEATURE SCALING)
           time series model this concept we called as (WHITE NOISE)

z-table == statistic table which help statistician to compute z-test or z-statistic test

z-test == z-test is one of the testing which apply to population data to find
          confidence interval for 95% & 99%
```

| Term | What it is |
| ---- | ---------- |
| **z-score** | A standardizing technique: it converts the data to **mean 0 and standard deviation 1** with `z = (x − μ) / σ` |
| **z-table** | A statistics table that helps a statistician **compute the z-test** (the z-statistic test). It gives the area to the left of a z value |
| **z-test** | A test used with **population data** (the population standard deviation `σ` is known). It is used to find the **confidence interval for 95% and 99%** |

**The z-score has different names in different fields:**

| Field | Name of the concept |
| ----- | ------------------- |
| Statistics | z-score |
| Machine learning | **Standardization** (also called **feature scaling**) |
| Time series | **White noise** (see the note below) |

**Machine learning: standardization (feature scaling).** Features with different scales (age in years, salary in rupees) are converted to mean 0 and standard deviation 1, so that no feature dominates only because its numbers are big.

```python
import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.DataFrame({"age": [22, 35, 58, 41, 29], "salary": [30000, 52000, 90000, 61000, 40000]})
scaled = StandardScaler().fit_transform(df)

print(scaled.round(2))
# [[-1.22 -1.19]
#  [-0.16 -0.13]
#  [ 1.71  1.72]
#  [ 0.33  0.31]
#  [-0.65 -0.71]]
print(scaled.mean(axis=0).round(2), scaled.std(axis=0).round(2))     # [-0. -0.]  [1. 1.]
```

**Time series: white noise.** A white noise series has a mean of 0, a constant spread and **no relation between one value and the next**. A standard white noise is `N ~ (0, 1)`: its values look like standardized data.

- A series that only has mean 0 and standard deviation 1 is not always white noise. The values must also be unrelated to each other (no autocorrelation).

```python
import numpy as np
import pandas as pd

rng = np.random.default_rng(0)
noise = pd.Series(rng.normal(0, 1, 5000))
print(round(noise.mean(), 2), round(noise.std(), 2))     # about 0 and 1
print(round(noise.autocorr(1), 2))                       # about 0: no relation to the previous value

walk = noise.cumsum()                                    # a random walk: not white noise
print(round(walk.autocorr(1), 2))                        # about 1: each value depends on the previous one
```

**z-test with the z-table: an example.** The salary example: `n = 30`, sample mean `x̄ = $100,200`, population standard deviation `σ = $15,000`. Test the claim that the true mean salary is `$95,000`.

| Step | Value |
| ---- | ----- |
| H0 | `μ = 95,000` |
| H1 | `μ ≠ 95,000` |
| Standard error | `σ / √n = 15000 / √30 = 2739` |
| z-statistic | `z = (x̄ − μ0) / (σ / √n) = (100,200 − 95,000) / 2739 = 1.90` |
| Area to the left of 1.90 (z-table, row 1.9, column 0.00) | 0.9713 |
| p-value (two sides) | `2 × (1 − 0.9713) = 0.0574` |
| Decision at 95% (critical z = 1.96) | `1.90 < 1.96`, so **do not reject H0** |

- The z-test uses the z-table the same way as the confidence interval: to turn a z value into an area (a probability).
- At 99% the critical z is 2.576, so the decision is the same here.

```python
import numpy as np
from scipy import stats

n, xbar, sigma, mu0 = 30, 100200, 15000, 95000
z = (xbar - mu0) / (sigma / np.sqrt(n))
p = 2 * (1 - stats.norm.cdf(z))

print(round(z, 2))                    # 1.9
print(round(p, 4))                    # 0.0576   (0.0574 when z is rounded to 1.90 and read from the table)
print(abs(z) > stats.norm.ppf(0.975)) # False: 1.9 is smaller than 1.96, so we do not reject H0 at 95%
```

### Confidence interval when the population standard deviation is known (z-score)

**Example: data scientist salary.** We have a sample of `n = 30` data scientist salaries. The values start like this: `$117,313`, `$104,002`, `$113,038`, `$101,936`, `$84,560`, `$113,136` ...

| Known | Value |
| ----- | ----- |
| Sample size `n` | 30 |
| Sample mean `x̄` | **$100,200** |
| Population standard deviation `σ` | **$15,000** (known) |

When the **population** standard deviation `σ` is **known**, we use the **z-score**. (When it is not known, we use the `t` distribution, as in the earlier example with `s`.)

**The formula**

```text
[  x̄ − z(α/2) · σ/√n  ,  x̄ + z(α/2) · σ/√n  ]
```

| Part | Meaning |
| ---- | ------- |
| `x̄` | The **sample mean** (the centre of the interval) |
| `σ / √n` | The **standard error** |
| `z(α/2)` | The z value for the confidence level (from the z-table) |
| `z(α/2) · σ/√n` | The **margin of error**: how far we go to the left and to the right of `x̄` |

**Step 1: the standard error**

```text
standard error = σ / √n = 15000 / √30 = 2739
```

**Step 2: common confidence levels, α and z**

`α` (alpha) is the chance that the interval misses the true value. For a two-sided interval it is split in two equal tails, `α/2` on each side.

| Confidence level | α | α/2 | Area to the left of z (1 − α/2) | z |
| ---------------- | - | --- | ------------------------------- | - |
| 90% | 10% (0.1) | 0.05 | 0.95 | 1.645 |
| **95%** | **5% (0.05)** | **0.025** | **0.975** | **1.96** |
| 99% | 1% (0.01) | 0.005 | 0.995 | 2.576 |

**Step 3: read z from the z-table (standard normal distribution)**

The z-table gives the **area to the left** of `z`. For 95%: `α = 0.05`, so `α/2 = 0.025` and `z(0.025)` is the z with an area of `1 − 0.025 = 0.975` to its left. Find `0.9750` in the table: the row is **1.9** and the column is **0.06**, so `z = 1.9 + 0.06 =` **1.96**.

| z | 0.04 | 0.05 | 0.06 | 0.07 | 0.08 | 0.09 |
| - | ---- | ---- | ---- | ---- | ---- | ---- |
| 1.8 | 0.9671 | 0.9678 | 0.9686 | 0.9693 | 0.9699 | 0.9706 |
| **1.9** | 0.9738 | 0.9744 | **0.9750** | 0.9756 | 0.9761 | 0.9767 |
| 2.0 | 0.9793 | 0.9798 | 0.9803 | 0.9808 | 0.9812 | 0.9817 |

**Step 4: the interval**

```text
margin of error = 1.96 × 2739 = 5368
95% interval    = [100,200 − 5,368 , 100,200 + 5,368] = [94,832 , 105,568]
```

We are 95% confident that the true mean salary of all data scientists is between **$94,832 and $105,568**.

| Confidence | z | Margin of error | Interval |
| ---------- | - | --------------- | -------- |
| 90% | 1.645 | 4,505 | $95,695 to $104,705 |
| 95% | 1.96 | 5,368 | $94,832 to $105,568 |
| 99% | 2.576 | 7,054 | $93,146 to $107,254 |

A higher confidence gives a **wider** interval.

**What it means (class notes):** a 95% confidence interval means you are sure that in 95% of the cases, the true population parameter would fall into the specified interval.

```python
import numpy as np
from scipy import stats

n, xbar, sigma = 30, 100200, 15000

se = sigma / np.sqrt(n)
print(round(se))                              # 2739   the standard error

z = stats.norm.ppf(1 - 0.05 / 2)              # the z-table lookup: area 0.975 to the left
print(round(z, 2))                            # 1.96

print(xbar - z * se, xbar + z * se)           # 94832.4  105567.6

print(stats.norm.interval(0.95, loc=xbar, scale=se))     # the same interval in one line
print(round(stats.norm.cdf(1.96), 4))                    # 0.975   the area to the left of 1.96 (the table value 0.9750)
```

### Confidence interval when the population standard deviation is unknown (t-score)

**Example: data scientist salary.** We have a sample of `n = 9` salaries, and we do **not** know the population standard deviation. So we use the **sample** standard deviation `s` and the **t-score**.

| Dataset (salary) |
| ---------------- |
| $78,000 |
| $90,000 |
| $75,000 |
| $117,000 |
| $105,000 |
| $96,000 |
| $89,500 |
| $102,300 |
| $80,000 |

| Value | Result |
| ----- | ------ |
| Sample mean `x̄` | **$92,533** |
| Sample standard deviation `s` | **$13,932** |
| Standard error `s / √n` | `13,932 / √9 = 13,932 / 3 =` **$4,644** |

**The two formulas** (the circled `s` and `σ` in the class image are the difference):

| Population variance **unknown** | Population variance **known** |
| ------------------------------- | ----------------------------- |
| `x̄ ± t(n−1, α/2) · s / √n` | `x̄ ± z(α/2) · σ / √n` |
| Uses the sample standard deviation **`s`** | Uses the population standard deviation **`σ`** |
| Uses the **t-score** with `n − 1` degrees of freedom | Uses the **z-score** |

- `n − 1` is the **degrees of freedom** (here `9 − 1 = 8`). The `t` value depends on it.
- The t distribution looks like the normal curve but with **heavier tails**, because `s` is only an estimate of `σ`. So the t-score is **bigger** than the z-score, and the interval is **wider**.
- When `n` is big, `t` gets very close to `z`.

| Degrees of freedom | 2 | 5 | 8 | 10 | 30 | 100 | 1000 | z (infinity) |
| ------------------ | - | - | - | -- | -- | --- | ---- | ------------ |
| t for 95% | 4.303 | 2.571 | **2.306** | 2.228 | 2.042 | 1.984 | 1.962 | 1.960 |

**The 95% interval for the salary example**

```text
t(8, 0.025) = 2.306                      (from the t-table, df = 8, 95%)
margin      = 2.306 × 4,644 = 10,709
interval    = 92,533 ± 10,709 = [81,824 , 103,242]
```

We are 95% confident that the true mean salary is between **$81,824 and $103,242**.

| Confidence | t (df = 8) | Margin | t interval | If we wrongly used z | z interval |
| ---------- | ---------- | ------ | ---------- | -------------------- | ---------- |
| 90% | 1.860 | 8,636 | $83,898 to $101,169 | 1.645 | $84,895 to $100,172 |
| 95% | 2.306 | 10,709 | $81,824 to $103,242 | 1.960 | $83,431 to $101,635 |
| 99% | 3.355 | 15,582 | $76,951 to $108,116 | 2.576 | $80,571 to $104,495 |

The t intervals are wider. Using `z` with a small sample would make the interval look **too narrow** and too sure.

```python
import numpy as np
from scipy import stats

salary = np.array([78000, 90000, 75000, 117000, 105000, 96000, 89500, 102300, 80000])

n = len(salary)
mean = salary.mean()                      # 92533.33
s = salary.std(ddof=1)                    # 13931.89   sample standard deviation (n - 1)
se = s / np.sqrt(n)                       # 4643.96    standard error

t = stats.t.ppf(1 - 0.05 / 2, df=n - 1)   # 2.306      the t-score for 95% and df = 8
print(round(t, 3))

print(mean - t * se, mean + t * se)       # 81824  103242  (rounded)
print(stats.t.interval(0.95, df=n - 1, loc=mean, scale=se))     # the same interval in one line
```

**Which one to use?**

| Situation | Use |
| --------- | --- |
| Population standard deviation `σ` is **known** | z-score: `x̄ ± z(α/2) · σ / √n` |
| `σ` is **unknown** (you only have the sample) | t-score: `x̄ ± t(n−1, α/2) · s / √n` |

In real projects `σ` is almost never known, so the t-score is the one you use most.

### Margin of error (ME)

Both confidence interval formulas have the same shape: **sample mean ± margin of error**.

```text
Population variance known                 Population variance unknown

   x̄ ± z(α/2) · σ/√n                         x̄ ± t(n−1, α/2) · s/√n
      └─────────────┘                           └────────────────┘
       margin of error                            margin of error

                          x̄ ± ME
```

| | Population variance **known** | Population variance **unknown** |
| - | ----------------------------- | ------------------------------- |
| Margin of error `ME` | `z(α/2) · σ / √n` | `t(n−1, α/2) · s / √n` |
| Confidence interval | `x̄ ± ME` | `x̄ ± ME` |
| Salary example | `ME = 1.96 × 2,739 =` **5,368** | `ME = 2.306 × 4,644 =` **10,709** |
| Interval | `100,200 ± 5,368 = [94,832 , 105,568]` | `92,533 ± 10,709 = [81,824 , 103,242]` |

- The **margin of error** is how far we go to the left and to the right of the sample mean. It is **half the width** of the interval: `(105,568 − 94,832) / 2 = 5,368`.
- The interval is `x̄ − ME` to `x̄ + ME`.

**What makes the margin of error bigger or smaller?**

| If this goes up | The margin of error | Example (known `σ = 15,000`, 95%) |
| --------------- | ------------------- | ---------------------------------- |
| Confidence level (90% to 95% to 99%) | Gets **bigger** (a wider net is needed to be more sure) | n = 30: ME = 4,505 (90%), 5,368 (95%), 7,054 (99%) |
| Sample size `n` | Gets **smaller** (more data, a better estimate) | 95%: n = 30 gives 5,368. n = 120 (4 times the data) gives 2,684, half |
| Spread of the data (`σ` or `s`) | Gets **bigger** (more spread, less certainty) | σ = 7,500 at n = 30 gives 2,684 against 5,368 for σ = 15,000 |

- To get a **narrower** interval with the same confidence, you need a **bigger sample**. Because `n` is under a square root, you need **4 times** the data to halve the margin of error.

```python
import numpy as np
from scipy import stats

sigma = 15000
z = stats.norm.ppf(0.975)                               # 1.96

for n in (30, 60, 120, 480):
    print(n, round(z * sigma / np.sqrt(n)))
# 30   5368
# 60   3796
# 120  2684     4 times the data of 30: half the margin of error
# 480  1342
```

### The t-table

**In simple words:** the t-table is a ready-made list of cut-off values. You do not have to work out the cut-off yourself. Look up your degrees of freedom and your confidence level, and you get the number that your `t` must beat. If your `t` is bigger than the cut-off, the result is real. If it is smaller, it can be just luck.

The **t-table** lists the **critical t values**. You read it with two things: the **degrees of freedom** (`df = n − 1`) and the **confidence level**.

| df | 90% (α = 0.10) | 95% (α = 0.05) | 99% (α = 0.01) |
| -- | -------------- | -------------- | -------------- |
| 1 | 6.314 | 12.706 | 63.657 |
| 2 | 2.920 | 4.303 | 9.925 |
| 5 | 2.015 | 2.571 | 4.032 |
| **8** | 1.860 | **2.306** | 3.355 |
| 10 | 1.812 | 2.228 | 3.169 |
| 20 | 1.725 | 2.086 | 2.845 |
| 30 | 1.697 | 2.042 | 2.750 |
| 100 | 1.660 | 1.984 | 2.626 |
| ∞ (like z) | 1.645 | 1.960 | 2.576 |

**How to read it (salary example, `n = 9`, 95%)**

1. Degrees of freedom: `df = n − 1 = 9 − 1 = 8`.
2. Confidence 95%: `α = 0.05`, so `α/2 = 0.025` in each tail.
3. Go to the row `df = 8` and the 95% column: **t = 2.306**.

- The z-table gives the **area** for a z value. The t-table gives the **t value** for a confidence level, and it changes with `df`.
- Some t-tables label the columns with the one-tail area (0.05, 0.025, 0.005). The 95% column is the one for `0.025`, so `t(8, 0.025) = 2.306`.
- A small sample has a big t (`df = 1` gives 12.706). As `df` grows, `t` gets close to `z` (the last row is the z value).

```python
from scipy import stats

print(round(stats.t.ppf(1 - 0.05 / 2, df=8), 3))     # 2.306   the t-table value for df = 8, 95%
print(round(stats.t.ppf(1 - 0.01 / 2, df=8), 3))     # 3.355   99%
print(round(stats.t.ppf(1 - 0.05 / 2, df=1000), 3))  # 1.962   a big df is close to z = 1.96
```

### The t-test

**In simple words:** a t-test checks whether a difference is **real** or just **luck** in the sample.

- Example: our 9 salaries have an average of 92,533. Is the true average really 95,000?
- The test gives a number `t`: **how many standard errors** the sample mean is away from the claim.
- `t` close to **0**: the sample agrees with the claim, so the claim is fine.
- `t` **far from 0** (beyond the cut-off in the t-table): the sample does not agree with the claim, so the claim is probably wrong.
- The t-test is the tool you use every day, because you almost never know the population standard deviation.

The **t-test** checks whether a mean (or the difference of two means) is real, or only luck in the sample. Use it when the **population standard deviation is unknown** and you have only the sample (`s`). With a **known** `σ` use the z-test.

| Type | What it compares | Example |
| ---- | ---------------- | ------- |
| **One-sample** t-test | The mean of one sample with a given number | Is the mean salary $95,000? |
| **Two-sample** (independent) t-test | The means of two separate groups | Birth rate of high income vs low income countries |
| **Paired** t-test | The same group measured twice (before and after) | Marks before and after a training |

| Test | t-statistic | df |
| ---- | ----------- | -- |
| One-sample | `t = (x̄ − μ0) / (s / √n)` | `n − 1` |
| Two-sample (Welch) | `t = (x̄1 − x̄2) / √(s1²/n1 + s2²/n2)` | Worked out from the two samples |
| Paired | `t = d̄ / (s_d / √n)`, where `d` is the difference of each pair | `n − 1` |

**The steps**

1. Write `H0` and `H1`.
2. Calculate the t-statistic.
3. Find the critical t in the **t-table** (with `df` and the confidence level), or the **p-value**.
4. Decide: if `|t|` is bigger than the critical t (or `p < 0.05`), **reject `H0`**. Otherwise **fail to reject `H0`**.

**Example 1: one-sample t-test (the 9 salaries).** `n = 9`, `x̄ = 92,533`, `s = 13,932`, standard error `= 4,644`, `df = 8`, critical t = **2.306** (95%).

| Claim | t-statistic | Compare with 2.306 | p-value | Decision |
| ----- | ----------- | ------------------ | ------- | -------- |
| `H0: μ = 95,000` | `(92,533 − 95,000) / 4,644 =` **−0.53** | `|−0.53| < 2.306` | 0.610 | **Fail to reject `H0`** |
| `H0: μ = 80,000` | `(92,533 − 80,000) / 4,644 =` **2.70** | `2.70 > 2.306` | 0.027 | **Reject `H0`** |

- This matches the 95% confidence interval `[81,824 , 103,242]` from before: it **contains** 95,000 (we cannot reject it) and **does not contain** 80,000 (we reject it).

```python
import numpy as np
from scipy import stats

salary = np.array([78000, 90000, 75000, 117000, 105000, 96000, 89500, 102300, 80000])

t, p = stats.ttest_1samp(salary, 95000)
print(round(t, 3), round(p, 4))      # -0.531  0.6097    p > 0.05: fail to reject H0

t, p = stats.ttest_1samp(salary, 80000)
print(round(t, 3), round(p, 4))      # 2.699   0.0271    p < 0.05: reject H0
```

**Class code: a t-test in Python (units sold).** The class code, as written:

```python
# Hypothesis Testing (t-test)
# Null hypothesis: Mean units sold is equal to 20
# Alternative hypothesis: Mean units sold is not equal to 20

t_statistic, p_value = stats.ttest_1samp(sales_data['units_sold'], 20)

print("\nHypothesis Testing (t-test)")
print(f"t-statistic: {t_statistic}")
print(f"p-value: {p_value}")

# Conclusion
if p_value < 0.05:
    print("Reject the null hypothesis: Mean units sold is significantly different from 20")
else:
    print("Fail to reject the null hypothesis: Mean units sold is not significantly different from 20")
```

| Part | Meaning |
| ---- | ------- |
| `H0` | The mean units sold is equal to 20 (`μ = 20`) |
| `H1` | The mean units sold is **not** equal to 20 (`μ ≠ 20`), a two-sided test |
| `stats.ttest_1samp(data, 20)` | The **one-sample t-test**: compares the mean of the data with the number `20`. It returns two values |
| `t_statistic` | `(x̄ − 20) / (s / √n)`: how many standard errors the sample mean is from 20 |
| `p_value` | The chance of seeing a sample like this if `H0` were true |
| `p_value < 0.05` | The limit `α = 0.05`: below it we **reject `H0`**, otherwise we **fail to reject `H0`** |

The class code needs two things that are not in the snippet: the import `from scipy import stats`, and the data `sales_data` (a DataFrame with a column `units_sold`). A complete example that runs, with made-up sales:

```python
import pandas as pd
from scipy import stats

sales_data = pd.DataFrame({"units_sold": [18, 25, 22, 30, 19, 24, 27, 21, 23, 26, 20, 28]})

t_statistic, p_value = stats.ttest_1samp(sales_data["units_sold"], 20)

print(f"t-statistic: {t_statistic}")     # 3.3077
print(f"p-value: {p_value}")             # 0.00698

if p_value < 0.05:
    print("Reject the null hypothesis: Mean units sold is significantly different from 20")
else:
    print("Fail to reject the null hypothesis: Mean units sold is not significantly different from 20")
# Reject the null hypothesis: Mean units sold is significantly different from 20
```

- The 12 days have a mean of `23.58` units. `t = (23.58 − 20) / 1.083 = 3.31` with `df = 11`, which is beyond the critical value `±2.201`. The p-value `0.007` is below `0.05`, so we **reject `H0`**.
- With sales close to 20 (`18, 22, 19, 21, 20, 23, 17, 21, 19, 22, 24, 18`, mean `20.33`) the same code gives `t = 0.53` and `p = 0.608`, so we **fail to reject `H0`**.
- `ttest_1samp` is two-sided by default (`H1: μ ≠ 20`). For `H1: μ > 20` write `stats.ttest_1samp(data, 20, alternative="greater")`. For `H1: μ < 20` use `alternative="less"`. The one-sided p-value here is `0.0035`, half of the two-sided one.

**Example 2: two-sample t-test.** Do high income and low income countries have the same mean birth rate? (`countries_dummy.xlsx`)

```python
import pandas as pd
from scipy import stats

df = pd.read_excel("countries_dummy.xlsx")
high = df[df["IncomeGroup"] == "High income"]["BirthRate"]      # 66 countries, mean 13.2
low = df[df["IncomeGroup"] == "Low income"]["BirthRate"]        # 28 countries, mean 41.3

t, p = stats.ttest_ind(high, low, equal_var=False)              # Welch's t-test
print(round(t, 1), p)       # -21.5  1.8e-20     p is far below 0.05: reject H0, the means are different
```

**Example 3: paired t-test.** The marks of 5 students before and after a training (made-up numbers).

| Student | 1 | 2 | 3 | 4 | 5 |
| ------- | - | - | - | - | - |
| Before | 60 | 65 | 70 | 55 | 80 |
| After | 66 | 70 | 74 | 60 | 85 |
| Difference | 6 | 5 | 4 | 5 | 5 |

- The differences have mean `d̄ = 5`, standard deviation `s_d = 0.707` and standard error `0.707 / √5 = 0.316`.
- `t = 5 / 0.316 = 15.8`, `df = 4`, critical t = 2.776, so we **reject `H0`**: the training changed the marks.

```python
import numpy as np
from scipy import stats

before = np.array([60, 65, 70, 55, 80])
after = np.array([66, 70, 74, 60, 85])

t, p = stats.ttest_rel(after, before)
print(round(t, 2), round(p, 5))      # 15.81  0.00009     p < 0.05: reject H0
```

**z-test or t-test?**

| | z-test | t-test |
| - | ------ | ------ |
| Population standard deviation `σ` | **Known** | **Unknown** (use the sample `s`) |
| Distribution | Standard normal (z-table) | t distribution (t-table) with `df = n − 1` |
| Typical use | Textbook problems and very large samples | Real projects: the common choice |

## 4. Advanced statistics

The advanced topics: r2, adjusted r2, ANOVA, type 1 and type 2 errors, MAE, MSE and RMSE.

### Advance stats: class notes (as written)

```text
cofdenence interval -- 2 part
population -- z test | sample - t test
99% ml model while we build regression table we will get t-tst only not z-test
p-value =0.05 | y = mx + c | y^ = mx + c
y - actual point | y^ - predicted point | m- slope | x - iv, c -- intercept and constant
y = mx + C this equestion predict the future ?
mae -- absoulte error ( actual - predicted ) | mse ( actual - predict) ** 2
rmse -- root mean squre error np** sqrt (actual - predicte)**2
how to build inferential project & also i shared some the link watch ( keep video)
easy way to forget ( oops, stats ) -- reference
permormance measre of regression model -- r 2 & adjusted r2 | range 0-1
performance measure of classificaiton -- confusion matrix
```

**Where each point is explained in these notes:**

| Class note | Where |
| ---------- | ----- |
| Confidence interval, 2 parts: population is the z-test, sample is the t-test | "Confidence interval when the population standard deviation is known (z-score)" and "... unknown (t-score)", and "z-test or t-test?" |
| p-value = 0.05 | The hypothesis test steps: reject `H0` when `p < 0.05`. See also "Null and alternative hypothesis" |
| `y = mx + c`, `ŷ = mx + c`: `y` actual point, `ŷ` predicted point, `m` slope, `x` independent variable (IV), `c` intercept and constant | "Linear regression model: geometrical representation" ("We can also call it `y = mx + c`") |
| MAE, MSE, RMSE | "MAE, MSE and RMSE: class notes and worked example" |
| Performance measure of a regression model: r2 and adjusted r2, range 0 to 1 | "r2 and adjusted r2" |
| Performance measure of classification: confusion matrix | **Not explained yet** |
| "While we build a regression table we get the t-test only, not the z-test" | "Regression tables (the summary output)" |
| "`y = mx + c`: does this equation predict the future?" | The line gives a **prediction** `ŷ` for a new `x` (for `x = 5` it gave `4.97`). It is a prediction from the pattern in the past data, not a certainty |
| How to build an inferential project, the shared link and the video | Not text, so nothing to add |

### Linear regression model: geometrical representation

```text
ŷᵢ = b₀ + b₁ · xᵢ
```

**We can also call it `y = mx + c`.** It is the same straight line from school, with different names:

| `ŷᵢ = b₀ + b₁ · xᵢ` | `y = m · x + c` | Meaning |
| ------------------- | --------------- | ------- |
| `b₁` | `m` | The slope |
| `b₀` | `c` | The intercept |
| `xᵢ` | `x` | The input |
| `ŷᵢ` | `y` | The output (the predicted value) |

- Only the order is different: `b₀` (the intercept) comes first, and `c` comes last.
- The example line below, `ŷ = 1.24 + 0.74 · x`, is the same as `y = 0.74x + 1.24` (`m = 0.74`, `c = 1.24`).

![Linear regression: the points, the best fit line, the intercept b0 and the slope b1](../image/statistics/linear-regression.png)

| Symbol | Name | Meaning |
| ------ | ---- | ------- |
| `xᵢ` | **Observed value** (of `x`) | The input value of row `i` |
| `yᵢ` | Actual value of `y` | The real output of row `i` (the grey dots) |
| `ŷᵢ` | Predicted value (y hat) | What the line says `y` should be for `xᵢ` |
| `b₀` | **Intercept** | The value of `ŷ` when `x = 0`: **where the line cuts the y axis** |
| `b₁` | **Slope** | How much `ŷ` goes up (or down) when `x` goes up by 1: the steepness of the line |

- The **dots** are the observed data. The **line** is the **best fit line**, the line that is as close as possible to all the dots.
- The vertical distance from a dot to the line is the **error** (the residual): `yᵢ − ŷᵢ`. This is the same error as in MAE and MSE.
- "Best" means the line with the **smallest sum of squared errors** (the least squares method). The line is the one that gives the lowest MSE.
- **Positive slope** (`b₁ > 0`): the line goes up, so `y` grows when `x` grows. **Negative slope**: the line goes down.
- This is the same idea as `y = m1x1 + m2x2 + m3x3 + c` from the variable identification notes. With one variable, `m1 = b₁` and `c = b₀`.

#### Reading a prediction and the error in the picture

![From xj to the predicted value yj on the line, and the estimator of the error e](../image/statistics/linear-regression-error.png)

| In the picture | Name | Meaning |
| -------------- | ---- | ------- |
| `xⱼ` (circled on the x axis) | A value of `x` | The input we want a prediction for |
| `ŷⱼ` (circled on the y axis) | The **predicted value** for `xⱼ` | The height of the line at `xⱼ` |
| Grey dots | **Observed values** | The real data |
| Orange line | The best fit line | `ŷ = b₀ + b₁ · x` |
| Brace between a dot and the line | **Estimator of the error** `êᵢ` | `êᵢ = yᵢ − ŷᵢ`: how far the real dot is from the line |

**How to read the prediction `ŷⱼ`:**

1. Find `xⱼ` on the x axis (here `xⱼ = 3.0`).
2. Go **up** to the line (the dashed vertical line).
3. Go **across** to the y axis (the dashed horizontal line). The value you reach is `ŷⱼ`.
4. With the formula: `ŷⱼ = b₀ + b₁ · xⱼ = 1.24 + 0.74 × 3.0 =` **3.48**.

**How to read the error `êᵢ`:**

- Take a real dot, for example `(x, y) = (4.0, 4.9)`.
- The line says that for `x = 4.0` the prediction is `ŷ = 1.24 + 0.74 × 4.0 = 4.22`.
- The error is `ê = y − ŷ = 4.9 − 4.22 =` **0.68**. This is the length of the brace between the dot and the line.

- A dot **above** the line has a **positive** error. A dot **below** the line has a **negative** error.
- It is called the **estimator of the error** because the true error is not known. We estimate it from the data, using the distance between the dot and the line (also called the residual).
- The best fit line is the line that makes these distances, all squared and added up, as small as possible.

**Example.** 7 points: `x = 1.2, 1.8, 2.4, 3.0, 3.6, 4.0, 4.4` and `y = 1.8, 3.0, 2.6, 4.2, 3.4, 4.9, 4.0`. The best fit line is `ŷ = 1.24 + 0.74 · x`.

| `x` | Actual `y` | Predicted `ŷ` | Error `y − ŷ` |
| --- | ---------- | ------------- | ------------- |
| 1.2 | 1.8 | 2.14 | −0.34 |
| 1.8 | 3.0 | 2.58 | 0.42 |
| 2.4 | 2.6 | 3.03 | −0.43 |
| 3.0 | 4.2 | 3.48 | 0.72 |
| 3.6 | 3.4 | 3.93 | −0.53 |
| 4.0 | 4.9 | 4.22 | 0.68 |
| 4.4 | 4.0 | 4.52 | −0.52 |

- **Intercept** `b₀ = 1.24`: at `x = 0` the line starts at `1.24`.
- **Slope** `b₁ = 0.74`: each time `x` goes up by 1, the prediction goes up by `0.74`.
- To predict for `x = 5`: `ŷ = 1.24 + 0.74 × 5 =` **4.97**.
- The errors add up to 0 (positive and negative balance out). Their squares give `MSE = 0.286`, and `r2 = 0.70`.

```python
import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([1.2, 1.8, 2.4, 3.0, 3.6, 4.0, 4.4])
y = np.array([1.8, 3.0, 2.6, 4.2, 3.4, 4.9, 4.0])

b1, b0 = np.polyfit(x, y, 1)                  # the best fit line: slope first, then intercept
print(round(b0, 2), round(b1, 2))             # 1.24  0.74

model = LinearRegression().fit(x.reshape(-1, 1), y)
print(round(model.intercept_, 2), round(model.coef_[0], 2))     # 1.24  0.74   the same, with scikit-learn

print(round(model.predict([[5]])[0], 2))      # 4.97   the prediction for x = 5

error = y - (b0 + b1 * x)
print(round(error.sum(), 6), round((error ** 2).mean(), 3))     # -0.0  0.286    the errors add up to 0, MSE = 0.286
```

### Error metrics for a model: MAE, MSE, RMSE

A model predicts a value (`ŷ`). The **error** is the actual value minus the predicted value. These metrics summarise the errors. **Smaller is better.**

| Metric | Formula | Meaning |
| ------ | ------- | ------- |
| **MAE** (mean absolute error) | `mean(abs(y − ŷ))` | The average size of the error, in the same unit as `y` |
| **MSE** (mean squared error) | `mean((y − ŷ)²)` | The average of the squared errors. Big errors count much more |
| **RMSE** (root mean squared error) | `√MSE` | MSE brought back to the unit of `y` |

### Sum of squares: SST, SSR and SSE

A regression line explains part of the ups and downs of `y`. The sums of squares measure how much it explains and how much it leaves unexplained.

![SSE, SSR and SST for one point: the distances from the mean, the line and the observed value](../image/statistics/sum-of-squares.png)

Look at one point `yᵢ` in the picture. There are three levels: the mean `ȳ`, the prediction `ŷᵢ` on the line, and the observed value `yᵢ`.

| Name | Formula | Measures | In the picture |
| ---- | ------- | -------- | -------------- |
| **SST** (sum of squares **total**) | `Σ (yᵢ − ȳ)²` | The **total** variability of `y` around its mean | From `ȳ` up to `yᵢ` |
| **SSR** (sum of squares **regression**) | `Σ (ŷᵢ − ȳ)²` | The **explained** variability: how much the **line** explains | From `ȳ` up to `ŷᵢ` |
| **SSE** (sum of squares **error**) | `Σ eᵢ² = Σ (yᵢ − ŷᵢ)²` | The **unexplained** variability: what the regression does **not** explain | From `ŷᵢ` up to `yᵢ` |

**The connection**

```text
SST  =  SSR  +  SSE

Σ (yᵢ − ȳ)²  =  Σ (ŷᵢ − ȳ)²  +  Σ eᵢ²
total        =  explained    +  unexplained
```

- The total distance `yᵢ − ȳ` splits into two parts: `(ŷᵢ − ȳ)` explained by the line, and `(yᵢ − ŷᵢ)` left over as the error.
- A **good line** has a big SSR and a small SSE: it explains most of the total.
- The best fit line is the line with the **smallest SSE**. This is the least squares method.
- **r2 uses these sums:** `r2 = SSR / SST = 1 − SSE / SST`. It is the share of the total variability that the line explains. (See "r2 and adjusted r2".)
- **MSE uses SSE:** `MSE = SSE / n`.

**Class notes (as written):**

```text
SSE -- actual point - predicted for all the datapoint
SSR - predicted point - avg for all the datatpoint
SST -- actual - avg
SST = SSE + SSR
```

The class notes give the idea in words. To get the numbers, each distance is **squared** and then **added up over all the data points** ("for all the datapoint"):

| Class note | In symbols | Meaning |
| ---------- | ---------- | ------- |
| SSE: actual point − predicted, for all the data points | `Σ (actual − predicted)² = Σ (yᵢ − ŷᵢ)²` | The error |
| SSR: predicted point − average, for all the data points | `Σ (predicted − average)² = Σ (ŷᵢ − ȳ)²` | The part the line explains |
| SST: actual − average | `Σ (actual − average)² = Σ (yᵢ − ȳ)²` | The total |
| SST = SSE + SSR | `Σ (yᵢ − ȳ)² = Σ (yᵢ − ŷᵢ)² + Σ (ŷᵢ − ȳ)²` | Total = error + explained |

- "Average" (`avg`) is the mean of `y`, written `ȳ`.
- Without squaring, the distances would add up to 0 (positive and negative cancel), so the sums would be useless.
- The class notes write the sum as `SST = SSE + SSR`. It is the same as `SST = SSR + SSE`, only in a different order.

> **A note on the names.** In these class slides, **SSR means the sum of squares of the _regression_** (the explained part) and **SSE the sum of squares of the _error_**. Some books and software use **SSR for the sum of squares of the _residuals_** (the error part, our SSE) and call the explained part SSM or SSreg. When you read another source, check which one it means.

**Example** (the 7 points of the regression example, `ŷ = 1.24 + 0.74 · x`, mean of `y` `ȳ = 3.414`):

| `x` | `y` | `ŷ` | `(y − ȳ)²` | `(ŷ − ȳ)²` | `e² = (y − ŷ)²` |
| --- | --- | --- | ---------- | ---------- | ---------------- |
| 1.2 | 1.8 | 2.14 | 2.606 | 1.630 | 0.114 |
| 1.8 | 3.0 | 2.58 | 0.172 | 0.689 | 0.173 |
| 2.4 | 2.6 | 3.03 | 0.663 | 0.147 | 0.186 |
| 3.0 | 4.2 | 3.48 | 0.617 | 0.004 | 0.521 |
| 3.6 | 3.4 | 3.93 | 0.000 | 0.261 | 0.276 |
| 4.0 | 4.9 | 4.22 | 2.207 | 0.654 | 0.458 |
| 4.4 | 4.0 | 4.52 | 0.343 | 1.225 | 0.271 |
| **Sum** | | | **SST = 6.609** | **SSR = 4.610** | **SSE = 1.999** |

- `SSR + SSE = 4.610 + 1.999 = 6.609 = SST`. The connection holds.
- `r2 = SSR / SST = 4.610 / 6.609 =` **0.698**. The line explains about 70% of the variability of `y`.
- `MSE = SSE / n = 1.999 / 7 = 0.286`.

```python
import numpy as np

x = np.array([1.2, 1.8, 2.4, 3.0, 3.6, 4.0, 4.4])
y = np.array([1.8, 3.0, 2.6, 4.2, 3.4, 4.9, 4.0])

b1, b0 = np.polyfit(x, y, 1)
y_hat = b0 + b1 * x
y_bar = y.mean()                          # 3.414

sst = ((y - y_bar) ** 2).sum()            # 6.609   total
ssr = ((y_hat - y_bar) ** 2).sum()        # 4.610   explained by the regression
sse = ((y - y_hat) ** 2).sum()            # 1.999   error (unexplained)

print(round(sst, 3), round(ssr, 3), round(sse, 3))     # 6.609  4.61  1.999
print(round(ssr + sse, 3))                              # 6.609   SST = SSR + SSE
print(round(ssr / sst, 3), round(1 - sse / sst, 3))     # 0.698  0.698   r2 two ways
print(round(sse / len(y), 3))                           # 0.286   MSE
```

### R² = SSR / SST: the share of the variability that the line explains

```text
            SSR       variability explained by the regression
   R²  =  ───────  =  ────────────────────────────────────────
            SST       total variability of the dataset
```

| Part | Meaning |
| ---- | ------- |
| `SSR` | The variability **explained by the regression** (by the line) |
| `SST` | The **total variability** of the dataset |
| `R²` | The share of the total that the line explains: a number from **0 to 1** |

Because `SST = SSR + SSE`, the same number can be written `R² = 1 − SSE / SST` (one minus the share that is **not** explained).

**The scale from 0 to 1**

```text
0 ───────────────────────────────────────────────────────── 1
R² = 0                                                  R² = 1
your regression explains                       your regression explains
NONE of the variability                        ALL of the variability
```

| `R²` | What it means | Example |
| ---- | ------------- | ------- |
| **0** | The regression explains **none** of the variability. The line is flat and no better than just using the mean `ȳ` | `x = 1…5`, `y = 2, 4, 3, 4, 2`: `SSR = 0`, `SST = 4`, so `R² = 0` |
| **0.17** | The line explains a little (a weak fit) | `y = 2, 4, 3, 5, 3`: `SSR = 0.9`, `SST = 5.2`, so `R² = 0.17` |
| **0.70** | The line explains about 70% (a good fit) | The 7 regression points: `SSR = 4.610`, `SST = 6.609`, so `R² = 0.698` |
| **1** | The regression explains **all** of the variability. Every point is exactly on the line (`SSE = 0`) | `y = 2x + 1`: `SSR = SST = 40`, so `R² = 1` |

- A **higher** `R²` is a better fit. `R² = 0.70` means that 70% of the ups and downs of `y` are explained by `x`, and the other 30% is not (it is the error).
- With one input variable, `R²` is the square of the correlation `r` between `x` and `y`: for the 7 points `r = 0.835` and `r² = 0.698`.
- `R²` never goes down when you add a variable to the model. That is why we also look at **adjusted r2**, below.

```python
import numpy as np

def r_squared(x, y):
    b1, b0 = np.polyfit(x, y, 1)
    y_hat = b0 + b1 * x
    ssr = ((y_hat - y.mean()) ** 2).sum()      # explained
    sst = ((y - y.mean()) ** 2).sum()          # total
    return ssr / sst

x = np.array([1, 2, 3, 4, 5.0])
print(round(r_squared(x, np.array([2, 4, 3, 4, 2.0])), 2))     # 0.0    explains none
print(round(r_squared(x, np.array([2, 4, 3, 5, 3.0])), 2))     # 0.17   a weak fit
print(round(r_squared(x, 2 * x + 1), 2))                       # 1.0    explains all

x7 = np.array([1.2, 1.8, 2.4, 3.0, 3.6, 4.0, 4.4])
y7 = np.array([1.8, 3.0, 2.6, 4.2, 3.4, 4.9, 4.0])
print(round(r_squared(x7, y7), 3))                             # 0.698
print(round(np.corrcoef(x7, y7)[0, 1] ** 2, 3))                # 0.698   the same: the correlation squared
```

### r2 and adjusted r2

| Metric | Formula | Meaning |
| ------ | ------- | ------- |
| **r2** (R squared) | `1 − SS_res / SS_tot` | The share of the variation in `y` that the model explains. 1 is perfect, 0 is no better than the mean |
| **adjusted r2** | `1 − (1 − r2) × (n − 1) / (n − p − 1)` | r2 corrected for the number of variables (`p`). It goes down if you add a useless variable |

- `n` is the number of rows and `p` is the number of independent variables.
- r2 never goes down when you add a variable, even a useless one. Adjusted r2 can, so use it to compare models with a different number of variables.

```python
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

y_true = np.array([3, 5, 2, 7])          # actual values
y_pred = np.array([2.5, 5, 4, 8])        # predicted values

mae = mean_absolute_error(y_true, y_pred)
mse = mean_squared_error(y_true, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_true, y_pred)

n, p = len(y_true), 1                     # 4 rows, 1 independent variable
adj_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)

print(mae)       # 0.875    errors: 0.5, 0, 2, 1  -> average 0.875
print(mse)       # 1.3125   squared errors: 0.25, 0, 4, 1 -> average 1.3125
print(rmse)      # 1.1456
print(r2)        # 0.644    the model explains about 64% of the variation
print(adj_r2)    # 0.466
```

### MAE, MSE and RMSE: class notes and worked example

```text
MAE ( MEAN ABSOLUTE ERROR )
    actual - predicted  ==
    (error = residual = loss function = cost function)

MSE ( MEAN SQUARE ERROR )
    (actual - predicted)** 2

RMSE (ROOT MEAN SQUARD ERROR)
    root of (A-P)**2
```

**Reading the class notes:**

- The **error** is `actual − predicted` (`A − P`). Other names for it in the class notes: **residual**, **loss function** and **cost function**.
- **MAE**: take the error, make it positive (absolute value), and **take the average**.
- **MSE**: take the error, **square** it, and take the average.
- **RMSE**: the **square root** of the MSE.

| Metric | Formula | Meaning |
| ------ | ------- | ------- |
| Error (residual) | `A − P` | One prediction: how far it is from the actual value (positive or negative) |
| **MAE** | `mean( abs(A − P) )` | The average size of the error |
| **MSE** | `mean( (A − P)² )` | The average squared error |
| **RMSE** | `√( mean( (A − P)² ) )` | The square root of MSE |

- A note on the words: the **loss** is usually the error of **one** row, and the **cost** is the loss **averaged over all** the rows. In the class notes they are used as the same thing.
- The raw errors cannot be averaged directly: positive and negative errors cancel each other. That is why MAE uses the absolute value and MSE uses the square.

**Worked example.** The actual values are `3, 5, 2, 7` and the predicted values are `2.5, 5, 4, 8`.

| Actual `A` | Predicted `P` | Error `A − P` | abs error `|A − P|` | Squared error `(A − P)²` |
| ---------- | ------------- | ------------- | ------------------- | ------------------------ |
| 3 | 2.5 | 0.5 | 0.5 | 0.25 |
| 5 | 5 | 0 | 0 | 0 |
| 2 | 4 | −2 | 2 | 4 |
| 7 | 8 | −1 | 1 | 1 |
| **Sum** | | **−2.5** | **3.5** | **5.25** |
| **Mean** (÷ 4) | | −0.625 | **0.875** = MAE | **1.3125** = MSE |

- The errors add up to `−2.5`, and they partly cancel. That is why the plain average (`−0.625`) is not used.
- **MAE** `= 3.5 / 4 = 0.875`
- **MSE** `= 5.25 / 4 = 1.3125`
- **RMSE** `= √1.3125 = 1.1456`

**MAE or RMSE?** One big mistake counts much more in MSE and RMSE, because the error is squared. If the last prediction is off by 10 instead of 1 (predicted `17`, actual `7`):

| Metric | Before | After one big error | Change |
| ------ | ------ | ------------------- | ------ |
| MAE | 0.875 | 3.125 | about 3.6 times |
| MSE | 1.3125 | 26.06 | about 20 times |
| RMSE | 1.1456 | 5.105 | about 4.5 times |

- Use **MAE** when all errors matter the same. Use **MSE** or **RMSE** when big errors are much worse than small ones.
- **RMSE** is in the **same unit as `y`** (the MSE is in squared units), so it is easier to explain.
- For all three, a **smaller** value is better.

```python
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, root_mean_squared_error

actual = np.array([3, 5, 2, 7])
predicted = np.array([2.5, 5, 4, 8])

error = actual - predicted                       # [ 0.5  0.  -2.  -1. ]   the error = residual
print(np.abs(error).mean())                      # 0.875     MAE  = mean of |A - P|
print((error ** 2).mean())                       # 1.3125    MSE  = mean of (A - P) ** 2
print(round(np.sqrt((error ** 2).mean()), 4))    # 1.1456    RMSE = root of MSE

print(mean_absolute_error(actual, predicted))                    # 0.875    the same, with scikit-learn
print(mean_squared_error(actual, predicted))                     # 1.3125
print(round(root_mean_squared_error(actual, predicted), 4))      # 1.1456
```

### Regression tables (the summary output)

When we build a regression model, the software (Excel, Python `statsmodels`) prints the result as **regression tables**: a summary output with three blocks. This is the class output (a regression of `y` on `x`, where `x` is the SAT score):

**1. Regression statistics**

| Regression statistics | |
| --------------------- | - |
| Multiple R | 0.637814539 |
| R Square | 0.406807387 |
| Adjusted R Square | 0.399484021 |
| Standard Error | 0.196036444 |
| Observations | 100 |

**2. ANOVA**

| | df | SS | MS | F | Significance F |
| - | -- | -- | -- | - | -------------- |
| Regression | 1 | 2.134773225 | 2.134773225 | 55.54923909 | 8.88714E-11 |
| Residual | 99 | 3.112853281 | 0.038430287 | | |
| Total | 100 | 5.247626506 | | | |

**3. Coefficients**

| | Coefficients | Standard Error | t Stat | P-value | Lower 95% | Upper 95% |
| - | ------------ | -------------- | ------ | ------- | --------- | --------- |
| Intercept | 0.480283003 | 0.384489681 | 1.249144064 | 0.21521022 | −0.284730857 | 1.245296863 |
| x (SAT score) | 0.001549208 | 0.00020786 | 7.453136192 | 8.88714E-11 | 0.001135632 | 0.001962784 |

**How to read each block**

| Part | Meaning | In this output |
| ---- | ------- | -------------- |
| **Multiple R** | The correlation between `y` and the predicted `ŷ`. It is `√R²` | `√0.4068 = 0.6378` |
| **R Square** | `R² = SSR / SST`: the share of the variability explained by the line | `2.1348 / 5.2476 = 0.4068`: the line explains about **41%** |
| **Adjusted R Square** | R² corrected for the number of variables | 0.3995 (a little lower than R²) |
| **Standard Error** | The typical size of an error: `√(SSE / df residual)` = `√MS residual` | `√0.03843 = 0.1960` |
| **Observations** | The number of rows `n` | See the note below |
| **ANOVA: SS** | The sums of squares: regression = **SSR**, residual = **SSE**, total = **SST** | `2.1348 + 3.1129 = 5.2476` |
| **ANOVA: MS** | The mean square: `SS / df` | `3.1129 / df = 0.03843` |
| **F** | `F = MS regression / MS residual`: tests whether the model as a whole is useful | `2.1348 / 0.03843 = 55.55` |
| **Significance F** | The p-value of the F test | `8.9E-11`, far below 0.05: the model is significant |
| **Coefficients** | The fitted line: `b₀` (intercept) and `b₁` (slope) | `ŷ = 0.4803 + 0.001549 · x` |
| **Standard Error** (coefficients) | How much each coefficient can move from sample to sample | 0.3845 and 0.000208 |
| **t Stat** | `coefficient / standard error`: the **t-test** of that coefficient | Slope: `0.001549 / 0.000208 = 7.45` |
| **P-value** | The p-value of that t-test (for `H0: the coefficient = 0`) | Slope: `8.9E-11`. Intercept: `0.2152` |
| **Lower 95% / Upper 95%** | The 95% confidence interval of the coefficient | Slope: `0.001136` to `0.001963` |

**Why the t-test and not the z-test (class note)**

- The coefficients are estimated from a **sample**, and the population standard deviation is **not known**, so the table uses the **t distribution** (with the residual degrees of freedom). That is why the column is called **t Stat**. There is no z-test in a regression table.
- For each coefficient the test is: `H0: the coefficient = 0` (that variable has no effect) and `H1: the coefficient ≠ 0`.
- **Slope:** `t = 7.45`, `p = 8.9E-11 < 0.05`, so we **reject `H0`**: `x` (the SAT score) has a real effect on `y`. The 95% interval (`0.001136` to `0.001963`) does not contain 0.
- **Intercept:** `p = 0.2152 > 0.05`, so we **fail to reject `H0`**: the intercept is not significantly different from 0. The interval (`−0.2847` to `1.2453`) contains 0. (We keep the intercept in the model anyway.)
- **Prediction:** `ŷ = 0.4803 + 0.001549 · x`. For `x = 1800`: `ŷ = 0.4803 + 0.001549 × 1800 =` **3.27**.

**Checking that the numbers fit together** (they are all linked):

| Check | Result |
| ----- | ------ |
| `SSR + SSE = SST` | `2.1348 + 3.1129 = 5.2476` ✓ |
| `R² = SSR / SST` | `0.4068` ✓ |
| `Multiple R = √R²` | `0.6378` ✓ |
| `Standard Error = √MS residual` | `0.1960` ✓ |
| `F = MS regression / MS residual` | `55.55` ✓ |
| `F = t²` (with one `x`) | `7.4531² = 55.55` ✓ |
| Significance F = p-value of the slope (with one `x`) | both `8.88714E-11` ✓ |

> **A note on the degrees of freedom in the picture.** The table shows `df = 1, 99, 100` and `Observations = 100`. For `n` observations and one `x`, the residual df is `n − 2` and the total df is `n − 1`. With 100 observations that would be 98 and 99. The other numbers do not fit 99 either: `MS residual = SS residual / df` gives `3.1129 / 0.03843 = 81`, and the 95% interval, the adjusted R² and the Significance F all match **residual df = 81**, which is **83 observations** (df `1, 81, 82`). So the `df` and `Observations` cells in the picture look like they were changed. The conclusions do not change.

**The same output in Python** (`statsmodels`), on the 7 points of the regression example:

```python
import numpy as np
import statsmodels.api as sm

x = np.array([1.2, 1.8, 2.4, 3.0, 3.6, 4.0, 4.4])
y = np.array([1.8, 3.0, 2.6, 4.2, 3.4, 4.9, 4.0])

model = sm.OLS(y, sm.add_constant(x)).fit()     # add_constant adds the intercept
print(model.summary())                           # the full regression tables

print(round(model.rsquared, 4), round(model.rsquared_adj, 4))   # 0.6975  0.637      R Square, Adjusted R Square
print(round(model.mse_resid ** 0.5, 4), int(model.nobs))        # 0.6323  7         Standard Error, Observations
print(round(model.ess, 3), round(model.ssr, 3), round(model.centered_tss, 3))   # 4.61  1.999  6.609   SSR, SSE, SST
print(round(model.fvalue, 3), round(model.f_pvalue, 4))         # 11.529  0.0193     F, Significance F
print(model.params.round(4))        # [1.2436 0.7448]    Coefficients: intercept, slope
print(model.bse.round(4))           # [0.6825 0.2194]    Standard Error of the coefficients
print(model.tvalues.round(3))       # [1.822  3.395 ]    t Stat
print(model.pvalues.round(4))       # [0.1281 0.0193]    P-value
print(model.conf_int().round(4))    # Lower 95%, Upper 95%
```

- Here the slope has `t = 3.395` and `p = 0.0193 < 0.05`, so `x` has a significant effect. The intercept has `p = 0.1281 > 0.05`.
- The "Standard Error" of the regression here is `√(SSE / (n − 2)) = √(1.999 / 5) = 0.632`. The `MSE` in the error metrics section is `SSE / n = 0.286`. They differ because the regression table divides by the residual degrees of freedom `n − 2`.

### ANOVA (analysis of variance)

- ANOVA compares the **means of 3 or more groups** to see if at least one is different. (A t-test compares only 2 groups.)
- H0: all the group means are equal. It gives an **F value** and a **p-value**.

```python
groups = [g["BirthRate"].values for _, g in df.groupby("IncomeGroup")]    # 4 income groups

F, p = stats.f_oneway(*groups)
print(round(F, 1), p)        # 260.3  3.3e-67   p < 0.05: the average birth rates are not all equal
```

```python
print(df.groupby("IncomeGroup")["BirthRate"].mean().round(2))
# High income            13.23
# Low income             41.29
# Lower middle income    24.08
# Upper middle income    17.37
```

- ANOVA only says that **some** groups are different. It does not say which ones.

### Type 1 and type 2 errors

When we test a hypothesis, our decision can be wrong in two ways:

| | H0 is really true (no difference) | H0 is really false (there is a difference) |
| - | --------------------------------- | ------------------------------------------ |
| **We reject H0** | **Type 1 error** (false positive) | Correct |
| **We do not reject H0** | Correct | **Type 2 error** (false negative) |

| Error | Meaning | Example |
| ----- | ------- | ------- |
| **Type 1** (false positive) | We say there is an effect, but there is none. Its probability is `α` (alpha), usually 0.05 | A spam filter marks a good email as spam. A test says a healthy person is ill |
| **Type 2** (false negative) | We say there is no effect, but there is one. Its probability is `β` (beta) | A spam filter lets a spam email in. A test says an ill person is healthy |

- Lowering the chance of one error usually raises the chance of the other.

## Quick reference

| Term | Meaning |
| ---- | ------- |
| Sampling | Population to sample |
| Inference | Sample to population |
| Parameter / statistic | A number of the population / a number of the sample |
| `.describe()` | Count, mean, std, min, quartiles, max |
| Mean, median, mode | Central tendency |
| Skewness, kurtosis | Symmetry (shape) |
| Variance, standard deviation | Variability (spread) |
| Confidence interval | A range for the population value |
| p-value | Small (< 0.05) means the difference is real |
| MAE, MSE, RMSE | Model errors (smaller is better) |
| r2, adjusted r2 | Share of variation explained (bigger is better) |
| ANOVA | Compare the means of 3 or more groups |
| Type 1 / type 2 error | False positive / false negative |
