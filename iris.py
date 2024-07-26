import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris

# Load Iris dataset
iris = load_iris()
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_df['species'] = iris.target
iris_df['species'] = iris_df['species'].map({i: name for i, name in enumerate(iris.target_names)})

st.title('Iris Dataset Visualization')

# Line Chart
st.subheader('Line Chart of Sepal and Petal Length')
line_chart_df = iris_df[['sepal length (cm)', 'petal length (cm)']]
st.line_chart(line_chart_df)

# Bar Chart
st.subheader('Bar Chart of Sepal Length by Species')
species_group = iris_df.groupby('species')['sepal length (cm)'].mean()
st.bar_chart(species_group)
