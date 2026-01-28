import streamlit as st
from pathlib import Path

# Configuration de l'onglet du navigateur
st.set_page_config(page_title="EliasDev Landing Page", layout="wide")

# Lecture des fichiers
def load_site():
    html_content = Path("index.html").read_text(encoding="utf-8")
    css_content = Path("style.css").read_text(encoding="utf-8")
    
    # Injection du CSS directement dans le HTML pour Streamlit
    full_code = f"<style>{css_content}</style>{html_content}"
    return full_code

# Affichage du site dans Streamlit
st.components.v1.html(load_site(), height=1500, scrolling=True)