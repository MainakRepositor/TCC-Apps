import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

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
    
    # Take feature input from the user
    st.subheader("Select Values:")

    col1, col2 = st.columns(2)

    with col1: 
        # Input features using sliders
        a3 = st.slider("API Access Control", 0, 1)
        b3 = st.slider("Cloud Workload Identity", 0, 1)
        c3 = st.slider("DLP Policies", 0, 1)
        d3 = st.slider("Infrastructure as Code", 0, 1)
        e3 = st.slider("Cloud Native Directory Services", 0, 1)
        f3 = st.slider("Access to Logs and Monitoring Tools", 0, 1)
        g3 = st.slider("Granular Access Control", 0, 1)
        h3 = st.slider("Custom Access Control Policies", 0, 1)
        i3 = st.slider("Zero Trust Architecture", 0, 1)

    # Map slider values to feature labels
    api_access_control = {1: 'Implemented', 0: 'Not Implemented'}.get(a3)
    cloud_workload_identity = {1: 'Enabled', 0: 'Disabled'}.get(b3)
    dlp_policies = {1: 'Enabled', 0: 'Disabled'}.get(c3)
    infra_as_code = {1: 'Implemented', 0: 'Not Implemented'}.get(d3)
    cloud_native_directory = {1: 'Enabled', 0: 'Disabled'}.get(e3)
    access_to_logs = {1: 'Granted', 0: 'Not Granted'}.get(f3)
    granular_access_control = {1: 'Enabled', 0: 'Disabled'}.get(g3)
    custom_access_policies = {1: 'Enabled', 0: 'Disabled'}.get(h3)
    zero_trust_architecture = {1: 'Implemented', 0: 'Not Implemented'}.get(i3)

    with col2:
        # Display the selected values in a structured format
        st.markdown(f"""
            <table style="width:100%">
                <tr><th>Feature</th><th>Selected Value</th></tr>
                <tr><td>API Access Control</td><td>{api_access_control}</td></tr>
                <tr><td>Cloud Workload Identity</td><td>{cloud_workload_identity}</td></tr>
                <tr><td>DLP Policies</td><td>{dlp_policies}</td></tr>
                <tr><td>Infrastructure as Code</td><td>{infra_as_code}</td></tr>
                <tr><td>Cloud Native Directory Services</td><td>{cloud_native_directory}</td></tr>
                <tr><td>Access to Logs and Monitoring Tools</td><td>{access_to_logs}</td></tr>
                <tr><td>Granular Access Control</td><td>{granular_access_control}</td></tr>
                <tr><td>Custom Access Control Policies</td><td>{custom_access_policies}</td></tr>
                <tr><td>Zero Trust Architecture</td><td>{zero_trust_architecture}</td></tr>
            </table>
        """, unsafe_allow_html=True)

    # Create a feature list for prediction
    features = [a3, b3, c3, d3, e3, f3, g3, h3, i3]
    features_array = np.array(features).reshape(1, -1)

    # Train the RandomForestRegressor model
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)

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
