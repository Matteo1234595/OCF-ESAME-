import streamlit as st
import random
import json
from domande_data import DOMANDE_COMPLETE

AREE = {
    "Diritto del mercato finanziario": 2002,
    "Diritto previdenziale e assicurativo": 500,
    "Diritto privato e commerciale": 400,
    "Diritto tributario": 500,
    "Matematica ed economia finanziaria": 1600
}

st.set_page_config("Simulatore Quiz OCF", layout="centered")
st.title("🧠 Simulatore Completo Quiz OCF")

area = st.selectbox("📚 Seleziona un'area tematica", list(AREE.keys()))
numero = st.slider("📌 Quante domande vuoi generare?", 1, 20, 5)

if st.button("🎯 Genera Domande"):
    disponibili = DOMANDE_COMPLETE.get(area, [])
    domande_scelte = random.sample(disponibili, min(numero, len(disponibili)))

    risultati = []
    for i, domanda in enumerate(domande_scelte, start=1):
        st.markdown(f"### Domanda {i}")
        st.write(domanda["domanda"])
        for j, opzione in enumerate(domanda["opzioni"]):
            st.write(f"{chr(65 + j)}. {opzione}")
        st.success(f"✅ Risposta corretta: {domanda['corretta']}")
        st.info(f"📘 Spiegazione: {domanda['spiegazione']}")
        st.warning(f"🎯 Distrattore: {domanda['distrattore']}")
        risultati.append(domanda)

    st.download_button("⬇️ Scarica queste domande", data=json.dumps(risultati, indent=2), file_name="domande_ocf_esercizio.json")
