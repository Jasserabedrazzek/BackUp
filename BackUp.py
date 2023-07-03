import streamlit as st
import pandas as pd
import os

# Function to get the database file path
def get_database_path():
    return "uploaded_files.csv"

# Function to load the database into a DataFrame
def load_database():
    db_path = get_database_path()
    if os.path.exists(db_path):
        return pd.read_csv(db_path)
    else:
        return pd.DataFrame(columns=['ID', 'File'])

# Function to save the database
def save_database(df):
    df.to_csv(get_database_path(), index=False)

# Function to delete a file from the database and file system
def delete_file(file_id):
    df = load_database()
    file_row = df.loc[df['ID'] == file_id]
    if not file_row.empty:
        file_path = file_row['File'].values[0]
        if os.path.exists(file_path):
            os.remove(file_path)
        df = df[df['ID'] != file_id]
        save_database(df)

# Function to display the uploaded files with options to delete and share
def display_uploaded_files():
    df = load_database()
    if not df.empty:
        st.subheader("Uploaded Files:")
        for index, row in df.iterrows():
            file_id = row['ID']
            file_path = row['File']
            st.write(f"**ID:** {file_id}")
            st.write(f"**File Name:** {os.path.basename(file_path)}")
            if st.button(f"Delete {file_id}"):
                delete_file(file_id)
                st.success("File deleted successfully.")
        st.subheader("Share File:")
        # Add code to implement the functionality for sharing the file here.

# Main code starts here
uniqID = st.experimental_get_query_params().get("uniqID", [None])[0]
if uniqID and len(str(uniqID)) == 12:
    ID = uniqID
    st.set_page_config(page_title=f'Welcome {ID}',
                       page_icon='',
                       layout='centered',
                       initial_sidebar_state='auto')
    UploadFile = st.file_uploader("Choose a file")
    if UploadFile:
        # Create the "uploads" directory if it doesn't exist
        if not os.path.exists("uploads"):
            os.makedirs("uploads")
        # Save the uploaded file and add its entry to the database
        file_path = os.path.join("uploads", f"{ID}_{UploadFile.name}")
        with open(file_path, "wb") as f:
            f.write(UploadFile.getbuffer())
        df = load_database()
        new_row = {'ID': ID, 'File': file_path}
        df = df.append(new_row, ignore_index=True)
        save_database(df)
        st.success("File uploaded successfully.")

    # Display the uploaded files with options to delete and share
    display_uploaded_files()

else:
    st.markdown("[Return Home Page](https://free-storage.streamlit.app/)")
