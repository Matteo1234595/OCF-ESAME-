import streamlit as st
import random
from domande_data import DOMANDE_COMPLETE

st.set_page_config("Simulatore Quiz OCF", layout="centered")
st.title("📘 Simulatore Completo per l'Esame OCF")

AREE = list(DOMANDE_COMPLETE.keys())

# Selezione area tematica
area = st.selectbox("📚 Scegli un'area tematica:", AREE)

# Numero massimo di domande disponibili per l'area
max_domande = len(DOMANDE_COMPLETE[area])

# Slider per scegliere quante domande mostrare
numero_domande = st.slider("📌 Quante domande vuoi visualizzare?", 1, max_domande, 10)

# Inizializza sessione per rotazione casuale
if "rotazione_domande" not in st.session_state:
    st.session_state["rotazione_domande"] = {}

# Clic per generare nuove domande
if st.button("🎯 Mostra nuove domande"):
    # Mescola l'elenco e salva la selezione attuale
    domande_area = DOMANDE_COMPLETE[area]
    scelte = random.sample(domande_area, k=min(numero_domande, len(domande_area)))
    st.session_state["rotazione_domande"][area] = scelte

# Mostra le domande salvate in sessione
if area in st.session_state["rotazione_domande"]:
    domande_visualizzate = st.session_state["rotazione_domande"][area]
    for i, domanda in enumerate(domande_visualizzate, start=1):
        st.markdown(f"### Domanda {i}")
        st.write(domanda["domanda"])
        for j, opzione in enumerate(domanda["opzioni"]):
            st.write(f"{chr(65 + j)}. {opzione}")
        st.success(f"✅ Risposta corretta: {domanda['corretta']}")
        st.info(f"📘 Spiegazione: {domanda['spiegazione']}")
        st.warning(f"🎯 Distrattore: {domanda['distrattore']}")
        st.markdown("---")
