import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image      #画像を扱う

st.title("Streamlit 超入門")

st.write("Interactive Widgets")

left_column, right_column = st.columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
    right_column.button("ここは右カラム")

# #sidebarの追加
# text = st.text_input("あなたの趣味を教えてください。")
# condistion = st.slider("あなたの今の調子は？", 0, 100, 50) 

# "あなたの趣味: ", text
# "コンディション: ", condistion