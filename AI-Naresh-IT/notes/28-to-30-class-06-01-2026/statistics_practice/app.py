"""Gradio app for the statistics notebook (code.ipynb).

It does the same steps as the notebook, on any CSV file:
    Step 1-2  load the data (or create the random sales data of the notebook)
    Step 3    descriptive statistics
    Step 4    confidence interval (t-score) and the hypothesis test (one-sample t-test)
    Charts    histogram, box plot by category and bar plot of the totals

Run it:
    pip install gradio pandas numpy scipy seaborn matplotlib
    python app.py
Then open the link that is printed (usually http://127.0.0.1:7860).
"""
from pathlib import Path

import gradio as gr
import numpy as np
import pandas as pd
import scipy.stats as stats
import seaborn as sns
from matplotlib.figure import Figure

DEFAULT_CSV = Path(__file__).parent / "sales_data.csv"
NO_GROUP = "(none)"

sns.set_theme(style="whitegrid")


# ---------------------------------------------------------------- Step 1 and 2: the data
def make_sample_data(seed=None):
    """The random sales data of the notebook: 20 products, units sold from a Poisson distribution."""
    rng = np.random.default_rng(seed)
    return pd.DataFrame({
        "product_id": range(1, 21),
        "product_name": [f"Product {i}" for i in range(1, 21)],
        "category": rng.choice(["Electronics", "Clothing", "Home", "Books"], size=20),
        "units_sold": rng.poisson(lam=50, size=20),
        "sale_data": pd.date_range(start="2023-01-01", periods=20, freq="D"),
    })


def load_data(file_path, use_sample, seed):
    """Uploaded CSV, or new random sample data, or the sales_data.csv next to this file."""
    if use_sample:
        return make_sample_data(None if seed in (None, "", 0) else int(seed))
    if file_path:
        return pd.read_csv(file_path)
    if DEFAULT_CSV.exists():
        return pd.read_csv(DEFAULT_CSV)
    return make_sample_data(42)


def column_choices(df):
    numeric = df.select_dtypes(include="number").columns.tolist()
    groups = [NO_GROUP] + [c for c in df.columns if not pd.api.types.is_float_dtype(df[c]) and df[c].nunique() <= 20]
    return numeric, groups


def refresh_columns(file_path, use_sample, seed):
    """When the data changes, update the two column drop-downs."""
    df = load_data(file_path, use_sample, seed)
    numeric, groups = column_choices(df)
    value = "units_sold" if "units_sold" in numeric else (numeric[0] if numeric else None)
    group = "category" if "category" in groups else NO_GROUP
    return gr.Dropdown(choices=numeric, value=value), gr.Dropdown(choices=groups, value=group)


# ---------------------------------------------------------------- Step 3: descriptive statistics
def descriptive_markdown(x):
    modes = x.mode().tolist()
    mode_text = ", ".join(f"{m:g}" for m in modes[:5]) + (" ..." if len(modes) > 5 else "")
    d = x.describe()
    rows = [
        ("Count", f"{d['count']:.0f}"), ("Mean", f"{x.mean():.4f}"), ("Median", f"{x.median():.4f}"), ("Mode", mode_text),
        ("Variance", f"{x.var():.4f}"), ("Standard deviation", f"{x.std():.4f}"),
        ("Minimum", f"{d['min']:g}"), ("25%", f"{d['25%']:g}"), ("75%", f"{d['75%']:g}"), ("Maximum", f"{d['max']:g}"),
        ("Skewness", f"{x.skew():.4f}"), ("Kurtosis", f"{x.kurt():.4f}"),
    ]
    lines = ["| Statistic | Value |", "| --- | --- |"] + [f"| {k} | {v} |" for k, v in rows]
    return "\n".join(lines)


def category_table(df, value_col, group_col):
    if group_col == NO_GROUP or group_col not in df.columns:
        return pd.DataFrame()
    out = df.groupby(group_col)[value_col].agg(["sum", "mean", "std"]).reset_index()
    out.columns = ["Category", "Total units Sold", "Average units Sold", "std Dev of units Sold"]
    return out.round(3)


# ---------------------------------------------------------------- Step 4: inferential statistics
def confidence_markdown(x, conf):
    n = len(x)
    df_ = n - 1
    se = x.std() / np.sqrt(n)
    t_score = stats.t.ppf((1 + conf) / 2, df_)
    margin = t_score * se
    low, high = x.mean() - margin, x.mean() + margin
    return (
        f"### {conf:.0%} confidence interval for the mean\n\n"
        f"| Part | Value |\n| --- | --- |\n"
        f"| Sample mean | {x.mean():.4f} |\n"
        f"| Sample standard deviation | {x.std():.4f} |\n"
        f"| Sample size n | {n} |\n"
        f"| Degrees of freedom (n - 1) | {df_} |\n"
        f"| Standard error (s / sqrt(n)) | {se:.4f} |\n"
        f"| t-score | {t_score:.4f} |\n"
        f"| Margin of error | {margin:.4f} |\n\n"
        f"**Confidence interval: ({low:.4f}, {high:.4f})**\n\n"
        f"We are {conf:.0%} confident that the true mean is between {low:.2f} and {high:.2f}."
    )


def test_markdown(x, mu0, alpha, value_col):
    t_stat, p_value = stats.ttest_1samp(x, mu0)
    if p_value < alpha:
        decision = f"**Reject the null hypothesis:** the mean of '{value_col}' is significantly different from {mu0:g}."
    else:
        decision = f"**Fail to reject the null hypothesis:** the mean of '{value_col}' is not significantly different from {mu0:g}."
    return (
        f"### Hypothesis test (one-sample t-test)\n\n"
        f"- Null hypothesis H0: the mean of '{value_col}' is equal to {mu0:g}\n"
        f"- Alternative hypothesis H1: the mean of '{value_col}' is not equal to {mu0:g}\n\n"
        f"| Part | Value |\n| --- | --- |\n"
        f"| t-statistic | {t_stat:.4f} |\n"
        f"| p-value | {p_value:.6g} |\n"
        f"| Significance level alpha | {alpha:g} |\n\n"
        f"{decision}\n\n"
        f"(p-value {'<' if p_value < alpha else '>='} alpha)"
    )


# ---------------------------------------------------------------- charts
def histogram_figure(x, value_col):
    fig = Figure(figsize=(8, 4.5))
    ax = fig.subplots()
    sns.histplot(x, bins=10, kde=True, ax=ax)
    ax.axvline(x.mean(), color="red", linestyle="--", label="Mean")
    ax.axvline(x.median(), color="blue", linestyle="--", label="Median")
    ax.axvline(x.mode()[0], color="green", linestyle="--", label="Mode")
    ax.set_title(f"Distribution of {value_col}")
    ax.set_xlabel(value_col)
    ax.set_ylabel("Frequency")
    ax.legend()
    fig.tight_layout()
    return fig


def boxplot_figure(df, value_col, group_col):
    fig = Figure(figsize=(8, 4.5))
    ax = fig.subplots()
    sns.boxplot(x=group_col, y=value_col, data=df, ax=ax)
    ax.set_title(f"Box Plot of {value_col} by {group_col}")
    fig.tight_layout()
    return fig


def barplot_figure(table, value_col):
    fig = Figure(figsize=(8, 4.5))
    ax = fig.subplots()
    sns.barplot(x="Category", y="Total units Sold", data=table, ax=ax)
    ax.set_title(f"Total {value_col} by Category")
    ax.set_xlabel("Category")
    ax.set_ylabel(f"Total {value_col}")
    fig.tight_layout()
    return fig


# ---------------------------------------------------------------- the whole analysis
def analyze(file_path, use_sample, seed, value_col, group_col, conf, mu0, alpha):
    df = load_data(file_path, use_sample, seed)

    if value_col not in df.columns or not pd.api.types.is_numeric_dtype(df[value_col]):
        raise gr.Error("Choose a numeric column to analyse.")
    x = df[value_col].dropna()
    if len(x) < 2:
        raise gr.Error("The column needs at least 2 values.")
    mu0 = 0.0 if mu0 is None else float(mu0)

    table = category_table(df, value_col, group_col)
    has_groups = not table.empty
    gr.Info("Analysis done.")

    return (
        df.head(100),
        descriptive_markdown(x),
        table,
        confidence_markdown(x, conf),
        test_markdown(x, mu0, alpha, value_col),
        histogram_figure(x, value_col),
        boxplot_figure(df, value_col, group_col) if has_groups else None,
        barplot_figure(table, value_col) if has_groups else None,
    )


# ---------------------------------------------------------------- the Gradio page
_first = load_data(None, False, None)
_numeric, _groups = column_choices(_first)

with gr.Blocks(title="Statistics app") as demo:
    gr.Markdown(
        "# 📊 Statistics app\n"
        "Descriptive statistics, a confidence interval, a t-test and charts, like the notebook `code.ipynb`. "
        "Upload a CSV file, or use the default `sales_data.csv`."
    )
    with gr.Row():
        with gr.Column(scale=1):
            file_in = gr.File(label="Upload a CSV file (optional)", file_types=[".csv"], type="filepath")
            sample_in = gr.Checkbox(label="Use new random sample data (like the notebook)", value=False)
            seed_in = gr.Number(label="Random seed for the sample data (0 = a new random sample each time)", value=0, precision=0)
            value_in = gr.Dropdown(label="Numeric column to analyse", choices=_numeric, value="units_sold" if "units_sold" in _numeric else _numeric[0])
            group_in = gr.Dropdown(label="Group by (optional)", choices=_groups, value="category" if "category" in _groups else NO_GROUP)
            conf_in = gr.Slider(0.80, 0.99, value=0.95, step=0.01, label="Confidence level")
            mu0_in = gr.Number(label="Null hypothesis: the mean is equal to (mu0)", value=20)
            alpha_in = gr.Slider(0.01, 0.10, value=0.05, step=0.01, label="Significance level (alpha)")
            run_btn = gr.Button("Run analysis", variant="primary")
        with gr.Column(scale=2):
            with gr.Tab("Data"):
                data_out = gr.Dataframe(label="First 100 rows", interactive=False)
            with gr.Tab("Descriptive statistics"):
                desc_out = gr.Markdown()
                cat_out = gr.Dataframe(label="Total, average and standard deviation by category", interactive=False)
            with gr.Tab("Confidence interval"):
                ci_out = gr.Markdown()
            with gr.Tab("Hypothesis test"):
                test_out = gr.Markdown()
            with gr.Tab("Charts"):
                plot1 = gr.Plot(label="Distribution")
                plot2 = gr.Plot(label="Box plot by category")
                plot3 = gr.Plot(label="Total by category")

    inputs = [file_in, sample_in, seed_in, value_in, group_in, conf_in, mu0_in, alpha_in]
    outputs = [data_out, desc_out, cat_out, ci_out, test_out, plot1, plot2, plot3]

    # new data -> refresh the two drop-downs
    for trigger in (file_in.change, sample_in.change):
        trigger(refresh_columns, [file_in, sample_in, seed_in], [value_in, group_in])

    run_btn.click(analyze, inputs, outputs)
    demo.load(analyze, inputs, outputs)       # show the results when the page opens

if __name__ == "__main__":
    demo.launch()
