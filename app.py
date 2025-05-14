import streamlit as st
import json
import os
from openai import OpenAI

# ✅ Inizializza il client OpenAI leggendo la chiave dai secrets
client = OpenAI(api_key=os.getenv("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"))

# ✅ Mappa delle aree OCF
AREE = {
    "Diritto del mercato finanziario": 2002,
    "Diritto previdenziale e assicurativo": 500,
    "Diritto privato e commerciale": 400,
    "Diritto tributario": 500,
    "Matematica ed economia finanziaria": 1600
}

# ✅ Prompt per GPT
PROMPT = """
Genera una domanda a scelta multipla in stile esame OCF sull'argomento: {area}.
Includi:
- Una domanda
- 4 opzioni (A, B, C, D)
- La risposta corretta
- Una spiegazione dettagliata
- Il distrattore più plausibile

Rispondi in JSON con queste chiavi:
"domanda", "opzioni", "corretta", "spiegazione", "distrattore"
"""

# ✅ Funzione che genera una domanda usando GPT
def genera_domanda(area):
    prompt = PROMPT.format(area=area)
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        content = response.choices[0].message.content.strip()
        return json.loads(content)
    except Exception as e:
        return {"errore": str(e)}

# ✅ UI Streamlit
st.set_page_config("Generatore Quiz OCF")
st.title("🧠 Generatore Intelligente di Domande OCF")

area_selezionata = st.selectbox("Seleziona un'area tematica", list(AREE.keys()))
numero = st.slider("Numero di domande da generare:", 1, 10, 1)

if st.button("🎯 Genera Domande"):
    for i in range(numero):
        st.markdown(f"### Domanda {i+1}")
        risultato = genera_domanda(area_selezionata)

        if "errore" in risultato:
            st.error(f"❌ Errore: {risultato['errore']}")
            continue

        st.write(risultato["domanda"])
        for idx, opzione in enumerate(risultato["opzioni"]):
            st.write(f"{chr(65 + idx)}. {opzione}")
        st.success(f"✅ Risposta corretta: {risultato['corretta']}")
        st.info(f"📘 Spiegazione: {risultato['spiegazione']}")
        st.warning(f"🎯 Distrattore: {risultato['distrattore']}")
