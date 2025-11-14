import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('final_model_v2.joblib')

# Set the page title and header
st.set_page_config(page_title="California Housing Price Predictor", layout="wide")
st.title('🏡 California Housing Price Predictor')
st.write('This app predicts the median house value in a California district.')
st.write('---')

# Create two columns for layout
col1, col2 = st.columns(2)

# Column 1: Sliders for user input
with col1:
    st.header('Input Features')
    
    # 8 sliders for the 8 features
    med_inc = st.slider('Median Income ($10,000s)', min_value=0.0, max_value=16.0, value=3.5, step=0.1)
    house_age = st.slider('House Age (years)', min_value=1, max_value=55, value=25, step=1)
    ave_rooms = st.slider('Average Rooms', min_value=1.0, max_value=15.0, value=5.0, step=0.1)
    ave_bedrms = st.slider('Average Bedrooms', min_value=1.0, max_value=10.0, value=1.0, step=0.1)
    population = st.slider('Population', min_value=1, max_value=40000, value=1400, step=10)
    ave_occup = st.slider('Average Occupancy', min_value=1.0, max_value=15.0, value=3.0, step=0.1)
    latitude = st.slider('Latitude', min_value=32.0, max_value=42.0, value=35.6, step=0.1)
    longitude = st.slider('Longitude', min_value=-125.0, max_value=-114.0, value=-119.5, step=0.1)

# Column 2: Display prediction
with col2:
    st.header('Prediction')
    
    # Create a 'Predict' button
    if st.button('Predict Price', type="primary"):
        
        # Create a DataFrame from the inputs
        input_data = pd.DataFrame({
            'MedInc': [med_inc],
            'HouseAge': [house_age],
            'AveRooms': [ave_rooms],
            'AveBedrms': [ave_bedrms],
            'Population': [population],
            'AveOccup': [ave_occup],
            'Latitude': [latitude],
            'Longitude': [longitude],
            'Rooms per person' : [Rooms_per_person],
            'Bedrooms per room' : [Bedrms_per_room]
        })
        
        # Make a prediction
        prediction = model.predict(input_data)[0]
        
        # Format the prediction as currency
        prediction_price = prediction * 100000 
        
        # Display the result
        st.success(f'**Predicted Median House Value:**')
        st.header(f'${prediction_price:,.2f}')
