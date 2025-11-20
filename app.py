import streamlit as st
import os

from main import run_script
from debugger_agent import call_groq_api
from json_utils import parse_llm_json
from patch_utils import apply_line_patch

st.set_page_config(page_title="Smart Debugger", layout="wide")

st.title("🛠️ Smart Debugger — Interface Streamlit")

# Initialisation des états persistants
if "source_code" not in st.session_state:
    st.session_state.source_code = None

if "parsed_json" not in st.session_state:
    st.session_state.parsed_json = None

if "script_path" not in st.session_state:
    st.session_state.script_path = None


# --- Sélection du fichier ---
st.subheader("Sélectionner un fichier Python")

python_files = [f for f in os.listdir(".") if f.endswith(".py")]

script = st.selectbox("Choisissez un fichier :", python_files)


# --- ANALYSER LE SCRIPT ---
if st.button("Analyser le script"):
    st.session_state.script_path = script

    # Lire code source
    with open(script, "r", encoding="utf-8") as f:
        st.session_state.source_code = f.read()

    # Exécuter le script
    stdout, stderr, code = run_script(script)

    st.subheader("📄 Code source")
    st.code(st.session_state.source_code, language="python")

    st.subheader("🖨️ Sortie du script (stdout)")
    st.text(stdout)

    st.subheader("❌ Erreur détectée")
    st.text(stderr)

    # Si erreur → envoyer au LLM
    if code != 0:
        parsed = parse_llm_json(call_groq_api(st.session_state.source_code, stderr))
        st.session_state.parsed_json = parsed

        # --- AFFICHAGE RÉSUMÉ ET MINIMAL ---
        line_number = parsed.get("line_number")
        fixed_line = parsed.get("fixed_line")

        st.success(f"🔧 Correction détectée :")
        st.write(f"**Ligne à corriger :** `{line_number}`")
        st.write(f"**Nouvelle ligne proposée :** `{fixed_line}`")


# --- AFFICHAGE APRÈS ANALYSE ---
if st.session_state.parsed_json:
    parsed = st.session_state.parsed_json
    line_number = parsed.get("line_number")
    fixed_line = parsed.get("fixed_line")

    # BOUTON DE CORRECTION
    if st.button("Appliquer la correction automatiquement 🔧"):
        apply_line_patch(st.session_state.script_path, line_number, fixed_line)
        st.success("✔ Correction appliquée avec succès !")

        # Réafficher le code après correction
        with open(st.session_state.script_path, "r", encoding="utf-8") as f:
            corrected = f.read()

        st.subheader("📄 Code après correction")
        st.code(corrected, language="python")
