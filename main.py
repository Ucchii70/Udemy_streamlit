import streamlit as st
import numpy as np
import pandas as pd

st.title("Streamlit 超入門")

st.write("DataFrame")

df = pd.DataFrame(
    np.random.rand(20,3),
    columns=["a","b","c"]
)

#st.table(df.style.highlight_max(axis=0))  ハイライトをつける
#st.line_chart(df)    ラインチャート
#st.area_chart(df)    エリアチャート
#st.bar_chart(df)　　　棒グラフ
