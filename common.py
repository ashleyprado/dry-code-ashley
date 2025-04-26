# common.py
import streamlit as st

COMPANY_NAME = "Fake Company LLC Inc."
COMPANY_ADDRESS = "1600 Amphitheatre Parkway Mountain View, CA 94043"
COPYRIGHT_NOTICE = "© 2024 Fake Company LLC Inc."

def initialize_session():
    if st.session_state.get("logged_in") is None:
        st.session_state["logged_in"] = False

def login():
    st.session_state.logged_in = True

def logout():
    st.session_state.logged_in = False

def login_sidebar():
    if st.session_state.logged_in:
        st.sidebar.success("Logged in")
        st.sidebar.button("Log out", key="logout", on_click=logout)
    else:
        st.sidebar.warning("Not logged in")
        st.sidebar.button("Log in", key="login", on_click=login)

def show_footer():
    st.sidebar.write(COPYRIGHT_NOTICE)
