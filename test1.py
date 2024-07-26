import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from PIL import Image
import os


import sklearn
print(sklearn.__version__)

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["target"] = iris.target

x = df.drop(columns=["target"])
y = df["target"]

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, random_state=40)

log = LogisticRegression()
log.fit(x_train, y_train)

st.title("Flowers Identification")

img1, img2, img3 = st.columns(3)
with img1:
    img1_placeholder = st.empty()
    img1_placeholder.image("versicolor.jpg", caption="Versicolor", use_column_width=True)
with img2:
    img2_placeholder = st.empty()
    img2_placeholder.image("virginica.jpg", caption="Virginica", use_column_width=True)
with img3:
    img3_placeholder = st.empty()
    img3_placeholder.image("setosa.jpg", caption="Setosa", use_column_width=True)

# st.write("Commencez à saisir les caractéristiques dans le volet latéral pour prédire le type de fleur.")

result_container = st.empty()

st.sidebar.header("Flower characteristics")
sepal_length = st.sidebar.number_input("Sepal length", value=0.0)
sepal_width = st.sidebar.number_input("Sepal width", value=0.0)
petal_length = st.sidebar.number_input("Petal length", value=0.0)
petal_width = st.sidebar.number_input("Petal width", value=0.0)

if st.sidebar.button("Guess the Flower!!"):
    # Supprimer les images des fleurs de l'accueil
    img1_placeholder.empty()
    img2_placeholder.empty()
    img3_placeholder.empty()

    prediction = log.predict([[sepal_length, sepal_width, petal_length, petal_width]])
    st.markdown(
        f"<p style='font-size:20px;font-weight:bold;'>Flower is : {['Versicolor', 'Virginica', 'Setosa'][prediction[0]]}</p>",
        unsafe_allow_html=True)

    image_paths = ["versicolor.jpg", "virginica.jpg", "setosa.jpg"]
    if 0 <= prediction < len(image_paths):
        image_path = image_paths[prediction[0]]
        if os.path.exists(image_path):
            image = Image.open(image_path)
            # Redimensionner l'image prédite
            image.thumbnail((150, 150))
            result_container.image(image, caption='Our Flower', use_column_width=True)
        else:
            st.error(f"L'image {image_path} n'existe pas.")
    else:
        st.error("Indice de prédiction incorrect.")