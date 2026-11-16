# Streamlit

## for ... else (a reminder)

- `for ... else` is a concept applicable only in the Python programming language. Most other languages do not have it.
- See the "for ... else" section in `advanced-python-concepts.md`.

## Intro to Streamlit

- Streamlit is a Python library to build a web app (a dashboard or a data app) with only Python code. You don't need HTML, CSS or JavaScript.
- Install: `pip install streamlit`
- Import: `import streamlit as st`

## Streamlit functions

### Text on the page

| Function | What it does |
| -------- | ------------ |
| `st.title()` | Shows the main title of the page |
| `st.header()` | Shows a header (smaller than the title) |
| `st.subheader()` | Shows a subheader (smaller than the header) |
| `st.write()` | Shows anything: text, numbers, a DataFrame, a chart |

### Sidebar (the panel on the left)

| Function | What it does |
| -------- | ------------ |
| `st.sidebar` | The left panel. Put a widget in it by writing `st.sidebar.` before the function |
| `st.sidebar.header()` | A header inside the sidebar |
| `st.sidebar.text_input()` | A box to type text |
| `st.sidebar.slider()` | A slider to select a number |
| `st.sidebar.selectbox()` | A drop-down list to select one option |

### Main page widgets

| Function | What it does |
| -------- | ------------ |
| `st.dataframe()` | Shows a DataFrame as an interactive table (sort and scroll) |
| `st.checkbox()` | A tick box. Returns `True` when ticked |
| `st.button()` | A button. Returns `True` in the run after it is clicked |

## Example app

Save this as `app.py` in the same folder as `countries_dummy.xlsx`:

```python
import streamlit as st
import pandas as pd

st.title("Country Data App")
st.header("This is a header")
st.subheader("This is a subheader")
st.write("Hello, this is st.write")

st.sidebar.header("Filters")
name = st.sidebar.text_input("Your name", "Guest")
value = st.sidebar.slider("Select a value", 0, 100, 25)
group = st.sidebar.selectbox(
    "Income group",
    ["High income", "Upper middle income", "Lower middle income", "Low income"],
)

df = pd.read_excel("countries_dummy.xlsx")

if st.checkbox("Show data"):
    st.dataframe(df[df["IncomeGroup"] == group])

if st.button("Say hello"):
    st.write(f"Hello {name}!")
```

- `text_input("Your name", "Guest")` -- the first value is the label, the second is the default text.
- `slider("Select a value", 0, 100, 25)` -- label, minimum, maximum, starting value.
- `selectbox("Income group", [...])` -- label and the list of options. It returns the option the user selected.
- `checkbox` and `button` are used with `if`, because they return `True` or `False`.

## How to run the app

Streamlit apps are not run with `python app.py`. Use the `streamlit run` command.

### 1. From cmd

```bash
cd C:\path\to\the\folder
streamlit run app.py
```

### 2. From VS Code

1. Open the folder in VS Code.
2. Open the terminal (`` Ctrl+` ``).
3. Run the same command:

```bash
streamlit run app.py
```

- The app opens in the browser, usually at `http://localhost:8501`.
- If `streamlit` is not found, use `python -m streamlit run app.py`.
- Press `Ctrl+C` in the terminal to stop the app.

## How it works

- Streamlit runs the whole script from top to bottom **every time** the user changes a widget (moves the slider, clicks the button, ticks the checkbox).
- The value returned by each widget is the user's current choice, so the app updates itself.
- When you save the file, the browser shows a "Rerun" option to see the change.
