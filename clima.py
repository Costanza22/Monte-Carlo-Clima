#simular as temperaturas mínimas e máximas, umidade às 9h e 15h, e a pressão às 9h e 15h
#Link para dados: https://www.kaggle.com/code/kunalkhurana007/rainfall-prediction-australia
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Criação do dataframe com os dados fornecidos
data = {
    "RowID": [13996, 13997, 13998, 13999, 14000, 14001, 14002],
    "Location": ["Canberra"] * 7,
    "MinTemp": [18.9, 13.2, 16.2, 19.8, 11.1, 11.1, 7.8],
    "MaxTemp": [34, 30.1, 37.1, 33.3, 24.5, 24.1, 28.1],
    "Humidity9am": [100, 76, 53, 98, 65, 67, 77],
    "Humidity3pm": [99, 32, 14, 56, 53, 53, 45],
    "Pressure9am": [1014.1, 1021.1, 1012.2, 1009.8, 1018.8, 1024, 1022.4],
    "Pressure3pm": [1011.6, 1017.9, 1007.9, 1012.2, 1016.9, 1021.8, 1017.8]
}

df = pd.DataFrame(data)

# Selecionar apenas as colunas numéricas
numeric_df = df.select_dtypes(include=[np.number])

# Calculando a média e o desvio padrão
mean_values = numeric_df.mean()
std_values = numeric_df.std()

# Número de simulações
num_simulations = 5000

# Dicionário para armazenar os resultados das simulações
simulated_data = {
    "MinTemp": [],
    "MaxTemp": [],
    "Humidity9am": [],
    "Humidity3pm": [],
    "Pressure9am": [],
    "Pressure3pm": []
}

# Realizando as simulações de Monte Carlo
np.random.seed(42)  # Para reprodutibilidade

for _ in range(num_simulations):
    simulated_data["MinTemp"].append(np.random.normal(mean_values["MinTemp"], std_values["MinTemp"]))
    simulated_data["MaxTemp"].append(np.random.normal(mean_values["MaxTemp"], std_values["MaxTemp"]))
    simulated_data["Humidity9am"].append(np.random.normal(mean_values["Humidity9am"], std_values["Humidity9am"]))
    simulated_data["Humidity3pm"].append(np.random.normal(mean_values["Humidity3pm"], std_values["Humidity3pm"]))
    simulated_data["Pressure9am"].append(np.random.normal(mean_values["Pressure9am"], std_values["Pressure9am"]))
    simulated_data["Pressure3pm"].append(np.random.normal(mean_values["Pressure3pm"], std_values["Pressure3pm"]))

# Convertendo os resultados simulados em DataFrame
simulated_df = pd.DataFrame(simulated_data)

# Plotando os resultados
plt.figure(figsize=(14, 8))

# Plot para MinTemp
plt.subplot(2, 3, 1)
plt.hist(simulated_df["MinTemp"], bins=30, color='blue', alpha=0.7)
plt.title('Simulated MinTemp')

# Plot para MaxTemp
plt.subplot(2, 3, 2)
plt.hist(simulated_df["MaxTemp"], bins=30, color='green', alpha=0.7)
plt.title('Simulated MaxTemp')

# Plot para Humidity9am
plt.subplot(2, 3, 3)
plt.hist(simulated_df["Humidity9am"], bins=30, color='red', alpha=0.7)
plt.title('Simulated Humidity9am')

# Plot para Humidity3pm
plt.subplot(2, 3, 4)
plt.hist(simulated_df["Humidity3pm"], bins=30, color='purple', alpha=0.7)
plt.title('Simulated Humidity3pm')

# Plot para Pressure9am
plt.subplot(2, 3, 5)
plt.hist(simulated_df["Pressure9am"], bins=30, color='orange', alpha=0.7)
plt.title('Simulated Pressure9am')

# Plot para Pressure3pm
plt.subplot(2, 3, 6)
plt.hist(simulated_df["Pressure3pm"], bins=30, color='cyan', alpha=0.7)
plt.title('Simulated Pressure3pm')

plt.tight_layout()
plt.show()
