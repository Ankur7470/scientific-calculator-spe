import streamlit as st
from calculator_functions import square_root, factorial, natural_log, power

st.title("Scientific Calculator")

operation = st.selectbox("Choose an operation", ["Square Root (√x)", "Factorial (x!)", "Natural Log (ln x)", "Power (x^b)"])

if operation == "Square Root (√x)":
    x = st.number_input("Enter a number (x):", min_value=0.0, format="%.2f")
    if st.button("Calculate"):
        st.write(f"√{x} = {square_root(x)}")

elif operation == "Factorial (x!)":
    x = st.number_input("Enter an integer (x):", min_value=0, step=1, format="%d")
    if st.button("Calculate"):
        st.write(f"{x}! = {factorial(x)}")

elif operation == "Natural Log (ln x)":
    x = st.number_input("Enter a positive number (x):", min_value=0.01, format="%.2f")
    if st.button("Calculate"):
        st.write(f"ln({x}) = {natural_log(x)}")

elif operation == "Power (x^b)":
    x = st.number_input("Enter base (x):", format="%.2f")
    b = st.number_input("Enter exponent (b):", format="%.2f")
    if st.button("Calculate"):
        st.write(f"{x}^{b} = {power(x, b)}")

#sample comment
