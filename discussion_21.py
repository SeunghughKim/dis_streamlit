import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

uploaded_file = st.file_uploader("Upload a CSV file", type = "csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    st,write("Number of rows:", df.shape[0])
    st.write("Number of Columns:", df.shape[1])
    st.write("Number of categorical variables:", len(df.select_dtypes(include='object').columns))
    st.write("Number of numerical variables:", len(df.select_dtypes(include='number').columns))
    st.write("Number of boolean variables:", len(df.select_dtypes(include='bool').columns))

    selected_column = st.selection("Select a column", df.columns)
    
    if df[selected_column].dtype == 'object':
        category_counts = df[selected_column].value_counts(normalize=True)
        st.write("Proportions of each category level:")
        st,write(category_counts)
        
        plt.figure(figsize=(10,6))
        sns.countplot(x=selected_column, data=df)
        plt.xticks(rotation=45)
        st.pyplot()
        
    elif df[selected_column].dtype in ['int64', 'float64']:
        summary = df[selected_column].describe()
        st.write("Five number Summary:")
        st.write(summary)
        
        plt.figure(figsize=(10,6))
        sns.histplot(df[selected_column],kde=TRUE)
        plt.xlabel(selected_column)
        plt.ylabel("Frequency")
        plt.title("Distribution Plot")
        st.pyplot()
