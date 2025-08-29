# main.py
import streamlit as st
from datetime import datetime


def main():
    # Page config
    st.set_page_config(page_title="Hello World App", page_icon="🌍", layout="centered")

    # Header with style
    st.markdown(
        """
        <h1 style='text-align: center; color: #4CAF50;'>
            🌍 Hello, World! 👋
        </h1>
        <p style='text-align: center; font-size:18px;'>
            Welcome to your first <b>Streamlit</b> app with a modern design.
        </p>
        """,
        unsafe_allow_html=True
    )

    # Input section
    st.subheader("💬 Say Hello Back!")
    name = st.text_input("Enter your name", placeholder="Type here...")
    
    if st.button("Greet Me 🎉"):
        if name.strip() != "":
            st.success(f"Hello, {name}! Glad to see you here 😃")
        else:
            st.warning("Please enter your name first!")

    # Footer with current time
    st.markdown("---")
    st.markdown(
        f"<p style='text-align:center; font-size:14px;'>🕒 Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
