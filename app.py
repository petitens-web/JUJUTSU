import streamlit as st
import streamlit.components.v1 as components

# Wide layout to support the 3D particle field
st.set_page_config(layout="wide")

# This CSS hides the Streamlit interface for a clean, immersive look
st.markdown("""
    <style>
        header, footer, #MainMenu {visibility: hidden;}
        .block-container {padding: 0rem;}
    </style>
""", unsafe_allow_html=True)

# Loads the visualizer code
try:
    with open("app.html", "r", encoding='utf-8') as f:
        visualizer_code = f.read()
    
    # Display the visualizer (Set to 800px height for the 3D field)
    components.html(visualizer_code, height=800, scrolling=False)
except FileNotFoundError:
    st.error("Please ensure your HTML file is named app.html in GitHub.")
