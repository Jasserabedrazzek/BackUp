import streamlit as st

# Get the URL parameters
url = st.experimental_get_query_params()
uniqID = url.get('uniqID', [''])[0]
email = url.get('email', [''])[0]
Name = url.get('name',[''])[0]

if email and uniqID:
  Id = uniqID
  st.sidebar.title("user")
  st.sidebar.text(f"Name : {name}")
  st.sidebar.text(f"Email : {email}")
  st.sidebar.text(f"Id : {Id}")




