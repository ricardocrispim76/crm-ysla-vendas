
import streamlit as st
import pandas as pd

# Carregar base de dados
data = pd.read_csv("clientes_crm.csv", sep=";", encoding="utf-8")
data.columns = data.columns.str.strip()

st.set_page_config(page_title="CRM YSLA Iguatemi", layout="wide")

st.title("📱 CRM de Vendas – YSLA Iguatemi")
st.markdown("Visualize suas clientes e entre em contato com um clique no WhatsApp.")

# Campo de busca por nome
nome_filtro = st.text_input("🔍 Buscar cliente por nome:")

if nome_filtro:
    data = data[data['CLIENTE_VAREJO'].str.contains(nome_filtro, case=False, na=False)]

# Exibir os dados em formato de cartões
for _, row in data.iterrows():
    st.markdown("---")
    col1, col2 = st.columns([3, 1])

    with col1:
        st.markdown(f"**👤 Cliente:** {row['CLIENTE_VAREJO']}")
        st.markdown(f"🛍️ **Última Compra:** {row['ULT_COMPRA']}")
        st.markdown(f"🎽 **Qtde Peças:** {row['QTDE_PECAS']} | 💰 **Valor Total:** R$ {row['VALOR']}")

    with col2:
        st.link_button("💬 WhatsApp", f"https://wa.me/55{row['TELEFONE']}?text=Olá%20{row['CLIENTE_VAREJO']}%2C%20tudo%20bem%3F%20😊%0AAqui%20é%20da%20YSLA%20Iguatemi!%0AEstamos%20com%20novidades%20lindas%20na%20loja%20e%20achamos%20que%20você%20vai%20amar.%0ASe%20quiser%2C%20posso%20te%20mostrar%20rapidinho%20por%20aqui%20mesmo%20💬✨", use_container_width=True)

st.markdown("---")
st.caption("Desenvolvido por RCS Consultoria | Powered by Streamlit")
