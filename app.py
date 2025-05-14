import streamlit as st
import random
import json

AREE = {
    "Diritto del mercato finanziario": 2002,
    "Diritto previdenziale e assicurativo": 500,
    "Diritto privato e commerciale": 400,
    "Diritto tributario": 500,
    "Matematica ed economia finanziaria": 1600
}

DOMANDE_SIMULATE = {
    "Diritto del mercato finanziario": [
        {
            "domanda": "Qual è la funzione principale della CONSOB?",
            "opzioni": [
                "Controllare le banche",
                "Vigilare sui mercati finanziari",
                "Gestire la politica monetaria",
                "Approvare i bilanci delle società"
            ],
            "corretta": "B",
            "spiegazione": "La CONSOB vigila sui mercati finanziari per garantirne la trasparenza e il corretto funzionamento.",
            "distrattore": "A"
        }
    ],
    "Matematica ed economia finanziaria": [
        {
            "domanda": "Qual è la formula dell'interesse semplice?",
            "opzioni": [
                "I = C × r × t",
                "I = C × (1 + r)^t",
                "I = r / C × t",
                "I = C × t / r"
            ],
            "corretta": "A",
            "spiegazione": "La formula dell'interesse semplice è I = Capitale × tasso × tempo.",
            "distrattore": "D"
        }
    ]
}

def genera_domanda_simulata(area):
    return random.choice(DOMANDE_SIMULATE.get(area, [{
        "domanda": "Domanda fittizia",
        "opzioni": ["Opzione A", "Opzione B", "Opzione C", "Opzione D"],
        "corretta": "A",
        "spiegazione": "Questa è una simulazione.",
        "distrattore": "B"
    }]))

st.set_page_config("Generatore Quiz OCF (Demo)")
st.title("🧠 Generatore Demo di Domande OCF (Offline)")

area_selezionata = st.selectbox("Seleziona un'area tematica", list(AREE.keys()))
numero = st.slider("Numero di domande da generare:", 1, 5, 1)

if st.button("🎯 Genera Domande"):
    risultati = []
    for i in range(numero):
        st.markdown(f"### Domanda {i+1}")
        risultato = genera_domanda_simulata(area_selezionata)
        st.write(risultato["domanda"])
        for idx, opzione in enumerate(risultato["opzioni"]):
            st.write(f"{chr(65 + idx)}. {opzione}")
        st.success(f"✅ Risposta corretta: {risultato['corretta']}")
        st.info(f"📘 Spiegazione: {risultato['spiegazione']}")
        st.warning(f"🎯 Distrattore: {risultato['distrattore']}")
        risultati.append(risultato)

    st.download_button("⬇️ Scarica domande", data=json.dumps(risultati, indent=2), file_name="domande_ocf_demo.json")
