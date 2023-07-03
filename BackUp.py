import streamlit as st
import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('file_storage.db')
c = conn.cursor()

# Create a table to store file information
c.execute('''CREATE TABLE IF NOT EXISTS files (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                filename TEXT,
                filedata BLOB
            )''')

# Get the uniqID from the URL parameters
uniqID = st.experimental_get_query_params().get("uniqID", [None])[0]

if uniqID and len(str(uniqID)) == 12:
    ID = uniqID
    st.set_page_config(page_title=f'Welcome {ID}',
                       page_icon='',
                       layout='centered',
                       initial_sidebar_state='auto')
    upload_file = st.file_uploader("Choose a file")
    if upload_file is not None:
        # Read the uploaded file data
        file_data = upload_file.read()

        # Insert the file data into the database
        c.execute("INSERT INTO files (filename, filedata) VALUES (?, ?)",
                  (upload_file.name, file_data))
        conn.commit()

    # Display the uploaded files
    st.header("Uploaded Files")
    files = c.execute("SELECT id, filename FROM files")
    for file in files:
        file_id, filename = file
        st.write(f"ID: {file_id}, Filename: {filename}")

        # Add a delete button for each file
        if st.button("Delete", key=f"delete_{file_id}"):
            c.execute("DELETE FROM files WHERE id=?", (file_id,))
            conn.commit()
            st.write("File deleted.")

        # Add a share button for each file
        if st.button("Share", key=f"share_{file_id}"):
            # Implement the sharing functionality here
            st.write("Sharing file...")

else:
    st.markdown("[Return Home Page](https://free-storage.streamlit.app/)")

# Close the database connection
conn.close()
