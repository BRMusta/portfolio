# -*- coding: utf-8 -*-
"""
----------------
@author: BRMusta
----------------
"""

import streamlit as st
import app_scripts.main_functions as fct

pages_json = fct.load_json("pages/index.json")
visible_pages, hidden_pages = fct.nav_menu(pages_json)

def main():
    sidebar_menu = st.navigation(visible_pages, position="sidebar")
    # sidebar_menu.add_item(st.navigation(hidden_pages, position="hidden"))
    sidebar_menu.run()

if __name__ == "__main__":
    main()
