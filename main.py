import streamlit as st
from dashboard import exibir_dashboard
from previsao import exibir_previsao

# Função para exibir a página
def exibir_pagina():
    # Criando os botões na barra lateral
    pagina_selecionada = st.sidebar.radio(
        "Escolha uma página", 
        ["Dashboard :bar_chart:", "Previsão :chart_with_upwards_trend:"]
    )
    
    # Definir a página inicial como "Dashboard", caso não haja seleção ainda
    if "pagina_selecionada" not in st.session_state:
        st.session_state.pagina_selecionada = "Dashboard"
    
    # Atualizando o estado da página selecionada
    st.session_state.pagina_selecionada = pagina_selecionada
    
    # Exibindo a página correspondente
    if st.session_state.pagina_selecionada == "Dashboard :bar_chart:":
        exibir_dashboard()
    elif st.session_state.pagina_selecionada == "Previsão :chart_with_upwards_trend:":
        exibir_previsao()

    # Exibindo as informações sobre a autora e links (esses dados ficam visíveis em todas as páginas)
    with st.sidebar:
        
        st.markdown("---")  # Adiciona outra linha de separação

        st.subheader("Sobre")
        st.markdown("**Cientista de Dados:** Beatriz Rosa Carneiro Gomes")
        st.markdown("**Turma:** 6DTAT")

        # Adicionando o link do LinkedIn
        st.markdown("**LinkedIn:** [Beatriz Rosa C. Gomes](https://www.linkedin.com/in/beatrizrosacgomes/)")


        st.markdown("---")  # Adiciona uma linha de separação
        st.subheader("Perfil Técnico")
        st.markdown("**GitHub:** [Beatriz Rosa C. Gomes](https://github.com/beatrizrosacgomes)")

        st.markdown("---")  # Adiciona uma linha de separação
        st.subheader("Documentação")
        st.markdown("**Github:** [código fonte](https://github.com/beatrizrosacgomes/tech_challenge_ml_fase4_fiap)")

        

# Exibir o conteúdo da página
exibir_pagina()
