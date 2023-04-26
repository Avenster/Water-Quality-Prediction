import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the saved model
with open('rf.pkl', 'rb') as file:
    rf = pickle.load(file)

# Define a function to predict AQI
def predict_aqi(al, ar, ba, cd, cl, cr,
       vi, ni, pe, ag):
    input_data = np.array([[al, ar, ba, cd, cl, cr,
       vi, ni, pe, ag]])
    water_pred = rf.predict(input_data)[0]
    if water_pred == 1:
        label = "Good water"
    else:
        label = "Bad water"

    return water_pred, label
  
    
   
# Create a web app using Streamlit
def main():
    st.markdown(
    """
    <div style='text-align: left;'>
        <h1 style='font-size: 36px; color:magenta ;font-weight: bold; font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;'>Water Quality Prediction App</h1>
    </div>
    """,
    unsafe_allow_html=True)
    
    st.markdown(
    """
    <div style='text-align: left;'>
        <h1 style='font-size: 15px;color:pink ;font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;'>This app predicts the water quality based on various input features.</h1>
    </div>
    """,
    unsafe_allow_html=True
    )

    # Add input features
    al = st.slider("Aluminium", min_value=0.0, max_value=10.000, value=1.65)
    ar= st.slider("Arsenic", min_value=0.0, max_value=2.0000, value=0.04)
    ba = st.slider("Barium", min_value=0.0, max_value=5.0000, value=2.85)
    cd = st.slider("Cadmium", min_value=0.0, max_value=0.5000, value=0.007)
    cl= st.slider("Chloramine", min_value=0.0, max_value=10.000, value=0.35)
    cr = st.slider("Chromium", min_value=0.0, max_value=1.0000, value=0.83)
    vi = st.slider("Viruses", min_value=0.00, max_value=1.000, value=0.1)
    ni= st.slider("Nitrates", min_value=0.0, max_value=20.000, value=16.08)
    pe = st.slider("Perchlorate", min_value=0.0, max_value=70.000, value=37.75)
    ag = st.slider("Silver", min_value=0.0, max_value=1.000, value=0.34)
   

    # Predict the water Quality
    if st.button("PREDICT"):
        water_pred, label = predict_aqi(al, ar, ba, cd, cl, cr,vi, ni, pe, ag)
        st.success(f"The predicted Water is {round(water_pred)}. The Water quality is {label}.")

    
    
if __name__ == '__main__':
    main()
