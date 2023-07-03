import streamlit as st

# Get the URL parameters
url = st.experimental_get_query_params()
uniqID = url.get('uniqID', [''])[0]
email = url.get('email', [''])[0]

# Display the values
st.write('uniqID:', uniqID)
st.write('email:', email)
st.sidebar.title("Sidebar")

# Add different elements to the sidebar
st.sidebar.text("This is the sidebar.")
st.sidebar.button("Click me!")
