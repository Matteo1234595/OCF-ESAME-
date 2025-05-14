# app.py — Generatore AI Quiz OCF con Streamlit (OpenAI API v1 compatibile)
# Requisiti: streamlit, openai, json

import streamlit as st
import json
from openai import OpenAI

# 👉 Inserisci la tua API Key OpenAI
client = OpenAI(api_key="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")

# 📚 Aree tematiche
AREE = {
    "Diritto del mercato finanziario": 2002,
    "Diritto previdenziale e assicurativo": 500,
    "Diritto privato e commerciale": 400,
    "Diritto tributario": 500,
    "Matematica ed economia finanziaria": 1600
}

# 🎯 Prompt base
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

# 💬 Funzione di generazione con OpenAI API v1
def genera_domanda(area):
    prompt = PROMPT_TEMPLATE.format(area=area)
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    content = response.choices[0].message.content.strip()
    try:
        return json.loads(content)
    except:
        return {"errore": "Impossibile interpretare la risposta come JSON.", "raw": content}

# 🧠 Interfaccia Streamlit
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
            for j, opzione in enumerate(risultato["opzioni"], start=1):
                st.write(f"{chr(64+j)}. {opzione}")
            st.success(f"✅ Risposta corretta: {risultato['corretta']}")
            st.info(f"📘 Spiegazione: {risultato['spiegazione']}")
            st.warning(f"🎯 Distrattore plausibile: {risultato['distrattore']}")
            risultati.append(risultato)

        # Esportazione
        st.download_button(
            label="⬇️ Scarica domande in JSON",
            data=json.dumps(risultati, indent=2, ensure_ascii=False),
            file_name="domande_ocf.json",
            mime="application/json"
        )

st.markdown("""---
🌐 *Creato con ❤️ da un sistema AI. Progetto per simulazioni d'esame OCF.*
""")
