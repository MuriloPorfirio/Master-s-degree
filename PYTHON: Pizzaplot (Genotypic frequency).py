# total de 146 pacientes
import matplotlib.pyplot as plt
import numpy as np  # Importando numpy

# Dados dos grupos
grupo_counts = {
    '*1/*1': 68,
    '*1/*2': 29,
    '*1/*17': 36,
    '*2/*17': 7,
    '*17/*17': 6
}
total = sum(grupo_counts.values())  # Total de amostras genotipadas

# Calculando as porcentagens e preparando as etiquetas
sizes = list(grupo_counts.values())
labels = [f"{key}" for key in grupo_counts.keys()]
percentages = [f'{size} ({size/total*100:.1f}%)' for size in sizes]

# Cores em tons pastéis mais vívidos
colors = ['#FF6347', '#FFD700', '#4682B4', 'pink', '#32CD32']

# Criando o gráfico de pizza
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(aspect="equal"))

# Adicionando os dados ao gráfico
wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct='', startangle=140, colors=colors,
                                  wedgeprops={'edgecolor': 'w'})

# Adicionando as porcentagens dentro das fatias
for i, wedge in enumerate(wedges):
    angle = (wedge.theta2 - wedge.theta1)/2. + wedge.theta1
    x = np.cos(np.deg2rad(angle))
    y = np.sin(np.deg2rad(angle))
    ax.text(x*0.7, y*0.7, percentages[i], ha="center", va="center", color="black", fontsize=25)

# Ajustando o tamanho das etiquetas de legenda
for text in texts:
    text.set_fontsize(25)

# Mostra o gráfico
plt.show()
