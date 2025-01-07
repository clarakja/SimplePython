import streamlit as st
import random

# 퀴즈 데이터
quiz_data = {
    "What is the capital of France?": "Paris",
    "What is 5 + 7?": "12",
    "Who wrote 'To Kill a Mockingbird'?": "Harper Lee",
    "What is the largest planet in our Solar System?": "Jupiter",
    "What is the chemical symbol for water?": "H2O"
}

# 랜덤 퀴즈 선택
question, answer = random.choice(list(quiz_data.items()))

# 제목
st.title("Simple Quiz App")

# 퀴즈 출력
st.write(question)
user_answer = st.text_input("Your answer:")

# 정답 확인
if st.button("Submit"):
    if user_answer.strip().lower() == answer.lower():
        st.success("Correct!")
    else:
        st.error(f"Wrong! The correct answer is {answer}.")
