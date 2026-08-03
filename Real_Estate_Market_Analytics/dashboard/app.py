import streamlit as st
from auth.login import login_user
from auth.register import register_user

st.set_page_config(
    page_title="Real Estate Analytics Login",
    page_icon="🏠",
    layout="centered"
)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

if st.session_state.logged_in:
    st.success(f"Welcome {st.session_state.username} 🎉")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()

    st.stop()

st.title("🏠 Real Estate Market Analytics")

option = st.radio(
    "Choose Option",
    ["Login", "Register"],
    horizontal=True
)

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if option == "Register":

    if st.button("Create Account"):

        if username == "" or password == "":
            st.warning("Please fill all fields")

        elif register_user(username, password):
            st.success("Registration Successful ✅")

        else:
            st.error("Username already exists")

else:

    if st.button("Login"):

        if login_user(username, password):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.rerun()

        else:
            st.error("Invalid Username or Password")