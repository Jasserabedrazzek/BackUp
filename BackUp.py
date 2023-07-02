import streamlit as st
import json

# Get the uniqID from the URL parameters
uniqID = st.experimental_get_query_params().get("uniqID", [None])[0]

# Load and display the user account data
if uniqID:
    filename = f"{uniqID}.json"
    try:
        with open(filename, "r") as user:
            account = json.load(user)
        st.write("User Account:")
        st.write(f"Name: {account['nom']}")
        st.write(f"Last Name: {account['prenom']}")
        st.write(f"Email: {account['Email']}")
    except FileNotFoundError:
        st.error("User account not found")
else:
    st.error("Invalid URL")
