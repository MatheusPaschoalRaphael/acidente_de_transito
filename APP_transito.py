import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

### Importando os arquivos CSV 
df_arquivo2021 = pd.read_csv("acidentes2021_todas_causas_tipos.csv", sep=';', low_memory=False)
df_arquivo2022 = pd.read_csv("acidentes2022_todas_causas_tipos.csv", sep=';', low_memory=False)
df_arquivo2023 = pd.read_csv("acidentes2023_todas_causas_tipos.csv", sep=';', low_memory=False)
df_arquivo2024 = pd.read_csv("acidentes2024_todas_causas_tipos.csv", sep=';', low_memory=False)
df_arquivo2025 = pd.read_csv("acidentes2025_todas_causas_tipos.csv", sep=';', low_memory=False)

## Visualizando as primeiras linhas dos dataframes
#print(df_arquivo2021.head())
#print(df_arquivo2022.head())
#print(df_arquivo2023.head())
#print(df_arquivo2024.head())
#print(df_arquivo2025.head())

## Concatenando todos os dataframes em um unico dataframe
df_todos_anos = pd.concat([df_arquivo2021, df_arquivo2022, df_arquivo2023, df_arquivo2024, df_arquivo2025], ignore_index=True)

## Visualizando as primeiras e ultimas linhas do dataframe concatenado
print(df_todos_anos.head(100))
print (df_todos_anos.tail(100))


## Analisando a estrutura dos dataframes
#df_todos_anos['uf'].value_counts().plot(kind='bar', title="Grafico de Barras")
#plt.show()

#df_todos_anos['dia_semana'].value_counts().plot(kind='bar', title="Grafico de Barras")
#plt.show()
