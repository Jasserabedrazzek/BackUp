import streamlit as st
import json
import os

# Get the URL parameters
url = st.experimental_get_query_params()
uniqID = url.get('uniqID', [''])[0]
email = url.get('email', [''])[0]
Name = url.get('name',[''])[0]
Lname = url.get('Lname',[''])[0]

st.set_page_config(
    page_title="Chat with developers",
    page_icon="	:computer:",
    layout="centered",
    initial_sidebar_state="expanded"
)
st.header("Chat")
st.write("---")
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
def MakeFileJson(IDuser , Name , LastName , Email ):
    UserInformations = {
        "Name" : Name ,
        "Last Name" : LastName ,
        "Email" : Email ,
        "messages" : ""
    }
    JsonFile = f"{str(IDuser)}.json"
    try :
        if os.path.exists(JsonFile):
            pass
        else:
            with open(JsonFile , "w") as SaveUserFile :
                json.dumps(UserInformations)
            
    except :
        pass
    
if uniqID:
    Id = uniqID
    JsonFile = f"{str(Id)}.json"
    
    st.sidebar.title("User")
    st.sidebar.text(f"Name : {Name}")
    st.sidebar.text(f"Last name : {Lname}")
    st.sidebar.text(f"Email : {email}")
    st.sidebar.text(f"Id : {Id}")
    
    
    
    selected_options = st.sidebar.multiselect(
        'Select options',
        languages,
        default=languages[0]
    )
    st.write('---')
    st.text_input(email,'')
    code = st.text_area("Whrite code (optional)",key="code_area")
    selected_optionsl = st.multiselect(
        'Select Languages',
        languages,
        default=languages[0]
         )
    if len(selected_optionsl) == 1:
        lang = selected_optionsl[0]
        st.code(code, language=lang, line_numbers=True)
    else:
        st.error("Please select exactly one language.")
    
else:
    pass
    

