import pandas as pd



# Dados
dados = {
"treino A": ["Rosca direta 777", "rosca alternada pegada","rosca baixo", "elevação tríceps", "triceps costas","triceps serote", "elevação lateral", "ombro frontal" ,"desenvolvimento"],
    "repetições A": ["5x15", "5x15", "5x15", "5x15", "5x15", "5x15", "5x15", "5x15", "5x15"],

    "treino B": ["agachamento", "abdômen x agachamento", "panturrilha", "abdominal", "agachamento afundo", "", "","",""],
    "repetições B": ["20x18x16x14x12", "5x12", "5x12", "5x12", "5x12", "", "", "", ""],

    "treino C": ["peito_inferior", "peito desenvolvimento", "costas baixo x ", "flexão inclinado x declinado", "trapezio x desenvolvimento",  "", "", "", ""],
    "repetições C": ["5x15", "5x15", "5x15", "5x15", "5x15",  "", "", "", ""],

    "treino D": ["Rosca direta 777", "rosca alternada pegada", "elevação tríceps", "flexão", "elevação lateral", "", "", "", ""],
    "repetições D": ["5x15", "5x15", "5x15", "5x15", "5x15",  "", "", "", ""],
}


# Criar DataFrame
df = pd.DataFrame(dados)


# Mostrar tabela
print(df)

# Salvar em Excel
df.to_csv("treino2.csv", index=False)
