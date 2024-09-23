# -*- coding: utf-8 -*-
"""
----------------
@author: BRMusta
----------------
"""

import streamlit as st
import json
import numpy as np
import pandas as pd

def load_json(path):
    # Open and read the JSON file
    try:
        with open(path, "r") as file:
            main_data = json.load(file)
    except FileNotFoundError:
        st.error("The JSON file was not found.")
        st.stop()
    except json.JSONDecodeError:
        st.error("Error decoding the JSON file.")
        st.stop()
    return main_data

def nav_menu(index = {}):
    sections_idx, pages_idx = index.get("sections", None), index.get("pages", None)
    visible_pages, hidden_pages = {}, {}
    for page_id in pages_idx:
        page_attributes = pages_idx.get(page_id, None)
        try:
            with open(page_attributes.get("path", None), "r") as tmp:
                path = page_attributes.get("path", None)
        except FileNotFoundError:
            path = None
        title = page_attributes.get("title", None)
        icon = page_attributes.get("icon", None)
        default = page_attributes.get("default", False)
        url_path = page_attributes.get("url_path", None)
        st_page = st.Page(page = path, title = title, icon = icon, default = default, url_path = url_path)
        position = page_attributes.get("position", "hidden")
        section_id = page_attributes.get("section_id", None)
        section = sections_idx.get(section_id, None).get("label", None)
        if section == None:
            section = section_id
        if position != "hidden":
            if section in visible_pages:
                pass
            else:
                visible_pages[section] = []
            visible_pages[section].append(st_page)
        else:
            if section in hidden_pages:
                pass
            else:
                hidden_pages[section] = []
            hidden_pages[section].append(st_page)
    return visible_pages, hidden_pages

def section_columns(json_data_section = {}, columns_number = 3):
    cols_num = int(columns_number)
    # Display section header
    label = json_data_section.get("label", None)
    if label:
        st.header(label, divider=True)
    # json_data_content is preformatted json data sections {section : {label:title, image:path, content:content}}
    json_data_content = json_data_section.get("content", None)
    if json_data_content:
        # Create columns
        len_sections = int(len(json_data_content))
        if len_sections < cols_num:
            cols_num = len_sections
        cols = st.columns(cols_num)
        # Iterate over each section in the JSON data
        for i, section in enumerate(json_data_content):
            section = json_data_content.get(section, {})
            col = cols[i % cols_num]
            # Safely access image, label, and content keys
            image_path = section.get("image", None)
            if image_path:
                try:
                    col.image(image_path)
                except Exception as e:
                    col.warning("Error loading image: {}".format(e))
            label = section.get("label", None)
            if label:
                col.subheader(label)
            content = section.get("content", None)
            if content:
                for content in content:
                    col.markdown(content)
    return None

def section_image_text_col(json_data_section = {}, first_column_spec = 0.3, second_column_spec = 0.7):
    col_1, col_2 = st.columns([first_column_spec, second_column_spec])
    # Safely access image, label, and content keys
    image_path = json_data_section.get("image", None)
    if image_path:
        try:
            col_1.image(image_path)
        except Exception as e:
            col_1.warning("Error loading image: {}".format(e))
    label = json_data_section.get("label", None)
    if label:
        col_2.subheader(label)
    content = json_data_section.get("content", None)
    if content:
        for content in content:
            col_2.markdown(content)
    return None

def section_text_image_col(json_data_section = {}, first_column_spec = 0.7, second_column_spec = 0.3):
    col_1, col_2 = st.columns([first_column_spec, second_column_spec])
    # Safely access image, label, and content keys
    label = json_data_section.get("label", None)
    if label:
        col_1.subheader(label)
    content = json_data_section.get("content", None)
    if content:
        for content in content:
            col_1.markdown(content)
    image_path = json_data_section.get("image", None)
    if image_path:
        try:
            col_2.image(image_path)
        except Exception as e:
            col_2.warning("Error loading image: {}".format(e))
    return None
