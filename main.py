import streamlit as st
import time

st.title("Streamlit 超入門")

st.write("プログレスバーの表示")
"Start!!"

latest_iteration = st.empty()                     #空の要素を作成
bar = st.progress(0)                              #

for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")     #進捗状況のテキストを表示
    bar.progress(i + 1)                           #バーを進める
    time.sleep(0.1)                               #0,1秒ごとに動かす

"Done!!"

bar.empty()                                       #カウントが終わったらバーを消す

left_column, right_column = st.columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
    right_column.button("ここは右カラム")

expander1 = st.expander("問い合わせ1")
expander1.write("問い合わせ1の回答")


expander2 = st.expander("問い合わせ2")
expander2.write("問い合わせ2の回答")
