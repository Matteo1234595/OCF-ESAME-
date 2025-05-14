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

# ⚠️ Per semplicità, ogni sezione ha più domande simulate (da espandere a piacere)
DOMANDE = {
    "Diritto del mercato finanziario": [
        {
            "domanda": "Chi vigila sulla trasparenza delle informazioni finanziarie in Italia?",
            "opzioni": ["Bankitalia", "IVASS", "CONSOB", "Ministero dell'Economia"],
            "corretta": "C",
            "spiegazione": "La CONSOB è responsabile della trasparenza dei mercati finanziari e della tutela degli investitori.",
            "distrattore": "A"
        },
        {
            "domanda": "Cosa sono i prospetti informativi?",
            "opzioni": ["Documenti fiscali", "Comunicazioni bancarie", "Informazioni obbligatorie per gli investitori", "Lettere di incarico"],
            "corretta": "C",
            "spiegazione": "I prospetti informativi sono documenti obbligatori contenenti tutte le informazioni su strumenti finanziari offerti al pubblico.",
            "distrattore": "A"
        }
    ],
    "Diritto previdenziale e assicurativo": [
        {
            "domanda": "Cos'è il TFR?",
            "opzioni": ["Un fondo pensione volontario", "Una tassa sulla rendita", "Una forma di previdenza integrativa", "Il Trattamento di Fine Rapporto"],
            "corretta": "D",
            "spiegazione": "Il TFR è una somma accantonata dal datore di lavoro che spetta al lavoratore alla cessazione del rapporto di lavoro.",
            "distrattore": "A"
        }
    ],
    "Diritto privato e commerciale": [
        {
            "domanda": "Qual è la differenza tra società di persone e di capitali?",
            "opzioni": ["Nessuna", "Responsabilità illimitata vs limitata", "Solo le prime sono fiscalmente soggette", "Le seconde non hanno personalità giuridica"],
            "corretta": "B",
            "spiegazione": "Nelle società di persone i soci rispondono anche con il proprio patrimonio, nelle società di capitali la responsabilità è limitata ai conferimenti.",
            "distrattore": "D"
        }
    ],
    "Diritto tributario": [
        {
            "domanda": "Qual è l'imposta sul reddito delle persone fisiche?",
            "opzioni": ["IVA", "IRAP", "IRPEF", "IMU"],
            "corretta": "C",
            "spiegazione": "L'IRPEF è l'imposta progressiva sui redditi delle persone fisiche, regolata dal TUIR.",
            "distrattore": "B"
        }
    ],
    "Matematica ed economia finanziaria": [
        {
            "domanda": "Cosa rappresenta il TAEG?",
            "opzioni": ["Il tasso fisso", "Il tasso di rendimento netto", "Il Tasso Annuo Effettivo Globale", "Il tasso variabile trimestrale"],
            "corretta": "C",
            "spiegazione": "Il TAEG rappresenta il costo complessivo del finanziamento su base annua, comprensivo di interessi e spese.",
            "distrattore": "D"
        },
        {
            "domanda": "Qual è la formula per calcolare l'interesse semplice?",
            "opzioni": ["I = C × r × t", "I = C / (1 + r)^t", "I = r / t × C", "I = C × r ÷ t"],
            "corretta": "A",
            "spiegazione": "L'interesse semplice si calcola come prodotto tra capitale, tasso e tempo.",
            "distrattore": "D"
        }
    ]
}

# UI Streamlit
st.set_page_config("Quiz OCF - Domande a Rotazione")
st.title("🔁 Generatore OCF - Domande a Rotazione")

area = st.selectbox("Seleziona un'area tematica", list(AREE.keys()))
numero = st.slider("Numero di domande da generare", 1, 5, 1)

if st.button("🎯 Genera Domande"):
    disponibili = DOMANDE.get(area, [])
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

    st.download_button("⬇️ Scarica domande", data=json.dumps(risultati, indent=2), file_name="domande_ocf_random.json")
