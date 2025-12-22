import pandas as pd

# Valores
mercado_agosto = 9.60 + 7.60 + 36.62 + 17.77 + 3.98 + 47.84 + 28.61
locomocao_agosto = 19.00 + 3.50 + 19.12 + 12.50
bolsa_agosto = 963.89 + 300
cartao_agosto = 150

# Dados
dados = {
    "Agosto": ["Aluguel", "Aniversário Yukio", "Mercado Agosto", "Locomoção Agosto", "Papelaria", "cartao agosto"],
    "Valores": [801, 23.42, mercado_agosto, locomocao_agosto, 29.30, cartao_agosto],
    "Entradas Agosto": ["Bolsa", "Dinheiro mãe", "", "", ""],
    "valores_entradas": [bolsa_agosto, 150, 0, 0, 0],
}

# Criar DataFrame
df = pd.DataFrame(dados)

# Criar linha total de gastos e entradas
total_gastos = df["Valores"].sum()
total_entradas = df["valores_entradas"].sum()
sobrou = total_entradas - total_gastos

# Adicionar linha de totais
df.loc["Total"] = ["Total", total_gastos, "Total Entradas", total_entradas]
df.loc["Sobrou"] = ["Sobrou", sobrou, "", ""]

# Mostrar tabela
print(df)

# Salvar em Excel
df.to_excel("gastos.xlsx", index=False)
