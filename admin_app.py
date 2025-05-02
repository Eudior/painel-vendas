import streamlit as st
import json
import os

# Nome do arquivo JSON com os dados das vendas
ARQUIVO = "dados_vendas.json"

# Função para carregar os dados
def carregar_dados():
    if not os.path.exists(ARQUIVO):
        return {"vendedores": {}}
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)

# Função para salvar os dados
def salvar_dados(dados):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)

# Carrega dados existentes
dados = carregar_dados()

st.title("Painel Administrativo de Vendas")

vendedor = st.text_input("Nome do vendedor").strip().lower()

if vendedor:
    if vendedor not in dados["vendedores"]:
        dados["vendedores"][vendedor] = {
            "mensal": {"meta": 0, "vendas": 0},
            "semanas": [{"meta": 0, "vendas": 0} for _ in range(4)]
        }

    st.subheader("Meta Mensal")
    meta_mensal = st.number_input("Meta mensal", min_value=0.0, key="meta_mensal")
    vendas_mensal = st.number_input("Vendas mensais", min_value=0.0, key="vendas_mensal")

    dados["vendedores"][vendedor]["mensal"] = {
        "meta": meta_mensal, "vendas": vendas_mensal
    }

    for i in range(4):
        st.subheader(f"Semana {i+1}")
        meta = st.number_input(f"Meta semana {i+1}", min_value=0.0, key=f"meta{i}")
        vendas = st.number_input(f"Vendas semana {i+1}", min_value=0.0, key=f"vendas{i}")
        dados["vendedores"][vendedor]["semanas"][i] = {
            "meta": meta, "vendas": vendas
        }

    if st.button("Salvar dados"):
        salvar_dados(dados)
        st.success("Dados salvos com sucesso!")
