import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title("Streamlit 超入門")

st.write("Display Image")

img = Image.open("IMGP3446.jpg")
st.image(img, caption="Huyen", use_column_width=True)