import pandas as pd
import streamlit as st
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.write("""

# Simple Iris Flower Prediction App
         
This app predicts the Iris flower type!

""")

# Side bar.
st.sidebar.header("User Input Parameters")


def user_input_features():
    """Dynamicly update the variables and generate the corresponding dataframe.

    Returns:
        _type_: The dataframe.
    """

    # parameters: label, min, max, starting default value.
    sepal_length = st.sidebar.slider("Sepal Length", 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider("Sepal Width", 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider("Petal Length", 0.1, 6.9, 1.3)
    petal_width = st.sidebar.slider("Petal Width", 0.1, 2.5, 0.2)
    data = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width,
    }
    features = pd.DataFrame(data, index=[0])
    return features


# Generate the dataframe from the user input.
df = user_input_features()

st.subheader("User Input parameters")
st.write(df)  # Write the df as a table.


# Load the iris dataset and make the prediction.
iris = datasets.load_iris()
X = iris.data
Y = iris.target

clf = RandomForestClassifier()
clf.fit(X, Y)

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)
prediction_proba = pd.DataFrame(prediction_proba)

prediction_proba.rename(
    columns={0: "Setosa", 1: "versicolor", 2: "virginica"}, inplace=True
)

st.subheader("Prediction")
st.write(iris.target_names[prediction])

st.subheader("Prediction Probability")
st.write(prediction_proba)
