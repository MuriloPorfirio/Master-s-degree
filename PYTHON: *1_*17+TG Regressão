import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import seaborn as sns
from scipy import stats

# Dados de PRU (ajustados para 56 elementos)
pru_values = np.array([
   
   167, 185, 221, 186, 187, 38, 79, 262, 115, 178, 294, 68, 68, 109, 183
])

# Dados de presença/ausência do haplótipo (Presença = 1, Ausência = 0, ajustados para 54 elementos)
haplotype_presence = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1])

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
plt.figure(figsize=(6, 4))  # Reduzindo o tamanho da figura para ser mais compacta
sns.scatterplot(x=haplotype_presence, y=pru_values, color='blue', s=100)
sns.lineplot(x=haplotype_presence, y=predictions, color='red', linewidth=2)

plt.xticks([0, 1], ['Ausente', 'Presente'], fontsize=12)
plt.yticks(fontsize=12)
plt.title('', fontsize=14)
plt.xlabel('Presença do Haplótipo', fontsize=12)
plt.ylabel('PRU (Agregação Plaquetária)', fontsize=12)
plt.legend(fontsize=12)
plt.tight_layout()  # Ajusta a figura para ocupar melhor o espaço
plt.show()

# Exibindo e descrevendo as métricas da regressão
print(f'Coeficiente de Determinação (R^2): {r_squared:.4f}')
print(f'Coeficiente do Modelo (Efeito do Haplótipo): {coefficient:.4f}')
print(f'Intercepto do Modelo (Valor de PRU quando o Haplótipo está ausente): {intercept:.4f}')
print(f'Valor-p do Teste t (Significância Estatística do Efeito do Haplótipo): {p_value:.4e}')
