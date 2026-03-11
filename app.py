import streamlit as st
import pandas as pd

st.title("Talking Rabbitt - AI Data Assistant")

uploaded_file = st.file_uploader("Upload your CSV file")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Dataset Preview")
    st.dataframe(df)

    question = st.text_input("Ask a question about your data")

    if question:
        st.write("Example Insight:")
        st.write("Total rows in dataset:", len(df))
