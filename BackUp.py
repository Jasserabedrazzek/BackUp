import streamlit as st
import urllib.parse

url = st.experimental_get_query_params()
parsed_url = urllib.parse.urlparse(url)

# Get the URL without query parameters
url_without_params = parsed_url.scheme + "://" + parsed_url.netloc + parsed_url.path

# Get the query parameters as a dictionary
query_params = urllib.parse.parse_qs(parsed_url.query)

# Access individual parameters
uniqID = query_params.get('uniqID', [None])[0]
email = query_params.get('email', [None])[0]

# Print the extracted values
st.write("URL without parameters:", url_without_params)
st.write("uniqID:", uniqID)
st.write("email:", email)
