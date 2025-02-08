import streamlit as st
import pandas as pd
import numpy as np

## Title of the application
st.title("Hello Streamlit")

## Displaying some simple text
st.write("hey...! This is a simple text")

## Creating simple dataframe
df = pd.DataFrame({
    'first column':[1,2,3,4],
    'second column': [10,20,30,40]
})


## Displaying the Dataframe
st.write("Here is the Dataframe")
st.write(df)

## Create a line chart
chart_data = pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)