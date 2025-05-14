# app.py — Generatore AI Quiz OCF con Streamlit
# Requisiti: streamlit, openai, json

import streamlit as st
import openai
import json

# 👉 Inserisci qui la tua API Key di OpenAI
openai.api_key = "INSERISCI_LA_TUA_API_KEY"

# 📚 Aree tematiche
AREE = {
    "Diritto del mercato finanziario": 2002,
    "Diritto previdenziale e assicurativo": 500,
    "Diritto privato e commerciale": 400,
    "Diritto tributario": 500,
    "Matematica ed economia finanziaria": 1600
}

# 🎯 Prompt di base per la generazione delle domande
PROMPT_TEMPLATE = """
Genera una domanda a scelta multipla in stile esame OCF sull'argomento: {area}.
La domanda deve contenere:
- Una domanda chiara e professionale
- 4 opzioni (A, B, C, D)
- La risposta corretta indicata chiaramente
- Una spiegazione dettagliata della risposta corretta
- L'identificazione del distrattore (opzione sbagliata ma plausibile)

Rispondi in formato JSON con queste chiavi:
"domanda", "opzioni", "corretta", "spiegazione", "distrattore"
"""

# 💬 Funzione per inviare il prompt a OpenAI

def genera_domanda(area):
    prompt = PROMPT_TEMPLATE.format(area=area)
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    content = response.choices[0].message.content.strip()
    try:
        json_data = json.loads(content)
    except:
        json_data = {"errore": "Impossibile interpretare la risposta come JSON.", "raw": content}
    return json_data

# 🧠 Streamlit UI
st.set_page_config(page_title="Generatore Quiz OCF", layout="wide")
st.title("🧠 Generatore Intelligente di Domande OCF")

area_selezionata = st.selectbox("Seleziona un'area tematica:", list(AREE.keys()))
num_domande = st.slider("Numero di domande da generare:", 1, 20, 5)

if st.button("🎯 Genera Domande"):
    with st.spinner("Generazione in corso..."):
        risultati = []
        for i in range(num_domande):
            st.markdown(f"**Domanda {i+1}:**")
            risultato = genera_domanda(area_selezionata)
            if "errore" in risultato:
                st.error("❌ Errore nella generazione della domanda.")
                st.text(risultato.get("raw", "Nessun contenuto"))
                continue
            st.write(risultato["domanda"])
            for i, opzione in enumerate(risultato["opzioni"], start=1):
                st.write(f"{chr(64+i)}. {opzione}")
            st.success(f"✅ Risposta corretta: {risultato['corretta']}")
            st.info(f"📘 Spiegazione: {risultato['spiegazione']}")
            st.warning(f"🎯 Distrattore plausibile: {risultato['distrattore']}")
            risultati.append(risultato)

        # Esportazione opzionale
        st.download_button(
            label="⬇️ Scarica domande in JSON",
            data=json.dumps(risultati, indent=2, ensure_ascii=False),
            file_name="domande_ocf.json",
            mime="application/json"
        )

st.markdown("""
---
🌐 *Creato con ❤️ da un sistema AI. Progetto per simulazioni d'esame OCF.*
""")
