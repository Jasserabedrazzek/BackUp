import streamlit as st
import random as Ran
import json
import re
import os
import webbrowser

st.set_page_config(page_title='Welcome to Back Up',
                   page_icon='',
                   layout='centered',
                   initial_sidebar_state='auto')

def EmailValidate(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def Passw(password, confirm):
    if len(password) >= 8 and password == confirm:
        correct = password
        return correct

def Signup(nom, prenom, email, password):
    # Check if the email already exists
    if email_exists(email):
        st.error("Email already exists")
        return
    
    # Validate email format
    if not EmailValidate(email):
        st.error("Invalid email format")
        return
    
    # Validate password length and match with confirm password
    if len(password) < 8:
        st.error("Password is too short (minimum 8 characters)")
        return
    elif password != confirm:
        st.error("Passwords do not match")
        return
    
    uniqId = Ran.randint(100000000000, 999999999999)
    
    UserAccount = {
        "nom": nom,
        "prenom": prenom,
        "Email": email,
        "Password": password,
        "uniqID": str(uniqId),
    }
    
    FileName = f"{email}.json"
    FileNameUniqId = f"{str(uniqId)}.json"
    try:
        with open(FileName, "w") as Save:
            json.dump(UserAccount, Save)
        with open(FileNameUniqId, "w") as UserId:
            json.dump(UserAccount, UserId)
        st.success(f"{FileName} created successfully")
    except FileNotFoundError:
        st.error(f"Error: {FileName} not found")

def email_exists(email):
    # Check if the email file already exists
    FileName = f"{email}.json"
    return os.path.exists(FileName)

# Initialize login and signup tabs
login, signup = st.tabs(["Login", "Sign Up"])

with login:
    st.title("Login")
    st.write("---")
    email = st.text_input('Enter Your Email:')
    if email == "":
        pass
    elif EmailValidate(email) is False:
        st.error('Invalid email format')
    elif EmailValidate(email) is False and email == '':
        pass
    elif EmailValidate(email) is True:
        EmailValid = email
    password = st.text_input('Enter your Password:')
    
    login_button = st.button('Login')
    if login_button:
        filename = f"{email}.json"
        try:
            with open(filename, "r") as user:
                account = json.load(user)
            if password == account['Password']:
                url = f'https://free-storage.streamlit.app/?uniqID={account["uniqID"]}'  # Change the URL here
                st.markdown(f"[Login]({url})")
        except FileNotFoundError:
            st.error("Go to signup")

    # Hide the tabs after clicking the Login button
    if login_button and 'account' in locals() and 'url' in locals():
        st.empty()

with signup:
    st.title('Sign Up')
    Name = st.text_input("Enter your name:")
    LastName = st.text_input("Enter your last name:")
    Email = st.text_input('Enter your Email:')
    Password = st.text_input('Enter Password:')
    if Password != '':
        if len(Password) < 8:
            st.error("Password is too short (minimum 8 characters)")
    confirm = st.text_input('Confirm Password:')
    if confirm != '':
        if Password != confirm:
            st.error("Passwords do not match")
    
    correct = Passw(Password, confirm)
    if correct:
        signup_button = st.button("Signup")
        if signup_button:
            Signup(Name, LastName, Email, correct)
