import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import seaborn as sns
from scipy import stats

# Dados de PRU (ajustados para 54 elementos)
pru_values = np.array([
    500, 50, 400, 60, 700, 346, 567, 345, 567, 455, 456, 456, 76, 45, 38, 39,
    467, 54, 41, 36, 32, 15, 40, 67, 54, 100, 102, 94, 130, 112, 476, 67, 109,
    99, 114, 107, 103, 112, 120, 134, 456, 784, 345, 676, 99, 130, 124, 115,
    109, 117, 130, 129, 98, 79
])

# Dados de presença/ausência do haplótipo (Presença = 1, Ausência = 0, ajustados para 54 elementos)
haplotype_presence = np.array([1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0,
1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1
])

# Verificando os comprimentos
print(f'Comprimento de pru_values: {len(pru_values)}')
print(f'Comprimento de haplotype_presence: {len(haplotype_presence)}')

# Reshape dos dados para se adequar ao formato exigido pela função de regressão do sklearn
X = haplotype_presence.reshape(-1, 1)
Y = pru_values

# Criação e ajuste do modelo de regressão linear
model = LinearRegression()
model.fit(X, Y)

# Predições do modelo para visualização da linha de regressão
predictions = model.predict(X)

# Calculando o coeficiente de determinação R^2
r_squared = model.score(X, Y)

# Coeficientes do modelo
coefficient = model.coef_[0]
intercept = model.intercept_

# Realizando o teste t para obter o valor-p
t_statistic, p_value = stats.ttest_ind(Y[haplotype_presence == 1], Y[haplotype_presence == 0], equal_var=False)

# Visualização dos dados e da linha de regressão em um único gráfico
plt.figure(figsize=(10, 6))
sns.scatterplot(x=haplotype_presence, y=pru_values, color='blue', label='Dados Observados')
sns.lineplot(x=haplotype_presence, y=predictions, color='red', label='Linha de Regressão')

plt.title('Regressão Linear da Presença do Haplótipo em relação a PRU em indivíduos *1/*17')
plt.xlabel('Presença/Ausência do Haplótipo')
plt.ylabel('PRU (Agregação Plaquetária)')
plt.legend()
plt.show()

# Exibindo e descrevendo as métricas da regressão
print(f'Coeficiente de Determinação (R^2): {r_squared:.4f}')
print(f'Coeficiente do Modelo (Efeito do Haplótipo): {coefficient:.4f}')
print(f'Intercepto do Modelo (Valor de PRU quando o Haplótipo está ausente): {intercept:.4f}')
print(f'Valor-p do Teste t (Significância Estatística do Efeito do Haplótipo): {p_value:.4e}')
