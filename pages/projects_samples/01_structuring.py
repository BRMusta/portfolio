# -*- coding: utf-8 -*-
"""
----------------
@author: BRMusta
----------------
"""

import streamlit as st

st.set_page_config(
    page_title="BRMusta",
    page_icon="🧑‍💻",
    # layout="wide",
)
st.sidebar.success("🔢 Structuring")
st.header("🔢 Structuring")

st.sidebar.page_link("pages/projects_samples/01_structuring.py", label="🔢 Structuring")
st.sidebar.page_link("pages/projects_samples/02_analyzing.py", label="🔎 Analyzing")
st.sidebar.page_link("pages/projects_samples/03_visualizing.py", label="📈 Visualizing")

st.markdown(
    """
    *Under development...*
    """
)
