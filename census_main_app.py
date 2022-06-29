# Import modules
import numpy as np
import pandas as pd
import streamlit as st

@st.cache()
#streamlit.set_page_config(page_title ="Census Visualisation Web App", layout = 'centered', initial_sidebar_state = 'auto')
def load_data():
	# Load the Adult Income dataset into DataFrame.

	census_df = pd.read_csv('https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/adult.csv', header=None)
	census_df.head()

	# Rename the column names in the DataFrame using the list given above. 

	# Create the list
	column_name =['age', 'workclass', 'fnlwgt', 'education', 'education-years', 'marital-status', 'occupation', 
               'relationship', 'race','gender','capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']

	# Rename the columns using 'rename()'
	for i in range(df.shape[1]):
	  census_df.rename(columns={i:column_name[i]},inplace=True)

	# Print the first five rows of the DataFrame
	census_df.head()

	# Replace the invalid values ' ?' with 'np.nan'.

	census_df['native-country'] = census_df['native-country'].replace(' ?',np.nan)
	census_df['workclass'] = census_df['workclass'].replace(' ?',np.nan)
	census_df['occupation'] = census_df['occupation'].replace(' ?',np.nan)

	# Delete the rows with invalid values and the column not required 

	# Delete the rows with the 'dropna()' function
	census_df.dropna(inplace=True)

	# Delete the column with the 'drop()' function
	census_df.drop(columns='fnlwgt',axis=1,inplace=True)

	return census_df

df = load_data()
import census_home
import census_plots
pages_dict={"Home":census_home,"Plot":census_plots}
st.sidebar.header("Navigation")
select=st.sidebar.radio("Go to",tuple(pages_dict.keys()))
pages_dict[select].app(df)

