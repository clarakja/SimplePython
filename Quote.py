import streamlit as st
import random

# 명언 리스트
quotes = [
    "The only limit to our realization of tomorrow is our doubts of today.",
    "Do what you can, with what you have, where you are.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "상황을 가장 잘 활용하는 사람이 가장 좋은 상황을 맞는다.",
    "The best time to plant a tree was 20 years ago. The second best time is now.",
    "It does not matter how slowly you go as long as you do not stop.",
    "큰 목표를 이루고 싶으면 허락을 구하지 마라. "
]

# 제목
st.title("Random Quote Generator")

# 버튼 클릭 시 랜덤 명언 출력
if st.button("Generate a Quote"):
    st.write(random.choice(quotes))
