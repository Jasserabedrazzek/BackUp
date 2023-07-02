import streamlit as st
query_params = st.experimental_get_query_params()

# Get the value of the 'uniqID' parameter
uniq_id = query_params.get('uniqID', [''])[0]
if not uniq_id:
    # Redirect to the specified URL
    st.redirect('https://free-storage.streamlit.app/')
# Display the value of 'uniqID'
st.write("uniqID:", uniq_id)
