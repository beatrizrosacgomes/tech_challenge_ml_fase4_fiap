import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

# Função para carregar os dados do Brent usando yfinance
def obter_dados_brent():
    brent = yf.download('BZ=F', start="2007-01-01", end="2025-02-10")
    brent.reset_index(inplace=True)
    return brent

# Função para exibir o dashboard
def exibir_dashboard():
    # Carregando os dados de Brent
    df_brent = obter_dados_brent()

    # Página de Dashboard no Streamlit
    st.title("Dashboard - Análise da Variação do Petróleo")

    # Filtro de Data
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Data Início", df_brent['Date'].min().date())
    with col2:
        end_date = st.date_input("Data Fim", df_brent['Date'].max().date())

    # Filtrando os dados com base nas datas
    df_filtrado = df_brent[(df_brent['Date'] >= pd.to_datetime(start_date)) & (df_brent['Date'] <= pd.to_datetime(end_date))]

    # Cards de Indicadores Principais
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Máximo Abertura", f"${df_filtrado['Open'].max():.2f}")
    with col2:
        st.metric("Mínimo Abertura", f"${df_filtrado['Open'].min():.2f}")
    with col3:
        st.metric("Máximo Fechamento", f"${df_filtrado['Close'].max():.2f}")
    with col4:
        st.metric("Mínimo Fechamento", f"${df_filtrado['Close'].min():.2f}")

    # Gráfico de Candlestick com Preço de Abertura, Fechamento, Máxima e Mínima
    fig_candlestick = go.Figure()

    fig_candlestick.add_trace(go.Candlestick(
        x=df_filtrado['Date'],
        open=df_filtrado['Open'],
        high=df_filtrado['High'],
        low=df_filtrado['Low'],
        close=df_filtrado['Close'],
        name="Candlestick",
        increasing_line_color='green',
        decreasing_line_color='red'
    ))

    fig_candlestick.update_layout(
        title='Gráfico Candlestick - Preço do Brent',
        xaxis_title='Data',
        yaxis_title='Preço (USD)',
        template='plotly_dark',
        width=1000,  # Largura personalizada (em pixels)
        height=500
    )

    # Exibindo o gráfico de Candlestick
    st.plotly_chart(fig_candlestick)

    # Gráfico de Linhas com Preço de Abertura e Fechamento
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=df_filtrado['Date'], y=df_filtrado['Open'], mode='lines', name='Abertura', line=dict(color='#4f81bd')))
    fig.add_trace(go.Scatter(x=df_filtrado['Date'], y=df_filtrado['Close'], mode='lines', name='Fechamento', line=dict(color='#6baed6')))

    fig.update_layout(
        title='Preço do Brent (Abertura e Fechamento)',
        xaxis_title='Data',
        yaxis_title='Preço (USD)',
        template='plotly_dark'
    )

    # Exibindo o gráfico de linhas
    st.plotly_chart(fig)

    # Gráfico de Volume por Ano
    df_filtrado['Ano'] = df_filtrado['Date'].dt.year
    volume_por_ano = df_filtrado.groupby('Ano')['Volume'].sum().reset_index()

    fig_volume = go.Figure()

    fig_volume.add_trace(go.Bar(
        x=volume_por_ano['Ano'],
        y=volume_por_ano['Volume'],
        name='Volume Anual',
        marker=dict(color='#b3cde0', opacity=0.7)
    ))

    fig_volume.update_layout(
        title="Volume de Negócios do Brent por Ano",
        xaxis_title="Ano",
        yaxis_title="Volume",
        template="plotly_dark"
    )

    # Exibindo o gráfico de volume por ano
    st.plotly_chart(fig_volume)

    # Lista de eventos adicionais
    eventos = [
        {"data": "2008-09-15", "evento": "Colapso do Lehman Brothers e início da crise financeira global"},
        {"data": "2009-06-11", "evento": "Declaração oficial da pandemia de Gripe Suína (H1N1)"},
        {"data": "2011-08-05", "evento": "Rebaixamento da nota de crédito dos EUA pela S&P"},
        {"data": "2011-12-17", "evento": "Início da Primavera Árabe"},
        {"data": "2013-10-01", "evento": "Fechamento do governo dos EUA devido à crise do orçamento"},
        {"data": "2014-02-20", "evento": "Anexação da Crimeia pela Rússia"},
        {"data": "2014-06-01", "evento": "Início da Guerra no Oriente Médio"},
        {"data": "2015-03-26", "evento": "Intervenção da Arábia Saudita na Guerra do Iêmen"},
        {"data": "2016-06-23", "evento": "Brexit"},
        {"data": "2016-11-30", "evento": "Acordo da OPEP+ para cortes na produção de petróleo"},
        {"data": "2018-07-06", "evento": "Início da Guerra Comercial EUA-China"},
        {"data": "2019-09-14", "evento": "Ataque às refinarias da Arábia Saudita (Aramco), impactando o fornecimento de petróleo"},
        {"data": "2020-03-01", "evento": "Início da Pandemia de COVID-19"},
        {"data": "2020-04-20", "evento": "Petróleo Brent atinge valores negativos nos contratos futuros"},
        {"data": "2021-01-06", "evento": "Invasão do Capitólio"},
        {"data": "2021-08-10", "evento": "Plano global para redução de emissões de carbono impacta mercado de petróleo"},
        {"data": "2022-02-01", "evento": "Guerra da Ucrânia"},
        {"data": "2023-10-07", "evento": "Conflito Israel-Palestina"}
    ]


    fig_eventos = go.Figure()

    # Linha do preço de fechamento
    fig_eventos.add_trace(go.Scatter(
        x=df_filtrado['Date'],
        y=df_filtrado['Close'],
        mode='lines',
        name='Preço de Fechamento',
        line=dict(color='#6baed6', width=2)
    ))

    # Obtendo os limites de data do df_filtrado
    data_min = df_filtrado['Date'].min()
    data_max = df_filtrado['Date'].max()

    # Filtrar eventos dentro do intervalo de datas
    eventos_filtrados = [evento for evento in eventos if data_min <= pd.to_datetime(evento['data']) <= data_max]

    evento_x = []
    evento_y = []

    for evento in eventos_filtrados:
        evento_data = pd.to_datetime(evento['data'])
        
        # Pegando a data mais próxima se a exata não existir
        if evento_data in df_filtrado['Date'].values:
            valor_evento = df_filtrado[df_filtrado['Date'] == evento_data]['Close'].values[0]
        else:
            evento_data_proxima = df_filtrado.iloc[(df_filtrado['Date'] - evento_data).abs().argsort()[:1]]['Date'].values[0]
            valor_evento = df_filtrado[df_filtrado['Date'] == evento_data_proxima]['Close'].values[0]
        
        evento_x.append(evento_data)
        evento_y.append(valor_evento)

    # Adicionando os eventos ao gráfico (agora somente os dentro do período filtrado)
    fig_eventos.add_trace(go.Scatter(
        x=evento_x,
        y=evento_y,
        mode='markers',
        name="Evento",
        marker=dict(size=10, color='red'),
        hoverinfo='text',
        hovertext=[evento['evento'] for evento in eventos_filtrados]
    ))

    # Personalizando layout e legenda
    fig_eventos.update_layout(
        title="Preço do Brent com Eventos Impactantes",
        xaxis_title="Data",
        yaxis_title="Preço (USD)",
        template="plotly_dark",
        legend=dict(
            orientation="h",  # Deixa a legenda na horizontal
            x=0.5,            # Centraliza no eixo X
            xanchor="center",
            y=1.1,            # Posição acima do gráfico
            yanchor="top"
        )
    )

    # Exibindo o gráfico no Streamlit
    st.plotly_chart(fig_eventos)

    # Gráfico de Comparativo Abertura vs Fechamento (Média por Ano)
    df_filtrado['Média_Abertura'] = df_filtrado['Open'].mean()
    df_filtrado['Média_Fechamento'] = df_filtrado['Close'].mean()

    fig_comparativo = go.Figure()

    fig_comparativo.add_trace(go.Scatter(
        x=df_filtrado['Date'],
        y=df_filtrado['Open'],
        mode='lines',
        name='Abertura',
        line=dict(color='#4f81bd', width=2)
    ))

    fig_comparativo.add_trace(go.Scatter(
        x=df_filtrado['Date'],
        y=df_filtrado['Close'],
        mode='lines',
        name='Fechamento',
        line=dict(color='#6baed6', width=2)
    ))

    fig_comparativo.add_trace(go.Scatter(
        x=df_filtrado['Date'],
        y=df_filtrado['Média_Abertura'],
        mode='lines',
        name='Média Abertura',
        line=dict(color='#2ca02c', dash='dash')
    ))

    fig_comparativo.add_trace(go.Scatter(
        x=df_filtrado['Date'],
        y=df_filtrado['Média_Fechamento'],
        mode='lines',
        name='Média Fechamento',
        line=dict(color='#d62728', dash='dash')
    ))

    fig_comparativo.update_layout(
        title="Comparativo Abertura vs Fechamento com Médias",
        xaxis_title="Data",
        yaxis_title="Preço (USD)",
        template="plotly_dark"
    )

    # Exibindo o gráfico comparativo
    st.plotly_chart(fig_comparativo)

    # Gráfico de Distribuição de Fechamento
    fig_histograma = go.Figure()

    fig_histograma.add_trace(go.Histogram(
        x=df_filtrado['Close'],
        name="Distribuição de Fechamento",
        marker=dict(color='#6baed6', opacity=0.7),
        nbinsx=30
    ))

    fig_histograma.update_layout(
        title="Distribuição dos Preços de Fechamento",
        xaxis_title="Preço de Fechamento (USD)",
        yaxis_title="Frequência",
        template="plotly_dark"
    )

    # Exibindo o histograma de distribuição
    st.plotly_chart(fig_histograma)

    # Gráfico de Volatilidade
    df_filtrado['Volatilidade'] = df_filtrado['Close'].pct_change() * 100

    fig_volatilidade = go.Figure()

    fig_volatilidade.add_trace(go.Scatter(
        x=df_filtrado['Date'],
        y=df_filtrado['Volatilidade'],
        mode='lines',
        name='Volatilidade',
        line=dict(color='#6baed6', width=1)
    ))

    fig_volatilidade.update_layout(
        title="Volatilidade do Preço do Brent",
        xaxis_title="Data",
        yaxis_title="Variação Percentual (%)",
        template="plotly_dark"
    )

    # Exibindo o gráfico de volatilidade
    st.plotly_chart(fig_volatilidade)

# Chama a função para exibir o dashboard
if __name__ == "__main__":
    exibir_dashboard()
