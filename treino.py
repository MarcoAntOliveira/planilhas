import pandas as pd



# Dados
dados = {
    "treino A": ["Rosca direta777", "rosca alternada pegada", "elevação triceps", "flexão", "elevação lateral"],
    "repetições":[ "5X21", "circuitos retificadores", "circuitos ceifadores", "ceifadores em serie", "ceifadores em paralelo"],
    "treino B": ["agaxamento", "abdomen x agaxamento", "panturilha", " abdominal", "agaxamento afundo"],
    "repetições": ["20x18x16x14x12", "5x12", "5x12", "5x12", "5x12", "5x12"],
    "treino A": ["Rosca direta777", "rosca alternada pegada", "elevação triceps", "flexão", "elevação lateral"],
    "repetições": ["Análise por reta de carga", "circuitos retificadores", "circuitos ceifadores", "ceifadores em serie", "ceifadores em paralelo"],
    "treino A": ["Rosca direta777", "rosca alternada pegada", "elevação triceps", "flexão", "elevação lateral"],
    "repetições": ["Análise por reta de carga", "circuitos retificadores", "circuitos ceifadores", "ceifadores em serie", "ceifadores em paralelo"],
}

# Criar DataFrame
df = pd.DataFrame(dados)


# Mostrar tabela
print(df)

# Salvar em Excel
df.to_excel("treino.xlsx", index=False)
