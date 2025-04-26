# app.py
import streamlit as st
from common import initialize_session, login_sidebar, show_footer

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

initialize_session()

st.write("# Welcome to Streamlit!")

login_sidebar()

show_footer()

st.markdown(
    """
    This website has a lot of redundant code. Can you find it and create a utility file which contains the redundancies?
    """
)

with st.expander("Company Info"):
    st.write(
        """
        Fake Company LLC Inc. is located at 1600 Amphitheatre Parkway Mountain View, CA 94043
        """
    )

with st.expander("Links"):
    st.markdown(
        """
        [Google](https://google.com)

        [Gemini](https://gemini.google.com)

        [Streamlit Docs](https://docs.streamlit.io/)
        """
    )
