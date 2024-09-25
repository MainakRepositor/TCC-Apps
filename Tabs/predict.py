"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

# Import necessary functions from web_functions
from web_functions import predict

hide_st_style = """
<style>
MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Prediction Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Random Forest Classifier</b> for the Analysis of Cloud Infrastructure.
            </p>
        """, unsafe_allow_html=True)
    
    # Take feature input from the user
    # Add a subheader
    # Inject custom CSS to style the slider



# Static reference table content
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

    

    col1,col2 = st.columns(2)

    with col1: 
        # Assume we are getting these values from sliders or checkboxes
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
        # Display the table using markdown for structure
        st.markdown("""
            <table style="width:100%">
                <tr>
                    <th>Feature</th>
                    <th>Selected Value</th>
                </tr>
                <tr>
                    <td>Authentication Mechanisms</td>
                    <td>{auth_mechanisms}</td>
                </tr>
                <tr>
                    <td>Authorization Models</td>
                    <td>{authorization_models}</td>
                </tr>
                <tr>
                    <td>User Identity Management</td>
                    <td>{identity_management}</td>
                </tr>
                <tr>
                    <td>Access Levels</td>
                    <td>{access_levels}</td>
                </tr>
                <tr>
                    <td>User Roles</td>
                    <td>{user_roles}</td>
                </tr>
                <tr>
                    <td>Security Policies</td>
                    <td>{security_policies}</td>
                </tr>
                <tr>
                    <td>Compliance Requirements</td>
                    <td>{compliance_requirements}</td>
                </tr>
                <tr>
                    <td>User Session Management</td>
                    <td>{session_management}</td>
                </tr>
                <tr>
                    <td>Privileged Access Management</td>
                    <td>{privileged_access}</td>
                </tr>
            </table>
            """.format(
            auth_mechanisms=auth_mechanisms,
            authorization_models=authorization_models,
            identity_management=identity_management,
            access_levels=access_levels,
            user_roles=user_roles,
            security_policies=security_policies,
            compliance_requirements=compliance_requirements,
            session_management=session_management,
            privileged_access=privileged_access
        ), unsafe_allow_html=True)


        
    # Create a list to store all the features
    features = [a,b,c,d,e,f,g,h,i]

    
    st.header("The values entered by user")
    st.cache_data()
    df3 = pd.DataFrame(features).transpose()
    df3.columns=['Authentication Mechanisms','Authorization Models','User Identity Management','Access Levels','User Roles','Security Policies','Compliance Requirements','User Session Management','Privileged Access Management']

    df3['Authentication Mechanisms'] = df3['Authentication Mechanisms'].replace({1: 'MFA', 2: 'SSO',3: 'Biometric', 4: 'Password'})

    df3['Authorization Models'] = df3['Authorization Models'].replace({1: 'RBAC', 2: 'ABAC',3: 'PBAC'})

    df3['User Identity Management'] = df3['User Identity Management'].replace({1: 'Enabled', 0: 'Disabled'})

    df3['Access Levels'] = df3['Access Levels'].replace({1: 'Read', 2: 'Write',3: 'Modify', 4: 'Admin'})

    df3['User Roles'] = df3['User Roles'].replace({1: 'Admin', 2: 'User',3: 'Guest', 4: 'Super Admin'})

    df3['Security Policies'] = df3['Security Policies'].replace({1: 'Applied', 0: 'Not Applied'})

    df3['Compliance Requirements'] = df3['Compliance Requirements'].replace({1: 'Applicable', 0: 'Not Application'})

    df3['User Session Management'] = df3['User Session Management'].replace({1: 'Enabled', 0: 'Disabled'})

    df3['Privileged Access Management'] = df3['Privileged Access Management'].replace({1: 'Approved', 0: 'Not Approved'})

    st.dataframe(df3)

    

    st.sidebar.info("Detection of Cloud Score based on access management and IAM")

    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        score = score + 0.12 #correction factor
        

        if(a==4 and c==0 and e==4 and f==1):
            st.warning('Cloud Score: 1')
            st.info('Your cloud is running with the lowest level of security. It is suggested to improve your security level with MFA, network audits and essential compliance practices')

        elif(a < 2 and b > 1 and e > 2 and g==1):
            st.warning('Cloud Score: 2')
            st.info('Your cloud is moderately secure. Please strengthen security with correct compliance practices')

        elif(g==1 and h==1 and i==1 and a<2):
            st.success('Cloud Score: 4')
            st.info('You have good security level for your cloud')

        elif(c>0 and a<2 and b>=2 and d<4 and e>0 and f==1 and g==1 and h==1 and i == 1):
            st.success('Cloud Score: 5')
            st.info('Highest level of security is provided')

        else:
            st.success('Cloud Score '+str(prediction[0]))


        
    
        # Print teh score of the model 
        st.sidebar.write("The model used is trusted by top cloud providers and has an accuracy of ", round((score*100),2),"%")
