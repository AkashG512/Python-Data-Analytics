import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Simple Data Dashboard")

uploaded_files = st.file_uploader("Chose a CSV file", type="csv")

if uploaded_files is not None:
    st.write("File uploaded....")

    df = pd.read_csv(uploaded_files)
    st.subheader("data Preview")

    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select a column to filter by", columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select a value to filter by", unique_values)
    
    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)

    st.subheader("Plot Data")
    x_column = st.selectbox("Select X-Axis column", columns)
    y_column = st.selectbox("Select Y-Axis column", columns)

    if st.button("Generate plot"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])
    else:
        st.write("waiting on file upload...")