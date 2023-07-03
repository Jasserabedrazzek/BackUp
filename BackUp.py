import streamlit as st
query_params = st.experimental_get_query_params()
uniqID = query_params.get('uniqID', [''])[0]
email = query_params.get('email', [''])[0]
st.write("uniqID:", uniqID)
st.write("email:", email)
