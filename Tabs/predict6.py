"""This module contains data about the prediction page"""

# Import necessary modules
import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# Hide streamlit default menus
hide_st_style = """
<style>
MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

def app(df, X, y):
    """This function creates the prediction page"""

    # Add title to the page
    st.title("Prediction Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Random Forest Regressor</b> for the Analysis of Cloud Infrastructure.
            </p>
        """, unsafe_allow_html=True)

    # Add reference table for the new features
    st.markdown("""
        ### Reference Table for Additional Feature Labels

        <table style="width:100%; border: 1px solid black; border-collapse: collapse;">
            <tr>
                <th style="border: 1px solid black; padding: 5px;">Feature</th>
                <th style="border: 1px solid black; padding: 5px;">Possible Values</th>
            </tr>
            <tr>
                <td style="border: 1px solid black; padding: 5px;">Third Party Integrations</td>
                <td style="border: 1px solid black; padding: 5px;">1: Enabled, 0: Disabled</td>
            </tr>
            <tr>
                <td style="border: 1px solid black; padding: 5px;">Cloud Service Provider</td>
                <td style="border: 1px solid black; padding: 5px;">1: AWS, 2: Azure, 3: Google Cloud</td>
            </tr>
            <tr>
                <td style="border: 1px solid black; padding: 5px;">Geolocation Restrictions</td>
                <td style="border: 1px solid black; padding: 5px;">1: Applied, 0: Not Applied</td>
            </tr>
            <tr>
                <td style="border: 1px solid black; padding: 5px;">Time Based Access</td>
                <td style="border: 1px solid black; padding: 5px;">1: Enabled, 0: Disabled</td>
            </tr>
            <tr>
                <td style="border: 1px solid black; padding: 5px;">User Behavior Analytics</td>
                <td style="border: 1px solid black; padding: 5px;">1: Applied, 0: Not Applied</td>
            </tr>
            <tr>
                <td style="border: 1px solid black; padding: 5px;">Network Security Controls</td>
                <td style="border: 1px solid black; padding: 5px;">1: Applied, 0: Not Applied</td>
            </tr>
            <tr>
                <td style="border: 1px solid black; padding: 5px;">Access Control Lists</td>
                <td style="border: 1px solid black; padding: 5px;">1: Applied, 0: Not Applied</td>
            </tr>
            <tr>
                <td style="border: 1px solid black; padding: 5px;">Encryption Policies</td>
                <td style="border: 1px solid black; padding: 5px;">1: Applied, 0: Not Applied</td>
            </tr>
            <tr>
                <td style="border: 1px solid black; padding: 5px;">Data Sensitivity Classification</td>
                <td style="border: 1px solid black; padding: 5px;">1: Applied, 0: Not Applied</td>
            </tr>
        </table>
    """, unsafe_allow_html=True)

    st.divider()
    st.subheader("Select Values for Additional Features:")

    col1, col2 = st.columns(2)

    with col1:
        # Sliders for new features
        a = st.slider("Third Party Integrations", 0, 1)
        b = st.slider("Cloud Service Provider", 1, 3)
        c = st.slider("Geolocation Restrictions", 0, 1)
        d = st.slider("Time Based Access", 0, 1)
        e = st.slider("User Behavior Analytics", 0, 1)
        f = st.slider("Network Security Controls", 0, 1)
        g = st.slider("Access Control Lists", 0, 1)
        h = st.slider("Encryption Policies", 0, 1)
        i = st.slider("Data Sensitivity Classification", 0, 1)

    # Map slider values to feature labels
    cloud_service_provider_map = {1: 'AWS', 2: 'Azure', 3: 'Google Cloud'}.get(b)

    with col2:
        # Display selected values in a table
        st.markdown(f"""
            <table style="width:100%">
                <tr><th>Feature</th><th>Selected Value</th></tr>
                <tr><td>Third Party Integrations</td><td>{'Enabled' if a else 'Disabled'}</td></tr>
                <tr><td>Cloud Service Provider</td><td>{cloud_service_provider_map}</td></tr>
                <tr><td>Geolocation Restrictions</td><td>{'Applied' if c else 'Not Applied'}</td></tr>
                <tr><td>Time Based Access</td><td>{'Enabled' if d else 'Disabled'}</td></tr>
                <tr><td>User Behavior Analytics</td><td>{'Applied' if e else 'Not Applied'}</td></tr>
                <tr><td>Network Security Controls</td><td>{'Applied' if f else 'Not Applied'}</td></tr>
                <tr><td>Access Control Lists</td><td>{'Applied' if g else 'Not Applied'}</td></tr>
                <tr><td>Encryption Policies</td><td>{'Applied' if h else 'Not Applied'}</td></tr>
                <tr><td>Data Sensitivity Classification</td><td>{'Applied' if i else 'Not Applied'}</td></tr>
            </table>
        """, unsafe_allow_html=True)

    # Create a feature list for prediction
    features = [a, b, c, d, e, f, g, h, i]
    features_array = np.array(features).reshape(1, -1)

    # Train the RandomForestRegressor in-house using provided dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)

    # Create a button to predict
    # Create a button to predict
    if st.button("Predict"):
        # Predict the cloud score using the trained RandomForest model
        
        prediction = rf_model.predict(features_array)
        prediction = (prediction - 3) * 600

        if isinstance(prediction, np.ndarray):
            result = prediction[0]
            

        else:
            result = prediction 
            
        
        if result > 100: result = 100
        result = abs(result)
        # Display the prediction result
        st.success(f"Cloud Security Optimization Level: {result:.2f} %")
        st.sidebar.info("Prediction of Cloud Security based on various access controls")