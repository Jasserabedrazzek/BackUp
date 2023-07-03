import streamlit as st

# Get the uniqID from the URL parameters
uniqID = st.experimental_get_query_params().get("uniqID", [None])[0]
if uniqID and len(str(uniqID)) == 12 :
    ID = uniqID
    st.set_page_config(page_title=f'Welcome {ID}',
                   page_icon='',
                   layout='centered',
                   initial_sidebar_state='auto')

























else:
    st.markdown("[Retunr Home Page](https://free-storage.streamlit.app/)")
