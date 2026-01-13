import streamlit as st
st.title("make a simple calculator")



num1 = st.number_input("Enter first number")
num2 = st.number_input("Enter second number")
operation = st.selectbox("Select operation", ["Add", "Subtract", "Multiply", "Divide", "Modulus", "Exponent", "Floor Division", "Average", "Maximum", "Minimum"])

if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":    
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"
    elif operation == "Modulus": 
        result = num1 % num2
    elif operation == "Exponent":
        result = num1 ** num2
    elif operation == "Floor Division":
        if num2 != 0:
            result = num1 // num2
        else:
            result = "Error: Division by zero"
    elif operation == "Average":
        result = (num1 + num2) / 2
    elif operation == "Maximum":
        result = max(num1, num2)
    elif operation == "Minimum":
        result = min(num1, num2)
        
    st.write("The result of {operation} is : ", result)