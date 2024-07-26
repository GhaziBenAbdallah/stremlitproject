import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Iris dataset
@st.cache
def load_data():
    iris = sns.load_dataset('iris')
    return iris

data = load_data()

# Title of the app
st.title('Iris Dataset Visualization')

# Sidebar for user input
st.sidebar.header('Filter by Species')
species = st.sidebar.multiselect('Select Species', options=data['species'].unique(), default=data['species'].unique())

# Filter data based on user input
filtered_data = data[data['species'].isin(species)]

# Show dataframe
st.write('## Filtered Data')
st.write(filtered_data)

# Create scatter plot
st.write('## Scatter Plot')
fig, ax = plt.subplots()
sns.scatterplot(x='sepal_length', y='sepal_width', hue='species', data=filtered_data, ax=ax)
ax.set_title('Sepal Length vs Sepal Width')
st.pyplot(fig)
