import pandas as pd



# Dados
dados = {
    "treino A": ["Rosca diretazzzz", "", "circuitos ceifadores", "ceifadores em serie", "ceifadores em paralelo", "circuitos grampeadores"],
    "circuitos_Diodos": ["Análise por reta de carga", "circuitos retificadores", "circuitos ceifadores", "ceifadores em serie", "ceifadores em paralelo", "circuitos grampeadores"],
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
