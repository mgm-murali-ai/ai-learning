# Course Outline

The 7 parts of the course, with a status for every topic and the note where it is explained.

**Status:** **Covered** = explained in these notes. **Partly** = a short explanation, more can be added. **Not yet** = not in the notes.

## The outline in one table

| # | Part | Topics |
| - | ---- | ------ |
| 1 | **Population and sample** | Sampling technique, inference technique |
| 2 | **Descriptive statistics** | Central tendency, skewness, kurtosis, variance, standard deviation, covariance (correlation) |
| 3 | **Inferential statistics** | Probability, distribution, confidence interval, z-test, t-test, z-table, t-table, z-score, p-value |
| 4 | **Advanced statistics** | Hypothesis testing (`H0`, `H1` or `Ha`: accept `H0` when the mean is close, reject `H0` when it is far), MAE, MSE, RMSE, the regression line (graphical representation, `y = mx + c`, `ŷ = mx + c`), ANOVA, SSR, SST, SSE, r2, adjusted r2, regression table |
| 5 | **Frontend part** | Streamlit, Gradio |
| 6 | **Data analysis libraries** | NumPy, Matplotlib, Pandas, Seaborn |
| 7 | **EDA technique** | Variable identification, univariate analysis, bivariate analysis, outlier treatment, missing value treatment, imputation technique, transformer, variable creation |

## Where to find each topic

### 1. Population and sample

| Topic | Status | Where |
| ----- | ------ | ----- |
| Sampling technique (population to sample) | Covered | [statistics.md](statistics.md) "1. Population vs sample", [descriptive-statistics.md](descriptive-statistics.md) "2. Sampling technique and inference" |
| Inference technique (sample to population) | Covered | The same sections |

### 2. Descriptive statistics

| Topic | Status | Where |
| ----- | ------ | ----- |
| Central tendency: mean, median, mode | Covered | [statistics.md](statistics.md) "Mean, median and mode in detail" |
| Skewness | Covered | [descriptive-statistics.md](descriptive-statistics.md) "4. Skewness", "Sample skewness formula" |
| Kurtosis | Covered | [descriptive-statistics.md](descriptive-statistics.md) "7. Kurtosis" |
| Variance | Covered | "Variance: population vs sample", with the population and sample examples |
| Standard deviation | Covered | "Standard deviation formulas" |
| Correlation | Covered | [pandas.md](pandas.md) "3. Bivariate analysis: correlation" |
| **Covariance** | **Not yet** | |

### 3. Inferential statistics

| Topic | Status | Where |
| ----- | ------ | ----- |
| Probability, distribution | Partly | [descriptive-statistics.md](descriptive-statistics.md) "8. Probability and distributions: the dice example", "5. Normal distribution". Probability rules are not covered |
| z-score (standardization) | Covered | "The standard normal distribution", "Standardization in one line" |
| z-table, z-test | Covered | "z-score, z-table and z-test", "Confidence interval ... known (z-score)" |
| t-table, t-test | Covered | "The t-table", "The t-test", "Confidence interval ... unknown (t-score)" |
| Confidence interval | Covered | [statistics.md](statistics.md) "Inferential statistics", "Margin of error (ME)" |
| p-value | Covered | "Null and alternative hypothesis", "Hypothesis test: the steps" |

### 4. Advanced statistics

| Topic | Status | Where |
| ----- | ------ | ----- |
| Hypothesis testing: `H0`, `H1` or `Ha`, accept and reject | Covered | [statistics.md](statistics.md) "Null and alternative hypothesis (notation)", "The null hypothesis `H0: μ₀ = $113,000`" |
| MAE, MSE, RMSE | Covered | "MAE, MSE and RMSE: class notes and worked example" |
| Graphical representation of the regression line, `y = mx + c`, `ŷ = mx + c` | Covered | "Linear regression model: geometrical representation" |
| ANOVA | Covered | "ANOVA (analysis of variance)": the idea, the ANOVA table in the regression output (SSR, SSE, SST, df, MS, F), and one-way ANOVA (between and within groups) |
| SSR, SST, SSE | Covered | "Sum of squares: SST, SSR and SSE" |
| r2 and adjusted r2 | Covered | "R² = SSR / SST", "r2 and adjusted r2" |
| Regression table | Covered | "Regression tables (the summary output)" |

### 5. Frontend part

| Topic | Status | Where |
| ----- | ------ | ----- |
| Streamlit | Covered | [streamlit.md](streamlit.md) |
| Gradio | Covered | [eda-llm-integration.md](eda-llm-integration.md) "The Gradio application", and the app `statistics\app.py` |

### 6. Data analysis libraries

| Topic | Status | Where |
| ----- | ------ | ----- |
| NumPy | Covered | [numpy-python.md](numpy-python.md) |
| Matplotlib | Partly | [numpy-python.md](numpy-python.md) "Plotting NumPy Data with Matplotlib", and the charts in the other notes |
| Pandas | Covered | [pandas.md](pandas.md) |
| Seaborn | Covered | [pandas.md](pandas.md) "Seaborn Introduction", "Outliers and Data Analysis" |

### 7. EDA technique

| Topic | Status | Where |
| ----- | ------ | ----- |
| Variable identification | Covered | [pandas.md](pandas.md) "EDA: The Foundation of Machine Learning", "1. Variable identification in detail" |
| Univariate and bivariate analysis | Covered | The same section, steps 2 and 3 |
| Outlier treatment | Covered | Step 4, and "Outliers and Data Analysis" |
| Missing value treatment | Covered | Step 5, with the filling example |
| Imputation technique | Covered | Step 6 |
| Transformer, variable creation | Covered | Steps 6 and 7: one-hot encoder and label encoder |

The slide deck for this topic is [eda-automation-using-llm-frameworks.pptx](eda-automation-using-llm-frameworks.pptx). The statistics slides are in [statistics.pptx](statistics.pptx).

## What is not in the notes yet

1. **Covariance** (part 2).
2. **Probability basics** (part 3): the rules, and the other distributions besides the normal and uniform ones.
3. **Matplotlib** (part 6): only a short section so far.
