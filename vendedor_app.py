import streamlit as st
import json
import os

ARQUIVO = "dados_vendas.json"

# Função para carregar os dados
def carregar_dados():
    if not os.path.exists(ARQUIVO):
        return {"vendedores": {}}
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)

dados = carregar_dados()

st.title("Painel de Metas do Vendedor")

nomes_vendedores = list(dados["vendedores"].keys())

if not nomes_vendedores:
    st.warning("Nenhum vendedor cadastrado ainda.")
else:
    vendedor = st.selectbox("Selecione seu nome", nomes_vendedores)

    info = dados["vendedores"][vendedor]

    st.subheader("Meta Mensal")
    meta = info["mensal"]["meta"]
    vendas = info["mensal"]["vendas"]
    progresso = min(vendas / meta, 1.0) if meta > 0 else 0
    st.progress(progresso)
    st.text(f"{vendas:.2f} / {meta:.2f} ({progresso * 100:.1f}%)")

    for i, semana in enumerate(info["semanas"], 1):
        st.subheader(f"Semana {i}")
        meta_s = semana["meta"]
        vendas_s = semana["vendas"]
        progresso_s = min(vendas_s / meta_s, 1.0) if meta_s > 0 else 0
        st.progress(progresso_s)
        st.text(f"{vendas_s:.2f} / {meta_s:.2f} ({progresso_s * 100:.1f}%)")
