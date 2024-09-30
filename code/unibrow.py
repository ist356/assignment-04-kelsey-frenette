'''
Solution unibrow.py
'''
import pandas as pd
import streamlit as st
import pandaslib as pl

st.title("UniBrow")
st.caption("The Universal data browser")

file = st.file_uploader("Upload a file:", type=["csv", "xlsx", "json"]) #upload file from computer
if file:
    file_type = pl.get_file_extension(file.name) #get file extension
    df = pl.load_file(file, file_type) #load file into pandas dataframe
    cols = pl.get_column_names(df) #get column names inot streamlit
    selected_cols = st.multiselect("Select columns to display", cols, default=cols) #select columns to display
    if st.toggle("Filter data"): #toggle to filter data
        stcols = st.columns(3) 
        text_cols = pl.get_columns_of_type(df, 'object') #get columns of type object
        filter_col = stcols[0].selectbox("Select column to filter", text_cols) #select column to filter
        if filter_col: #if filter column is selected
            vals = pl.get_unique_values(df, filter_col) #get unique values
            val = stcols[1].selectbox("Select value to filter On", vals) #select value to filter on
            df_show = df[df[filter_col] == val][selected_cols]  #filter data
    else:
        df_show = df[selected_cols] #display selected columns

    st.dataframe(df_show) #display dataframe
    st.dataframe(df_show.describe()) #display dataframe description

