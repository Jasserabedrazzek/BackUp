import streamlit as st

# Get the URL parameters
url = st.experimental_get_query_params()
uniqID = url.get('uniqID', [''])[0]
email = url.get('email', [''])[0]

if email and uniqID:
  Id = unqID
  st.sidebar.title("user")
  st.sidebar.text(f"Email : {email}")
  st.sidebar.text(f"Id : {Id}")




