import streamlit as st

# Get the URL parameters
url = st.experimental_get_query_params()
uniqID = url.get('uniqID', [''])[0]
email = url.get('email', [''])[0]
Name = url.get('name',[''])[0]

st.set_page_config(
    page_title="Chat with devoloppers",
    page_icon="",
    layout="centered",
    initial_sidebar_state="expanded",
    
)
languages = [
    "Python",
    "Java",
    "JavaScript",
    "C++",
    "C#",
    "Ruby",
    "Go",
    "Rust",
    "Swift",
    "Kotlin",
    "TypeScript"
]

if email and uniqID:
  Id = uniqID
  st.sidebar.title("user")
  st.sidebar.text(f"Name : {Name}")
  st.sidebar.text(f"Email : {email}")
  st.sidebar.text(f"Id : {Id}")
  selected_options = st.sidebar.multiselect(
    'Select options',
    languages[0]
)




