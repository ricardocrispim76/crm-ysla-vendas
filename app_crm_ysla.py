# Novo script com tratamento de colunas (strip) para evitar KeyError

codigo_corrigido_v2 = """
import streamlit as st
import pandas as pd

# Carregar base de dados com separador ponto e vírgula
data = pd.read_csv("clientes_crm.csv", sep=";", encoding="utf-8")
data.columns = data.columns.str.strip()  # remove espaços nos nomes de colunas

st.set_page_config(page_title="CRM YSLA Iguatemi", layout="wide")

st.title("📱 CRM de Vendas – YSLA Iguatemi")
st.markdown("Visualize suas clientes e entre em contato com um clique no WhatsApp.")

# Campo de busca por nome
nome_filtro = st.text_input("🔍 Buscar cliente por nome:")

if nome_filtro:
    data = data[data['Cliente'].str.contains(nome_filtro, case=False, na=False)]

# Exibir os dados em formato de cartões
for _, row in data.iterrows():
    st.markdown("---")
    col1, col2 = st.columns([3, 1])

    with col1:
        st.markdown(f"**👤 Cliente:** {row['Cliente']}")
        st.markdown(f"🛍️ **Última Compra:** {row['UltimaCompra']}")
        st.markdown(f"🎽 **Qtde Peças:** {row['QtdePecas']} | 💰 **Valor Total:** R$ {row['ValorTotal']}")

    with col2:
        st.link_button("💬 WhatsApp", row['LinkWhatsApp'], use_container_width=True)

st.markdown("---")
st.caption("Desenvolvido por RCS Consultoria | Powered by Streamlit")
"""

# Salvar nova versão com correção robusta
file_path_v2 = "/mnt/data/app_crm_ysla_corrigido_v2.py"
with open(file_path_v2, "w", encoding="utf-8") as f:
    f.write(codigo_corrigido_v2)

file_path_v2
