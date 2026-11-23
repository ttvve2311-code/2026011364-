print('hello')

python -m pip install streamlit

import streamlit as st
import datetime

name = st.text_input("이름을 입력하세요")
age = st.number_input("나이를 입력하세요", min_value=0, max_value=120)
birthdate = st.date_input("생년월일 선택")
hobby = st.selectbox("취미 선택", ["독서", "운동", "게임", "음악"])
agree = st.checkbox("이용 약관에 동의합니다")
file = st.file_uploader("파일 업로드")

if st.button("제출"):
st.success(f"{name}님({age}세), 제출 완료!")