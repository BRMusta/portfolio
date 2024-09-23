# -*- coding: utf-8 -*-
"""
----------------
@author: BRMusta
----------------
"""

import streamlit as st
import app_scripts.main_functions as fct

st.set_page_config(
    page_title="BRMusta",
    page_icon="🧑‍💻",
    layout="wide",
)
st.sidebar.success("@BRMusta")
st.header("@BRMusta")

st.markdown(
    """
    ## Data Analysis Consulting
    ### Structure, Analyze and Visualize your Data - from supporting any decisions to driving global change
    *Under development...*
    """
)

def main():
    # Load the JSON data from the file and store it in main_data variable
    main_data = fct.load_json("db/main_data.json")
    # Call the function with the appropriate JSON section
    fct.section_columns(main_data.get("main_data_services", {}), 3)
    fct.section_image_text_col(main_data.get("about_me", {}), 0.25, 0.75)
    return None

if __name__ == "__page__":
    main()
