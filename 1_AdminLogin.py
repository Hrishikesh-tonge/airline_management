import streamlit as st 
import mysql.connector

st.title("Admin Login")
cnx = mysql.connector.connect(
    user="root",
    password="Titanium@1604",
    host="localhost",
    database="airport"
)
cursor = cnx.cursor()
def login(username,password):
    sql = "select passwd from pass_login where id = %s"
    value = (username,)
    cursor.execute(sql,value)
    passw = cursor.fetchall()
    if passw[0][0] == password:
        return True
    else:
        return False
def LoggedInClicked(username,password):
    if login(username,password):
        st.success("Login Successful")
        st.session_state['loggedIn'] = True
    else:
        st.session_state['loggedIn'] = False
        st.error("Invalid creds")
username = st.text_input(label="Username")
password = st.text_input(label="Password",type='password')
st.button("Login",on_click=LoggedInClicked,args=(username,password))