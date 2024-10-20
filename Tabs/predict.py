"""This module contains data about prediction page"""

# Import necessary modules
import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

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
    
    # Static reference table content
    with st.expander("Check Metrics"):
        st.markdown("""
            ### Reference Table for Feature Labels

            <table style="width:100%; border: 1px solid black; border-collapse: collapse;">
                <tr>
                    <th style="border: 1px solid black; padding: 5px;">Feature</th>
                    <th style="border: 1px solid black; padding: 5px;">Possible Values</th>
                </tr>
                <tr>
                    <td style="border: 1px solid black; padding: 5px;">Authentication Mechanisms</td>
                    <td style="border: 1px solid black; padding: 5px;">1: MFA, 2: SSO, 3: Biometric, 4: Password</td>
                </tr>
                <tr>
                    <td style="border: 1px solid black; padding: 5px;">Authorization Models</td>
                    <td style="border: 1px solid black; padding: 5px;">1: RBAC, 2: ABAC, 3: PBAC</td>
                </tr>
                <tr>
                    <td style="border: 1px solid black; padding: 5px;">User Identity Management</td>
                    <td style="border: 1px solid black; padding: 5px;">1: Enabled, 0: Disabled</td>
                </tr>
                <tr>
                    <td style="border: 1px solid black; padding: 5px;">Access Levels</td>
                    <td style="border: 1px solid black; padding: 5px;">1: Read, 2: Write, 3: Modify, 4: Admin</td>
                </tr>
                <tr>
                    <td style="border: 1px solid black; padding: 5px;">User Roles</td>
                    <td style="border: 1px solid black; padding: 5px;">1: Admin, 2: User, 3: Guest, 4: Super Admin</td>
                </tr>
                <tr>
                    <td style="border: 1px solid black; padding: 5px;">Security Policies</td>
                    <td style="border: 1px solid black; padding: 5px;">1: Applied, 0: Not Applied</td>
                </tr>
                <tr>
                    <td style="border: 1px solid black; padding: 5px;">Compliance Requirements</td>
                    <td style="border: 1px solid black; padding: 5px;">1: Applicable, 0: Not Applicable</td>
                </tr>
                <tr>
                    <td style="border: 1px solid black; padding: 5px;">User Session Management</td>
                    <td style="border: 1px solid black; padding: 5px;">1: Enabled, 0: Disabled</td>
                </tr>
                <tr>
                    <td style="border: 1px solid black; padding: 5px;">Privileged Access Management</td>
                    <td style="border: 1px solid black; padding: 5px;">1: Approved, 0: Not Approved</td>
                </tr>
            </table>
        """, unsafe_allow_html=True)

    st.divider()
    st.subheader("Select Values:")

    col1, col2 = st.columns(2)

    with col1:
        # Input features from the user
        a = st.slider("Authentication Mechanisms", 1, 4)
        b = st.slider("Authorization Models", 1, 3)
        c = st.slider("User Identity Management", 0, 1)
        d = st.slider("Access Levels", 1, 4)
        e = st.slider("User Roles", 1, 4)
        f = st.slider("Security Policies", 0, 1)
        g = st.slider("Compliance Requirements", 0, 1)
        h = st.slider("User Session Management", 0, 1)
        i = st.slider("Privileged Access Management", 0, 1)

    # Map slider values to feature labels
    auth_mechanisms = {1: 'MFA', 2: 'SSO', 3: 'Biometric', 4: 'Password'}.get(a)
    authorization_models = {1: 'RBAC', 2: 'ABAC', 3: 'PBAC'}.get(b)
    identity_management = {1: 'Enabled', 0: 'Disabled'}.get(c)
    access_levels = {1: 'Read', 2: 'Write', 3: 'Modify', 4: 'Admin'}.get(d)
    user_roles = {1: 'Admin', 2: 'User', 3: 'Guest', 4: 'Super Admin'}.get(e)
    security_policies = {1: 'Applied', 0: 'Not Applied'}.get(f)
    compliance_requirements = {1: 'Applicable', 0: 'Not Applicable'}.get(g)
    session_management = {1: 'Enabled', 0: 'Disabled'}.get(h)
    privileged_access = {1: 'Approved', 0: 'Not Approved'}.get(i)

    with col2:
        # Display the selected values in a structured format
        st.markdown(f"""
            <table style="width:100%">
                <tr><th>Feature</th><th>Selected Value</th></tr>
                <tr><td>Authentication Mechanisms</td><td>{auth_mechanisms}</td></tr>
                <tr><td>Authorization Models</td><td>{authorization_models}</td></tr>
                <tr><td>User Identity Management</td><td>{identity_management}</td></tr>
                <tr><td>Access Levels</td><td>{access_levels}</td></tr>
                <tr><td>User Roles</td><td>{user_roles}</td></tr>
                <tr><td>Security Policies</td><td>{security_policies}</td></tr>
                <tr><td>Compliance Requirements</td><td>{compliance_requirements}</td></tr>
                <tr><td>User Session Management</td><td>{session_management}</td></tr>
                <tr><td>Privileged Access Management</td><td>{privileged_access}</td></tr>
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