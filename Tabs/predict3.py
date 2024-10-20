import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# Hide Streamlit default menu and footer
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
                    <td style="border: 1px solid black; padding: 5px;">Data Sensitivity Classification</td>
                    <td style="border: 1px solid black; padding: 5px;">1: Public, 2: Private, 3: Confidential, 4: Very Confidential</td>
                </tr>
                <tr>
                    <td style="border: 1px solid black; padding: 5px;">Logging and Monitoring</td>
                    <td style="border: 1px solid black; padding: 5px;">1: Enabled, 0: Disabled</td>
                </tr>
                <tr>
                    <td style="border: 1px solid black; padding: 5px;">Cross Region Access</td>
                    <td style="border: 1px solid black; padding: 5px;">1: Enabled, 0: Disabled</td>
                </tr>
                <tr>
                    <td style="border: 1px solid black; padding: 5px;">Segmentation of Duties</td>
                    <td style="border: 1px solid black; padding: 5px;">1: Implemented, 0: Not Implemented</td>
                </tr>
                <tr>
                    <td style="border: 1px solid black; padding: 5px;">Shared Responsibility Model</td>
                    <td style="border: 1px solid black; padding: 5px;">1: Clear, 0: Unclear</td>
                </tr>
                <tr>
                    <td style="border: 1px solid black; padding: 5px;">Access Control Propagation</td>
                    <td style="border: 1px solid black; padding: 5px;">1: Propagated, 0: Not Propagated</td>
                </tr>
                <tr>
                    <td style="border: 1px solid black; padding: 5px;">API Access Control</td>
                    <td style="border: 1px solid black; padding: 5px;">1: Implemented, 0: Not Implemented</td>
                </tr>
                <tr>
                    <td style="border: 1px solid black; padding: 5px;">Cloud Workload Identity</td>
                    <td style="border: 1px solid black; padding: 5px;">1: Enabled, 0: Disabled</td>
                </tr>
                <tr>
                    <td style="border: 1px solid black; padding: 5px;">Audit Trails</td>
                    <td style="border: 1px solid black; padding: 5px;">1: Enabled, 0: Disabled</td>
                </tr>
            </table>
        """, unsafe_allow_html=True)

    st.divider()
    st.subheader("Select Values:")

    col1, col2 = st.columns(2)

    with col1:
        # Input features from the user
        a3 = st.slider("Data Sensitivity Classification", 1, 4)
        b3 = st.slider("Logging and Monitoring", 0, 1)
        c3 = st.slider("Cross Region Access", 0, 1)
        d3 = st.slider("Segmentation of Duties", 0, 1)
        e3 = st.slider("Shared Responsibility Model", 0, 1)
        f3 = st.slider("Access Control Propagation", 0, 1)
        g3 = st.slider("API Access Control", 0, 1)
        h3 = st.slider("Cloud Workload Identity", 0, 1)
        i3 = st.slider("Audit Trails", 0, 1)

    # Map slider values to feature labels
    data_sensitivity = {1: 'Public', 2: 'Private', 3: 'Confidential', 4: 'Very Confidential'}.get(a3)
    logging_monitoring = {1: 'Enabled', 0: 'Disabled'}.get(b3)
    cross_region_access = {1: 'Enabled', 0: 'Disabled'}.get(c3)
    segmentation_of_duties = {1: 'Implemented', 0: 'Not Implemented'}.get(d3)
    shared_responsibility = {1: 'Clear', 0: 'Unclear'}.get(e3)
    access_control_propagation = {1: 'Propagated', 0: 'Not Propagated'}.get(f3)
    api_access_control = {1: 'Implemented', 0: 'Not Implemented'}.get(g3)
    cloud_workload_identity = {1: 'Enabled', 0: 'Disabled'}.get(h3)
    audit_trails = {1: 'Enabled', 0: 'Disabled'}.get(i3)

    with col2:
        # Display the selected values in a structured format
        st.markdown(f"""
            <table style="width:100%">
                <tr><th>Feature</th><th>Selected Value</th></tr>
                <tr><td>Data Sensitivity Classification</td><td>{data_sensitivity}</td></tr>
                <tr><td>Logging and Monitoring</td><td>{logging_monitoring}</td></tr>
                <tr><td>Cross Region Access</td><td>{cross_region_access}</td></tr>
                <tr><td>Segmentation of Duties</td><td>{segmentation_of_duties}</td></tr>
                <tr><td>Shared Responsibility Model</td><td>{shared_responsibility}</td></tr>
                <tr><td>Access Control Propagation</td><td>{access_control_propagation}</td></tr>
                <tr><td>API Access Control</td><td>{api_access_control}</td></tr>
                <tr><td>Cloud Workload Identity</td><td>{cloud_workload_identity}</td></tr>
                <tr><td>Audit Trails</td><td>{audit_trails}</td></tr>
            </table>
        """, unsafe_allow_html=True)

    # Create a feature list for prediction
    features = [a3, b3, c3, d3, e3, f3, g3, h3, i3]
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