import streamlit as st
import numpy as np
import pandas as pd

st.title("Streamlit 超入門")

st.write("DataFrame")

df = pd.DataFrame({
    "1列目":[1,2,3,4],
    "2列目":[10,20,30,40]
})
#st.write(df)
#st.dataframe(df.style.highlight_max(axis=0),width=400,height=400) #dataframeの方が使い勝手がいい、動的な表
st.table(df.style.highlight_max(axis=0)) #静的な表でサイズ指定ができない？

"""

# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```

"""

