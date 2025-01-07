import streamlit as st

# 제목
st.title("Simple Calculator")

# 사용자 입력
number1 = st.number_input("Enter first number", value=0)
operation = st.selectbox("Choose an operation", ["+", "-", "*", "/"])
number2 = st.number_input("Enter second number", value=0)

# 계산 및 결과 출력
if st.button("Calculate"):
    try:
        if operation == "+":
            result = number1 + number2
        elif operation == "-":
            result = number1 - number2
        elif operation == "*":
            result = number1 * number2
        elif operation == "/":
            result = number1 / number2
        st.write(f"Result: {result}")
    except Exception as e:
        st.error("An error occurred!")
