# Import all packages needed
import pandas as pd
import streamlit as st
import plotly.express as px
from matplotlib import pyplot as plt 

# Read CSV file into the DataFrame
df = pd.read_csv('vehicles_us.csv')

# Edit ~ Scatterplot - Header . . .

# Let's start with making a Header
st.header('Data View')

st.dataframe(df)

# Let's make a Scatterplot
st.subheader('Scatterplot')
x_sp = 'model_year'
y_sp = 'odometer'
fig_scatter = px.scatter(df, x=x_sp, y=y_sp)
fig_scatter.update_layout(
    title='Model year VS Odometer'
)
st.plotly_chart(fig_scatter)

# Read CSV file into the DataFrame
df = pd.read_csv('vehicles_us.csv')

# Edit ~ Histogram - Filter . . .

# Let's make a Histogram with Filter
st.header('Histogram')

filter_above_75k = st.checkbox('Filter Out Price Above 75k')

filtered_df = df.copy()
if filter_above_75k:
    filtered_df = filtered_df[filtered_df['price'] <= 75000]

fig_hist = px.histogram(filtered_df, x='price', nbins=75, opacity=0.7, title='Histogram of Price')

st.plotly_chart(fig_hist)