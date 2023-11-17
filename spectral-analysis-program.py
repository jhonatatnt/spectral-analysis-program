import pandas as pd
import glob
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#Caminho da pasta do google drive
link = "/content/drive/MyDrive/Dados espectrofotometro/…"

#Cada item representa uma pasta
aliquotas = [75, 150, 225, 300]

#DataFrame Concentracao // ABS
data = []
data.append([0,0])


for j in aliquotas:

  # Pegar pasta:
  path_folder = link + str(j)
  l_paths = glob.glob(path_folder + '/*')

  d_files = {}

  # Listar o nome dos arquivos e armazenar na lista l_names:
  for path in l_paths:
      d_files[path[54:-4]] = pd.read_csv(path, sep='\s+', header=None, names=['col0', 'col1'])

  l_names = list(d_files.keys())

  # Fazer uma estrutura de repetição para coletar dados de absorbância máxima de cada arq. da pasta aliquotas[i] e armazenar em um vetor
  vet_abs_max = []

  for i in l_names:
      DB = pd.read_csv(link + i + '.asc', sep='\t', header=None,
                      names=['λ', 'ABS'])
      max_abs = DB["ABS"].max()
      vet_abs_max.append(max_abs)

  #Calcular a média aritmetica das amostras da aliquotas[i]
  media_vet_abs_max = np.mean(vet_abs_max)
  elemento = [str(j/10), media_vet_abs_max]

  data.append(elemento)

df = pd.DataFrame(data, columns=['Concentração', 'Absorbância'])

# Criar o modelo de regressão linear
regressor = LinearRegression()

# Ajustar o modelo aos dados
regressor.fit(df[['Concentração']], df['Absorbância'])

# Coeficiente angular da reta
coef_angular = regressor.coef_[0]

# Coeficiente linear da reta
coef_linear = regressor.intercept_

# Imprimir a equação da reta
print(f"Equação da reta de regressão: y = {coef_angular:.7f}x + {coef_linear:.7f}")

# Gerar os valores previstos pela reta de regressão
predicted_values = regressor.predict(df[['Concentração']])

# Plotar a reta de regressão junto com os pontos
plt.plot(df['Concentração'], predicted_values, color='red', label='y = 0.0636447x + 0.3017013')

# Gerando pontos de dispersão
plt.scatter(df['Concentração'], df['Absorbância'], color='blue', label='Pontos de dispersão')

# Personalização do gráfico
plt.title('Curva de Calibração')
plt.xlabel('Concentração (mg/L)')
plt.ylabel('Absorbância (Abs)')
plt.legend()

# Exibir o gráfico
plt.show()
