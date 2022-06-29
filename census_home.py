import streamlit as st
def app(df):
	st.title("Census Visualisation Web App")
	st.write("This web app allows a user to explore and visualise the census data.")
	st.title("View Data:")
	with st.expander("Dataset"):
		st.table(df)
	#with col3:
		#if st.checkbox("Show Column Data:"):
	        #var=st.selectbox("Columns",["age","education-years","capital-gain","capital-loss","hours-per-week"])
            #st.write(df[var])
	st.title("Data Description:")
	if st.checkbox("Show Summary:"):
		st.table(df.describe())
	col1,col2=st.columns(2)
	with col1:
		if st.checkbox("Column Names:"):
			st.table(df.columns)
	with col2:
		if st.checkbox("Column Datatype:"):
		    st.write(list(df.dtypes))
	
