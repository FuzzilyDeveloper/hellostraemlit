import streamlit as st
import pandas as pd
import joblib
import keras

# Load the model
model = joblib.load('bag_price_predictor.pkl')

# Streamlit app
st.title('Bag Price Predictor')

# Input form
st.header('Enter Bag Details')

brand = st.selectbox('Brand', ['Jansport', 'Under Armour', 'Nike', 'Adidas'])
material = st.selectbox('Material', ['Leather', 'Canvas', 'Nylon'])
size = st.selectbox('Size', ['Small', 'Medium'])
compartments = st.number_input('Number of Compartments', min_value=1.0, max_value=10.0, step=0.1)
laptop_compartment = st.selectbox('Laptop Compartment', ['Yes', 'No'])
waterproof = st.selectbox('Waterproof', ['Yes', 'No'])
style = st.selectbox('Style', ['Tote', 'Messenger'])
color = st.selectbox('Color', ['Black', 'Green', 'Red'])
weight_capacity = st.number_input('Weight Capacity (kg)', min_value=0.0, step=0.1)

# Create input DataFrame
input_data = pd.DataFrame({
    'Brand': [brand],
    'Material': [material],
    'Size': [size],
    'Compartments': [compartments],
    'Laptop Compartment': [laptop_compartment],
    'Waterproof': [waterproof],
    'Style': [style],
    'Color': [color],
    'Weight Capacity (kg)': [weight_capacity]
})

# Predict
if st.button('Predict Price'):
    prediction = model.predict(input_data)[0]
    st.success(f'Predicted Price: ${prediction:.2f}')
