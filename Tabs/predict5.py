import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Hide Streamlit style elements
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
                This app uses <b style="color:green">Random Forest Regressor</b> for Cloud Infrastructure Analysis.
            </p>
        """, unsafe_allow_html=True)
    
    # Add subheader for input values
    st.subheader("Select Values:")

    col1, col2 = st.columns(2)

    with col1:
        # Input features from the user using sliders
        vpc_controls = st.slider("VPC Controls", 0, 1)
        segmentation_of_duties = st.slider("Segmentation of Duties", 0, 1)
        instance_metadata_access = st.slider("Instance Metadata Service Access", 0, 1)
        shared_responsibility = st.slider("Shared Responsibility Model", 0, 1)
        storage_access_policies = st.slider("Cloud Storage Access Policies", 0, 1)
        data_governance = st.slider("Data Governance Framework", 0, 1)
        api_gateway_security = st.slider("API Gateway Security", 0, 1)
        dynamic_access_management = st.slider("Dynamic Access Management", 0, 1)
        sensitive_compute_access = st.slider("Access to Sensitive Compute Resources", 0, 1)

    # Map slider values to feature labels
    vpc_control_status = {1: 'Enabled', 0: 'Disabled'}.get(vpc_controls)
    segmentation_duties_status = {1: 'Implemented', 0: 'Not Implemented'}.get(segmentation_of_duties)
    instance_metadata_access_status = {1: 'Allowed', 0: 'Blocked'}.get(instance_metadata_access)
    shared_responsibility_status = {1: 'Clear', 0: 'Unclear'}.get(shared_responsibility)
    storage_access_policies_status = {1: 'Enforced', 0: 'Not Enforced'}.get(storage_access_policies)
    data_governance_status = {1: 'In Place', 0: 'Not In Place'}.get(data_governance)
    api_gateway_security_status = {1: 'Secured', 0: 'Not Secured'}.get(api_gateway_security)
    dynamic_access_management_status = {1: 'Enabled', 0: 'Disabled'}.get(dynamic_access_management)
    sensitive_compute_access_status = {1: 'Granted', 0: 'Restricted'}.get(sensitive_compute_access)

    with col2:
        # Display the selected values in a table
        st.markdown(f"""
            <table style="width:100%">
                <tr><th>Feature</th><th>Selected Value</th></tr>
                <tr><td>VPC Controls</td><td>{vpc_control_status}</td></tr>
                <tr><td>Segmentation of Duties</td><td>{segmentation_duties_status}</td></tr>
                <tr><td>Instance Metadata Service Access</td><td>{instance_metadata_access_status}</td></tr>
                <tr><td>Shared Responsibility Model</td><td>{shared_responsibility_status}</td></tr>
                <tr><td>Cloud Storage Access Policies</td><td>{storage_access_policies_status}</td></tr>
                <tr><td>Data Governance Framework</td><td>{data_governance_status}</td></tr>
                <tr><td>API Gateway Security</td><td>{api_gateway_security_status}</td></tr>
                <tr><td>Dynamic Access Management</td><td>{dynamic_access_management_status}</td></tr>
                <tr><td>Access to Sensitive Compute Resources</td><td>{sensitive_compute_access_status}</td></tr>
            </table>
        """, unsafe_allow_html=True)

    # Create a list of features for prediction
    features = [vpc_controls, segmentation_of_duties, instance_metadata_access, shared_responsibility,
                storage_access_policies, data_governance, api_gateway_security,
                dynamic_access_management, sensitive_compute_access]

    # Reshape features for prediction
    features_array = np.array(features).reshape(1, -1)

    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize RandomForestRegressor
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)

    # Create a button for prediction
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