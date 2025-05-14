import streamlit as st
import random
import json
from domande_data import DOMANDE_COMPLETE

AREE = list(DOMANDE_COMPLETE.keys())
SESSION_KEY = "domande_mostrate"

st.set_page_config("Simulatore Quiz OCF - Completo", layout="centered")
st.title("📘 Simulatore Esame OCF – Domande a Rotazione Completa")

# Selezione area tematica
area = st.selectbox("📚 Scegli una materia:", AREE)
max_domande = len(DOMANDE_COMPLETE[area])
quante = st.slider("📌 Numero di domande da visualizzare:", 1, min(max_domande, 20), 10)

# Inizializza memoria sessione
if SESSION_KEY not in st.session_state:
    st.session_state[SESSION_KEY] = set()

# Quando clicchi il bottone...
if st.button("🎯 Genera nuove domande"):
    tutte = DOMANDE_COMPLETE[area]
    viste = st.session_state[SESSION_KEY]

    # Filtra quelle già viste
    non_viste = [d for i, d in enumerate(tutte) if i not in viste]
    if len(non_viste) < quante:
        viste.clear()  # reset se finite

    # Prendi un set casuale non ripetuto
    disponibili = [d for i, d in enumerate(tutte) if i not in viste]
    domande_scelte = random.sample(disponibili, min(quante, len(disponibili)))

    # Salva gli indici visti
    for d in domande_scelte:
        idx = tutte.index(d)
        viste.add(idx)

    st.session_state["ultime_domande"] = domande_scelte

# Visualizza
if "ultime_domande" in st.session_state:
    for i, domanda in enumerate(st.session_state["ultime_domande"], start=1):
        st.markdown(f"### Domanda {i}")
        st.write(domanda["domanda"])
        for j, opzione in enumerate(domanda["opzioni"]):
            st.write(f"{chr(65 + j)}. {opzione}")
        st.success(f"✅ Risposta corretta: {domanda['corretta']}")
        st.info(f"📘 Spiegazione dettagliata:

{domanda['spiegazione']}")
        st.warning(f"🎯 Distrattore comune: {domanda['distrattore']}")
        st.markdown("---")
