import streamlit as st
import json
import os

# Get the URL parameters
url = st.experimental_get_query_params()
uniqID = url.get('uniqID', [''])[0]
email = url.get('email', [''])[0]
Name = url.get('name', [''])[0]
Lname = url.get('Lname', [''])[0]

st.set_page_config(
    page_title="Chat with developers",
    page_icon=":computer:",
    layout="centered",
    initial_sidebar_state="expanded"
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


def MakeFileJson(IDuser, Name, LastName, Email):
    UserInformations = {
        "Name": Name,
        "Last Name": LastName,
        "Email": Email,
        "messages": ""
    }
    JsonFile = f"{str(IDuser)}.json"
    try:
        if os.path.exists(JsonFile):
            pass
        else:
            with open(JsonFile, "w") as SaveUserFile:
                json_data = json.dumps(UserInformations)
                SaveUserFile.write(json_data)

    except Exception as e:
        st.error(f"Error creating JSON file: {e}")


if uniqID:
    Id = uniqID
    JsonFile = f"{str(Id)}.json"
    MakeFileJson(Id, Name, Lname, email)
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

    with open(JsonFile, "r") as f:
        st.write(json.load(f))

else:
    pass


# Check if the JSON file exists
def check_json_file():
    json_file = "data.json"

    if not st.session_state.json_file_created:
        try:
            with open(json_file, "w") as f:
                initial_data = {"key": "value"}  # Replace with your initial JSON data
                json.dump(initial_data, f)
                st.session_state.json_file_created = True
                st.success("JSON file created successfully!")
        except Exception as e:
            st.error(f"Error creating JSON file: {e}")


# Register the event handler to check JSON file on page load
st.session_state.json_file_created = False
st.on_event("startup", check_json_file)

# Streamlit app code
st.title("My App")
st.write("JSON file creation on page load")

# Rest of your Streamlit app code goes here...
