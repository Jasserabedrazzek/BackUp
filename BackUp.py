import streamlit as st
import json

st.set_page_config(page_title=f'Welcome',
                   page_icon='',
                   layout='centered',
                   initial_sidebar_state='auto')

query_params = st.experimental_get_query_params()

# Get the value of the 'uniqID' parameter
uniq_id = query_params.get('uniqID', [''])[0]
if not uniq_id:
    # Provide a default value or handle the missing parameter here
    st.markdown(f"uniqID not provided , [Go to login page](https://free-storage.streamlit.app/) .")
else:
    # Display the value of 'uniqID'
    Id = uniq_id
    FileName = f'{Id}.json'
    try:
        with open(FileName,'r') as file:
            user = json.load(file)
            st.write(user)
    except FileNotFoundError :
        st.markdown(f"uniqID not provided , [Go to login page](https://free-storage.streamlit.app/) .")


