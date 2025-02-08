import streamlit as st
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

st.cache_data # This decorator is used to load the daraset in the cache so that the dataset isn't loaded always from the library
def load_data():
    iris = load_iris()
    df = pd.DataFrame(iris.data,columns=iris.feature_names)
    df['species'] = iris.target
    return df,iris.target_names

df,target_names = load_data()

model = RandomForestClassifier()
model.fit(df.iloc[:,:-1],df['species'])  # first feature is dataset independent and exclusing last feature i.e dependent and the second feature is the target

st.sidebar.title("Input feature")
sepal_length = st.sidebar.slider("Sepal length",float(df['sepal length (cm)'].min()),float(df['sepal length (cm)'].max()))
sepal_width = st.sidebar.slider("Sepal length",float(df['sepal width (cm)'].min()),float(df['sepal width (cm)'].max()))
petal_length = st.sidebar.slider("Petal length",float(df['petal length (cm)'].min()),float(df['petal length (cm)'].max()))
petal_width = st.sidebar.slider("Petal width",float(df['petal width (cm)'].min()),float(df['petal width (cm)'].max()))

input_data = [[sepal_length,sepal_width,petal_length,petal_width]]

## prediction 
prediction = model.predict(input_data)
predict_species = target_names[prediction[0]]

st.write("Prediction")
st.write(f"The prediction species is: {predict_species}")








