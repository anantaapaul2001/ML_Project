import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px

st.title('**WELCOME TO MY APP**')
st.markdown(' **First** **Tutorial** 1')
st.text(' This is a website to let you know about Python Streamlit')
st.header('ABOUT PYTHON')
st.subheader("You are welcome in this website")

st.text(' lets talk about the python streamlit app')
df = sns.load_dataset('tips')
st.dataframe(df.head(10),use_container_width=False, height=400,width=400)

st.bar_chart(df, x='day', y='tip',height=500, color = '#ffaa0088')

fig = px.scatter(df, x='tip', y='total_bill', template ='seaborn')
st.plotly_chart(fig)
import matplotlib.pyplot as plt

figg= plt.figure(figsize=(10,6))
sns.scatterplot(df, x= 'tip', y='total_bill')
st.pyplot(figg)

