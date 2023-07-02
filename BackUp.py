import streamlit as st
query_params = st.experimental_get_query_params()

# Get the value of the 'uniqID' parameter
uniq_id = query_params.get('uniqID', [''])[0]
if not uniq_id:
    # Provide a default value or handle the missing parameter here
    st.markdown(f"uniqID not provided,[GO TO HOME](https://free-storage.streamlit.app/)")
else:
    # Display the value of 'uniqID'
    st.write("uniqID:", uniq_id)
