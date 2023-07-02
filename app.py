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
    try:
        with open(FileName, "w") as Save:
            json.dump(UserAccount, Save)
        
        st.success(f"{FileName} created successfully")
    except FileNotFoundError:
        st.error(f"Error: {FileName} not found")

def email_exists(email):
    # Check if the email file already exists
    FileName = f"{email}.json"
    return os.path.exists(FileName)

login, signup, DeleteAccount = st.tabs(["Login", "Sign Up", "Delete Account ."])

with login:
    Co1, Co2 = st.columns([5, 7])
    with Co2:
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
    password = st.text_input('Enter your Password:',type="password")
    
    if st.button('Login'):
        filename = f"{email}.json"
        try:
            with open(filename, "r") as user :
                account = json.load(user)
            if password == account['Password']:
                url = f'https://backup-free.streamlit.app/?uniqID={account["uniqID"]}'
                webbrowser.open_new_tab(url)
            
            
            else:
                st.error("Password Invalid")
            
        except FileNotFoundError :
            st.error("Go to signup")
            

with signup:
    Cs1, Cs2 = st.columns([4, 6])
    with Cs2:
        st.title('Sign Up')
    col1, col2 = st.columns(2)
    with col1:
        Name = st.text_input("Enter your name:")
    with col2:
        LastName = st.text_input("Enter your last name:")
    Email = st.text_input('Enter your Email:')
    col3, col4 = st.columns(2)
    
    with col3:
        Password = st.text_input('Enter Password:')
        if Password == '':
            pass
        elif len(Password) < 8:
            short = "Password is too short (minimum 8 characters)"
            st.error(short)
    with col4:
        confirm = st.text_input('Confirm Password:')
        if confirm == '':
            pass
        elif Password != confirm:
            incorrect = "Passwords do not match"
            st.error(incorrect)
    
    correct = Passw(Password, confirm)
    if correct:
        if st.button("Signup"):
            Signup(Name, LastName, Email, correct)
with DeleteAccount :
  DeleteEmail = st.text_input("Email :")
  DeletePassword =  st.text_input('your Password:',type="password")
  if DeleteEmail == '' or DeletePassword == '': pass
  elif DeleteEmail != '' and DeletePassword != '':
    AccountFileName = f'{DeleteEmail}.json'
    if os.path.exists(AccountFileName):
      
    # Delete the file
      os.remove(DeleteEmail)
      st.success(f"{AccountFileName} has been deleted.")
  else:
      st.error(f"{AccountFileName} does not exist.")
