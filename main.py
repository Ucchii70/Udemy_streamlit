import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image      #画像を扱う

st.title("Streamlit 超入門")

st.write("Interactive Widgets")

text = st.text_input("あなたの趣味を教えてください。")
"あなたの趣味: ", text

condistion = st.slider("あなたの今の調子は？", 0, 100, 50)
"コンディション: ", condistion