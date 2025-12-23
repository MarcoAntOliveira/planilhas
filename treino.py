import pandas as pd



# Dados
dados = {
    "treino A": ["Rosca direta 777", "rosca alternada pegada", "elevação tríceps", "flexão", "elevação lateral"],
    "repetições A": ["5x21", "circuitos retificadores", "circuitos ceifadores", "ceifadores em série", "ceifadores em paralelo"],

    "treino B": ["agachamento", "abdômen x agachamento", "panturrilha", "abdominal", "agachamento afundo"],
    "repetições B": ["20x18x16x14x12", "5x12", "5x12", "5x12", "5x12"],

    "treino C": ["Rosca direta 777", "rosca alternada pegada", "elevação tríceps", "flexão", "elevação lateral"],
    "repetições C": ["Análise por reta de carga", "circuitos retificadores", "circuitos ceifadores", "ceifadores em série", "ceifadores em paralelo"],

    "treino D": ["Rosca direta 777", "rosca alternada pegada", "elevação tríceps", "flexão", "elevação lateral"],
    "repetições D": ["Análise por reta de carga", "circuitos retificadores", "circuitos ceifadores", "ceifadores em série", "ceifadores em paralelo"],
}


# Criar DataFrame
df = pd.DataFrame(dados)


# Mostrar tabela
print(df)

# Salvar em Excel
df.to_csv("treino.csv", index=False)
