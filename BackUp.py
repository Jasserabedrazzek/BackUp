import streamlit as st
query_params = st.experimental_get_query_params()

# Get the value of the 'uniqID' parameter
uniq_id = query_params.get('uniqID', [''])[0]
if not uniq_id:
    # Redirect to the specified URL using JavaScript
    redirect_url = 'https://free-storage.streamlit.app/'
    st.markdown(f'<script>window.location.href="{redirect_url}";</script>', unsafe_allow_html=True)
else:
    # Display the value of 'uniqID'
    st.write("uniqID:", uniq_id)
