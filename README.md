<h1>Análise de Séries Temporais e Previsão do Preço do Petróleo</h1>

Desenvolvido por Beatriz Rosa Carneiro Gomes

<p>Este projeto visa explorar dados históricos do petróleo por meio de análise de séries temporais e avaliação de diferentes modelos preditivos para prever o preço do petróleo Brent. O comparativo foi realizado entre os modelos <strong>ARIMA</strong> e <strong>LSTM</strong> para identificar o modelo mais eficaz. O modelo mais eficaz será implantado em produção via <strong>Streamlit</strong>, proporcionando um painel interativo que oferece insights sobre as variações de preços e seus fatores determinantes, como a geopolítica, crises econômicas e a demanda global. Após a escolha do modelo ideal, um plano de deploy será desenvolvido para garantir sua disponibilização e manutenção contínua em produção.</p>


<h2>2. Definindo Métricas para Avaliação de Modelos</h2>

<p>A função abaixo foi implementada para calcular as métricas de avaliação de cada modelo, facilitando a comparação de seu desempenho. As métricas utilizadas são:</p>

<h3>MAE (Erro Absoluto Médio)</h3>
<p>Calcula o erro absoluto médio entre os valores reais e as previsões. Quanto menor o MAE, mais preciso é o modelo.</p>

<h3>MSE (Erro Quadrático Médio)</h3>
<p>Calcula o erro quadrático médio, penalizando mais os erros grandes devido ao seu caráter quadrático. Quanto maior o erro, maior a penalização.</p>

<h3>MAPE (Erro Percentual Absoluto Médio)</h3>
<p>Mede a diferença entre os valores reais e os valores previstos, expressando o erro como uma porcentagem. Valores menores de MAPE indicam maior precisão do modelo.</p>

<p>Essas métricas são fundamentais para a análise do desempenho dos modelos, permitindo determinar o modelo com maior precisão preditiva.</p>

<h2>3. Exploração e Análise dos Dados</h2>

<p>A seguir, será realizada a análise exploratória dos dados, verificando os tipos de dados e identificando valores ausentes ou duplicados. Esses valores serão tratados adequadamente para garantir a integridade da análise. Além disso, será realizada uma descrição resumida dos dados, análise de outliers e avaliação da variação dos valores desde 2007.</p>

<h3>Outliers</h3>
<p>Outliers são valores que se desviam significativamente do restante das observações e podem impactar a precisão dos modelos. Através do <strong>Intervalo Interquartil (IQR)</strong>, os outliers serão identificados nas colunas de "Open" e "Close" da cotação do Petróleo. O impacto dos outliers será avaliado e tratado para garantir a precisão dos modelos de previsão.</p>

![image](https://github.com/user-attachments/assets/bff574e6-551d-4bd2-8448-5d600cceb89e)

<h3>Variação dos Preços de Petróleo (2007-2025)</h3>

![image](https://github.com/user-attachments/assets/450de358-46fc-4ef6-a750-003bcccd77d2)

<ul>
    <li><strong>2008:</strong> Preço do petróleo atinge recordes devido à demanda global e tensões no Oriente Médio. A crise financeira de 2008 leva o preço de US$ 140 para US$ 40.</li>
    <li><strong>2009-2014:</strong> Recuperação impulsionada por pacotes de estímulo, mas com oscilações devido a fatores como a produção de petróleo de xisto nos EUA.</li>
    <li><strong>2014-2016:</strong> Crise com queda do preço para US$ 30 devido ao aumento da produção de xisto e decisões da OPEP.</li>
    <li><strong>2020 (Pandemia):</strong> A COVID-19 reduz drasticamente a demanda, levando os preços a níveis negativos no mercado de futuros.</li>
    <li><strong>2021-2025:</strong> Recuperação pós-pandemia, com aumento da demanda global e tensões geopolíticas (como a guerra na Ucrânia) impactando os preços.</li>
</ul>

<p>Essa trajetória do Brent é sensível a uma série de fatores econômicos e geopolíticos, fazendo com que a previsão do preço do petróleo seja um desafio constante.</p>

<h2>4. Decomposição da Série Temporal</h2>

<p>A decomposição da série temporal é uma técnica que permite separar os dados em componentes distintas, facilitando a análise e interpretação dos mesmos:</p>

![image](https://github.com/user-attachments/assets/5144a2f1-70ac-426b-95f9-46bddaa935ee)

<ul>
    <li><strong>Tendência (Trend):</strong> Direção geral da série ao longo do tempo (crescente, decrescente ou estável).</li>
    <li><strong>Sazonalidade (Seasonality):</strong> Padrões que se repetem em intervalos regulares.</li>
    <li><strong>Ciclos (Cycles):</strong> Flutuações relacionadas a fatores econômicos ou eventos específicos.</li>
    <li><strong>Resíduos (Residuals):</strong> Variações aleatórias que não podem ser explicadas pelas componentes anteriores.</li>
</ul>

<p>Essa decomposição facilita a análise e o uso de modelos preditivos.</p>

<h2>5. Decomposição Autoregressiva</h2>

<p>A decomposição autoregressiva considera a dependência temporal dos dados e permite identificar a influência dos valores passados na previsão dos valores futuros. A diferenciação é uma técnica utilizada para transformar uma série temporal não estacionária em estacionária, o que é necessário para a aplicação de muitos modelos preditivos, como ARIMA. Através dessa técnica, garantimos que a série tenha propriedades constantes, como média e variância, ao longo do tempo.</p>

<h2>6. LSTM - Long Short-Term Memory</h2>

<p>O modelo <strong>LSTM</strong> (Long Short-Term Memory) é uma rede neural recorrente (RNN) especializada em capturar dependências de longo prazo em séries temporais. Ele mantém informações por períodos mais longos e é eficaz na captura de tendências e padrões sazonais complexos. Além disso, é mais robusto a ruídos pontuais em comparação com outros modelos como ARIMA.</p>

![image](https://github.com/user-attachments/assets/d724c1a0-5f0a-4d74-aa15-086773516f5e)

<h2>7. Comparação de Modelos</h2>

<p>Neste projeto, diferentes modelos de previsão serão comparados para determinar o que oferece o melhor desempenho. A comparação será realizada com base nas métricas MAE, MSE e MAPE. Modelos a serem considerados incluem ARIMA, LSTM, XGBoost, entre outros. O modelo com melhor desempenho será selecionado para implementação em produção.</p>

<h2>8. ARIMA (AutoRegressive Integrated Moving Average)</h2>

<p>O <strong>ARIMA</strong> é um modelo amplamente utilizado para previsão de séries temporais. Ele combina componentes autoregressivos (AR), médias móveis (MA) e diferenciação (I) para tornar a série estacionária e gerar previsões precisas. Será utilizado para comparar seu desempenho com outros modelos e escolher a melhor abordagem.</p>

<h2>Bibliotecas Utilizadas</h2>
<ul>
    <li><strong>Matplotlib:</strong> Para visualizações gráficas.</li>
    <li><strong>Numpy & Pandas:</strong> Para manipulação e análise dos dados.</li>
    <li><strong>Statsmodels:</strong> Para modelos estatísticos e decomposição da série temporal.</li>
    <li><strong>XGBoost:</strong> Algoritmo de aprendizado de máquina para previsão.</li>
    <li><strong>yfinance:</strong> Para obtenção de dados financeiros.</li>
    <li><strong>Plotly:</strong> Para visualizações interativas.</li>
    <li><strong>Keras:</strong> Para modelagem de redes neurais LSTM.</li>
</ul>
