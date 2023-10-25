import streamlit as st
import numpy as np
import pandas as pd

st.title("Streamlit 超入門")

st.write("DataFrame")

df = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [35.69,139.70],     #NumPyのnp.random.rand()関数を使用して生成されます。この関数は0から1の範囲の一様分布からランダムな数値を生成するもの
    columns=["lat","lon"]
)

st.map(df) #mapを表示