import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import matplotlib.pyplot as plt
from datetime import timedelta

# Função para obter os dados do Brent utilizando o yfinance
@st.cache_data
def obter_dados_brent():
    ticker = "BZ=F"
    dados_brent = yf.download(ticker, start="2024-11-01", end="2025-02-10")
    df = dados_brent[["Close"]].reset_index()
    df.columns = ["Date", "Close"]
    return df

# Função para treinar o modelo LSTM
@st.cache_data
def treinar_modelo_lstm(df):
    scaler = MinMaxScaler(feature_range=(0, 1))
    df_scaled = scaler.fit_transform(df[["Close"]])

    X, y = [], []
    for i in range(60, len(df)):
        X.append(df_scaled[i-60:i, 0])
        y.append(df_scaled[i, 0])
    
    X, y = np.array(X), np.array(y)
    X = X.reshape(X.shape[0], X.shape[1], 1)

    modelo = Sequential()
    modelo.add(LSTM(units=50, return_sequences=True, input_shape=(X.shape[1], 1)))
    modelo.add(LSTM(units=50, return_sequences=False))
    modelo.add(Dense(units=1))

    modelo.compile(optimizer='adam', loss='mean_squared_error')
    modelo.fit(X, y, epochs=5, batch_size=32)

    return modelo, scaler

# Função para gerar as previsões para os próximos 'num_dias'
def gerar_previsao(modelo, scaler, df, num_dias):
    # Obtemos a data máxima dos dados históricos
    data_max = pd.to_datetime(df["Date"].max())
    
    # Gerar datas para os próximos 'num_dias' dias
    previsao_data = pd.date_range(start=data_max + timedelta(days=1), periods=num_dias, freq="D")
    
    # Preparando os dados de entrada para a previsão (usando sempre os últimos 60 dias)
    dados_entrada = df[["Close"]].tail(60).values  # Usamos os últimos 60 dias como entrada
    dados_entrada = scaler.transform(dados_entrada)  # Escalando os dados
    dados_entrada = dados_entrada.reshape(1, -1, 1)  # Ajustando a forma dos dados para o modelo

    previsao = []

    # Fazendo previsões iterativas para cada dia
    for _ in range(num_dias):
        # Prevendo o próximo dia
        pred = modelo.predict(dados_entrada)
        pred = scaler.inverse_transform(pred)  # Revertendo a escala para o valor real
        previsao.append(pred[0, 0])  # Adiciona a previsão para o próximo dia
        
        # Atualizando os dados de entrada com a previsão mais recente
        dados_entrada = np.append(dados_entrada[:, 1:, :], pred.reshape(1, 1, 1), axis=1)

    # Criando DataFrame com os resultados da previsão
    df_previsao = pd.DataFrame({"Data": previsao_data, "Preço Previsto": previsao})
    
    return df_previsao


# Função para exibir o gráfico com os dados históricos e a previsão
def exibir_grafico(df, df_previsao):
    # Plotando os dados históricos e as previsões
    plt.figure(figsize=(10, 6))
    plt.plot(df["Date"], df["Close"], label="Preço Histórico", color="blue")
    plt.plot(df_previsao["Data"], df_previsao["Preço Previsto"], label="Preço Previsto", color="red", linestyle="--")
    
    plt.title("Previsão do Preço do Brent")
    plt.xlabel("Data")
    plt.ylabel("Preço (USD)")
    plt.legend()
    st.pyplot(plt)

# Função principal
def exibir_previsao():
    df = obter_dados_brent()
    modelo, scaler = treinar_modelo_lstm(df)
    
    data_max = df["Date"].max()
    data_prevista = pd.to_datetime("2025-02-10")  # Exemplo de data de previsão
    
    df_previsao = gerar_previsao(modelo, scaler, df, data_max, data_prevista)
    exibir_grafico(df, df_previsao)

if __name__ == "__main__":
    exibir_previsao()
