import streamlit as st
import base64
import os
from pathlib import Path

# Fonction pour convertir une image en texte (Base64)
def get_base64_image(image_path):
    try:
        img_bytes = Path(image_path).read_bytes()
        # On détermine l'extension pour le type MIME (png, jpg, etc.)
        ext = Path(image_path).suffix.replace(".", "")
        if ext == "jpg": ext = "jpeg"
        return f"data:image/{ext};base64,{base64.b64encode(img_bytes).decode()}"
    except Exception as e:
        return None

def load_site():
    html = Path("index.html").read_text(encoding="utf-8")
    css = Path("style.css").read_text(encoding="utf-8")
    
    # Chemin vers ton dossier d'images
    assets_dir = Path("Assets/images")
    
    # On parcourt chaque fichier dans le dossier Assets/images
    if assets_dir.exists():
        for img_file in assets_dir.iterdir():
            if img_file.is_file():
                # On crée le chemin tel qu'il est écrit dans ton HTML
                # Exemple : "Assets/images/html_logo.png"
                relative_path = f"Assets/images/{img_file.name}"
                
                # On génère la version Base64
                base64_data = get_base64_image(img_file)
                
                if base64_data:
                    # On remplace TOUTES les occurrences de ce chemin dans le HTML
                    html = html.replace(relative_path, base64_data)
    
    # Injection du CSS
    return f"<style>{css}</style>{html}"

# Configuration Streamlit
st.set_page_config(page_title="EliasDev SaaS", layout="wide")

# Affichage avec une hauteur suffisante
st.components.v1.html(load_site(), height=2000, scrolling=True)