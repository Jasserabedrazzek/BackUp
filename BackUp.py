import streamlit as st

def get_uniqID_and_email():
    uniqID = st.session_state["uniqID"]
    email = st.session_state["email"]
    return uniqID, email

uniqID, email = get_uniqID_and_email()

st.write("The uniqID is:", uniqID)
st.write("The email is:", email)
