import streamlit as st
import pandas as pd
import numpy as np

# st.title("My 1st Streamlit App Created by Murali")

# st.write("Welcome ! This app calculates the square of a number.")
# # Create an interactive slider for input
# st.header("Select a Number")
# # number = st.slider("Pick a number", min=0, max=100, default=25)
# number = st.slider("Pick a number", 0,100,25)

# # Calculate the square of the selected number
# st.subheader("Result")
# square = number * number
# st.write(f"The square of **{number}** is **{square}**")


st.title("My 1st Streamlit App Created by Murali")
st.write("This is a simple apps to demontrate  the basic functionality of Streamlit.")
st.sidebar.header("User Input Features")
# Text input
user_name = st.sidebar.text_input("What is your name?", "Murali")
# Slider
age = st.sidebar.slider("Selectyour age?", 0, 100, 25)
# Selectbox
favorite_color = st.sidebar.selectbox("Select your favorite color", ["Red", "Green", "Blue", "Yellow"])
# ---- Main page Content -------
st.header(f"Hello, {user_name}!")
st.write(f"Your age is **{age}** and your favorite color is **{favorite_color}**.")
st.subheader("Here is Sample DataFrame")
# Create a sample DataFrame
data = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('col %d' % i for i in range(5))
)

st.dataframe(data)
## ---- Checkbox to show/hide the content -------
if st.checkbox("Show raw data"):
    st.subheader("Raw Data")
    st.write(data)

## --- Button to trigger an action -------
if st.button("Say Hello"):
    st.write(f"Hello there")
else:
    st.write(f"Goodbye")
