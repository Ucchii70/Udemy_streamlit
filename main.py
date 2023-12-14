import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image      #画像を扱う

st.title("Streamlit 超入門")

st.write("Display Image")

#チェックが入っていたらTrue(画像を表示)
if st.checkbox("show Image"):
    img = Image.open("IMGP3446.jpg")
    st.image(img, caption="Huyen", use_column_width=True)     #use_column_width=Trueでアプリ、画像の幅に自動で合わせる
