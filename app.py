import streamlit as st
import pandas as pd
import numpy as np

##title  of application
st.title("Hello Streamlit")

#Display a simple text
st.write("This is  a simple text ")
#create a simple dataframe
df= pd.DataFrame({
    'first Col':[1,2,3,4,5],
    'second Col':[10,20,30,40,50]
})
##Display the Dataframe
st.write("Here is a dataframe")
st.write(df)

##Create a line chart
chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)