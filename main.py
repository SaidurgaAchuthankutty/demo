import streamlit as st
import pandas as pd
st.title('My First Project')
data={
    'volume': [3,3,5,6],
    'mass':[6,4,8,9],
    'velocity':[9,5,6,7],
}
df=pd.DataFrame(data)
st.table(df)
