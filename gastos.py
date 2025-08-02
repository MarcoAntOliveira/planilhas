import pandas as pd

# Dados de exemplo
dados = {
    "Produtos A": ["Banana", "Maçã", "Laranja", "Uva"],
    "Valores A": [2.5, 3.0, 4.2, 1.8],

    "Produtos B": ["Arroz", "Feijão", "Macarrão", "Farinha"],
    "Valores B": [5.0, 6.0, 3.5, 4.5],

    "Produtos C": ["Sabonete", "Shampoo", "Pasta", "Escova"],
    "Valores C": [1.2, 7.5, 3.0, 2.5],
}

# Descobrir quantos pares de colunas temos
num_linhas = len(next(iter(dados.values())))
df = pd.DataFrame(dados)

# Adicionar linha com as somas
linha_soma = {}
for col in df.columns:
    if "Valores" in col:
        linha_soma[col] = df[col].sum()
    else:
        linha_soma[col] = "Total"

# Adiciona a linha ao DataFrame
df.loc["Total"] = linha_soma

# Salvar como Excel ou mostrar no terminal
print(df)

# (Opcional) salvar em Excel
df.to_excel("produtos_valores.xlsx", index=False)
