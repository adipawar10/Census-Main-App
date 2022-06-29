import streamlit as st 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
def app(df):
	st.sidebar.subheader("Charts")
chart_list=st.sidebar.multiselect("Select the type of charts:",["Scatter Plot","Histogram","Box Plot","Count Plot","Pie Chart","Coorelation Heatmap","Line Chart","Area Chart"])
if "Scatter Plot" in chart_list:
    data_list=st.sidebar.multiselect("Select the columns for scatter plot:",["age","education-years","capital-gain","capital-loss","hours-per-week"])
    for i in data_list:
        st.write(f'Scatterplot for {i}')
        plt.figure(figsize=(20,10))
        plt.scatter(df[i],df["income-group"])
        st.pyplot()
if "Box Plot" in chart_list:
    data_list=st.sidebar.multiselect("Select the columns for box plot:",["age","education-years","capital-gain","capital-loss","hours-per-week"])
    for i in data_list:
        st.write(f'Boxplot for {i}')
        plt.figure(figsize=(20,10))
        sns.boxplot(df[i])
        st.pyplot()
if "Histogram" in chart_list:
    data_list=st.sidebar.multiselect("Select the columns for histogram:",["age","education-years","capital-gain","capital-loss","hours-per-week"])
    for i in data_list:
        st.write(f'Histogram for {i}')
        plt.figure(figsize=(20,10))
        sns.distplot(df[i])
        st.pyplot()
if "Count Plot" in chart_list:
    st.write(f'CountPlot')
    plt.figure(figsize=(20,10))
    sns.countplot(df["income-group"])
    st.pyplot()
if "Pie Chart" in chart_list:
    st.write(f'PieChart')
    plt.figure(figsize=(20,10))
    plt.pie(df["income-group"].value_counts(),labels=df["income-group"].value_counts().index,autopct="%.2f%%")
    st.pyplot()
if "Coorelation Heatmap" in chart_list:
    st.write(f'Corelation Heatmap')
    plt.figure(figsize=(20,10))
    sns.heatmap(df.corr(),annot=True)
    st.pyplot()
if "Line Chart" in chart_list:
    st.write(f"Line Chart")
    plt.figure(figsize=(20,10))
    st.line_chart(df)
    st.pyplot()
if "Area Chart" in chart_list:
    st.write(f"Area Chart")
    plt.figure(figsize=(20,10))
    st.area_chart(df)
    st.pyplot()
