"""This is the main module to run the app"""

# Importing the necessary Python modules.
import streamlit as st

# Import necessary functions from web_functions
from web_functions import load_data

# Configure the app
st.set_page_config(
    page_title = 'Cloud Architecture Analysis',
    page_icon ='🌨️',
    layout = 'wide',
    initial_sidebar_state = 'auto'
)

# Import pages
from Tabs import home, data, predict, predict2, predict3, predict4, predict5, predict6, faq #visualise



# Dictionary for pages
Tabs = {
    "Home": home,
    "Data Info": data,
    "Cloud Security Analytics": predict,
    "Cloud Architecture Analytics": predict2,
    "Cloud Billing Analytics": predict3,
    "Cloud Network Traffic Analytics": predict4,
    "Cloud Compute Analytics": predict5,
    "Cloud Sustainability Analytics": predict6,
    "FAQ": faq
    #"Visualisation": visualise
    #"About me": about
}

# Create a sidebar
# Add title to sidear
st.sidebar.title("Navigation")

# Create radio option to select the page
page = st.sidebar.radio("Pages", list(Tabs.keys()))

# Loading the dataset.
df, X, y = load_data()

# Call the app funciton of selected page to run
if page in ["Cloud Security Analytics","Cloud Architecture Analytics","Cloud Billing Analytics","Cloud Network Traffic Analytics","Cloud Compute Analytics","Cloud Sustainability Analytics"]:
    Tabs[page].app(df, X, y)
elif (page == "Data Info" or page=="FAQ"):
    Tabs[page].app(df)
else:
    Tabs[page].app()
