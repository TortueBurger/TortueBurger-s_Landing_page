import streamlit as st
import base64
from pathlib import Path

def get_base64_image(image_path):
    # Convertit une image locale en chaîne base64
    img_bytes = Path(image_path).read_bytes()
    return base64.b64encode(img_bytes).decode()

def load_site():
    html = Path("index.html").read_text(encoding="utf-8")
    css = Path("style.css").read_text(encoding="utf-8")
    
    # On remplace les chemins locaux par les données Base64
    # Exemple pour l'image de profil
    img_profile = get_base64_image("Assets/images/Elias.jpg")
    html = html.replace("Assets/images/Elias.jpg", f"data:image/jpeg;base64,{img_profile}")
    
    # Tu peux faire de même pour tes icônes si besoin
    # ou utiliser des liens URLs pour les logos technos (plus simple)

    return f"<style>{css}</style>{html}"

st.set_page_config(page_title="EliasDev SaaS", layout="wide")
st.components.v1.html(load_site(), height=1500, scrolling=True)