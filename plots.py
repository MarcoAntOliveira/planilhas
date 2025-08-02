import pandas as pd
import matplotlib.pyplot as plt

# Criar o DataFrame (mesmo exemplo anterior)
dados = {
    "Produtos A": ["Banana", "Maçã", "Laranja", "Uva"],
    "Valores A": [2.5, 3.0, 4.2, 1.8],

    "Produtos B": ["Arroz", "Feijão", "Macarrão", "Farinha"],
    "Valores B": [5.0, 6.0, 3.5, 4.5],

    "Produtos C": ["Sabonete", "Shampoo", "Pasta", "Escova"],
    "Valores C": [1.2, 7.5, 3.0, 2.5],
}

df = pd.DataFrame(dados)

# Calcular a soma de cada coluna de valores
somas = {
    "A": df["Valores A"].sum(),
    "B": df["Valores B"].sum(),
    "C": df["Valores C"].sum()
}

# Plotar gráfico de barras
plt.figure(figsize=(8, 5))
plt.bar(somas.keys(), somas.values(), color=["orange", "blue", "green"])
plt.title("Total por Categoria")
plt.xlabel("Categorias")
plt.ylabel("Valor Total")
plt.grid(axis='y')
plt.tight_layout()
plt.show()

plt.pie(somas.values(), labels=somas.keys(), autopct='%1.1f%%')
plt.title("Distribuição percentual dos valores")
plt.show()

plt.plot(df["Produtos A"], df["Valores A"], marker='o', label="Valores A")
plt.plot(df["Produtos B"], df["Valores B"], marker='s', label="Valores B")
plt.plot(df["Produtos C"], df["Valores C"], marker='^', label="Valores C")
plt.legend()
plt.title("Valor por Produto")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

