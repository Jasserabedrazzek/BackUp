import streamlit as st
import sqlite3

# Create a SQLite database connection
conn = sqlite3.connect('file_database.db')
c = conn.cursor()

# Create a table to store uploaded files if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS files
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              file_name TEXT,
              file_type TEXT,
              file_path TEXT)''')

# Get the uniqID from the URL parameters
uniqID = st.experimental_get_query_params().get("uniqID", [None])[0]
if uniqID and len(str(uniqID)) == 12:
    ID = uniqID
    st.set_page_config(page_title=f'Welcome {ID}',
                       page_icon='',
                       layout='centered',
                       initial_sidebar_state='auto')
    UploadFile = st.file_uploader("Choose a file")
    Audio, Video, Images, Doc, etc = st.columns(5)
    
    # Define the file types for each tab
    file_types = {"Audio": ["mp3", "wav"],
                  "Video": ["mp4", "mov"],
                  "Images": ["jpg", "jpeg", "png"],
                  "Doc": ["pdf", "docx", "txt"],
                  "etc": []}  # Add any other file types to this list
    
    # Process the uploaded file
    if UploadFile is not None:
        file_name = UploadFile.name
        file_type = file_name.split('.')[-1]
        file_path = f"uploads/{file_name}"
        
        # Save the file to the uploads folder
        with open(file_path, "wb") as f:
            f.write(UploadFile.getbuffer())
        
        # Store file details in the database
        c.execute("INSERT INTO files (file_name, file_type, file_path) VALUES (?, ?, ?)",
                  (file_name, file_type, file_path))
        conn.commit()
        
        # Categorize the file based on its type
        for tab_name, supported_types in file_types.items():
            if file_type.lower() in supported_types:
                tab = eval(tab_name.lower().capitalize())
                tab.file(file_name)
    
    # Show the uploaded files in a table
    st.subheader("Uploaded Files")
    files = c.execute("SELECT file_name, file_type, file_path FROM files").fetchall()
    for file_name, file_type, file_path in files:
        st.write(file_name, file_type, file_path)
        
        # Add buttons for deleting or sharing the file
        col1, col2 = st.columns(2)
        if col1.button("Delete"):
            # Perform deletion logic here
            c.execute("DELETE FROM files WHERE file_path=?", (file_path,))
            conn.commit()
            st.write("File deleted!")
        if col2.button("Share"):
            # Perform sharing logic here
            st.write("File shared!")
    
    # Close the database connection
    conn.close()
else:
    st.markdown("[Return Home Page](https://free-storage.streamlit.app/)")
