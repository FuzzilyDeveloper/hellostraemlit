
# app.py
import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# Set page configuration
st.set_page_config(page_title="Iris Flower Prediction", page_icon="🌺")

# Title and description
st.title("🌺 Iris Flower Species Prediction")
st.write("""
    This app predicts the Iris flower species based on sepal and petal measurements.
    Enter the measurements below and click 'Predict' to see the result!
""")

# Load and prepare the Iris dataset
@st.cache_data
def load_data():
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    return df, iris.feature_names, iris.target_names

df, feature_names, target_names = load_data()

# Train the model
@st.cache_resource
def train_model():
    X = df[feature_names]
    y = df['species']
    X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

model = train_model()

# Create input fields
st.subheader("Enter Iris Measurements")
col1, col2 = st.columns(2)

with col1:
    sepal_length = st.slider("Sepal Length (cm)", 
                            min_value=0.0, 
                            max_value=10.0, 
                            value=5.0, 
                            step=0.1)
    sepal_width = st.slider("Sepal Width (cm)", 
                           min_value=0.0, 
                           max_value=10.0, 
                           value=3.0, 
                           step=0.1)

with col2:
    petal_length = st.slider("Petal Length (cm)", 
                            min_value=0.0, 
                            max_value=10.0, 
                            value=1.5, 
                            step=0.1)
    petal_width = st.slider("Petal Width (cm)", 
                           min_value=0.0, 
                           max_value=10.0, 
                           value=0.2, 
                           step=0.1)

# Prediction button
if st.button("Predict"):
    # Prepare input data
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    
    # Make prediction
    prediction = model.predict(input_data)
    predicted_species = target_names[prediction][0]
    
    # Display result
    st.subheader("Prediction Result")
    st.success(f"The predicted Iris species is: **{predicted_species}**")
    
    # Display input values
    st.write("Input Measurements:")
    st.write(f"- Sepal Length: {sepal_length} cm")
    st.write(f"- Sepal Width: {sepal_width} cm")
    st.write(f"- Petal Length: {petal_length} cm")
    st.write(f"- Petal Width: {petal_width} cm")

# Add some information about the model
st.sidebar.header("About the Model")
st.sidebar.write("""
    This application uses a Random Forest Classifier trained on the Iris dataset.
    The dataset contains 150 samples of three Iris species:
    - Iris Setosa
    - Iris Versicolor
    - Iris Virginica
    
    Features used for prediction:
    - Sepal Length
    - Sepal Width
    - Petal Length
    - Petal Width
""")
