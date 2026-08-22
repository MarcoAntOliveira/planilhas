import pandas as pd



# Dados
dados = {
"treino A": ["Rosca direta x a nt-inv", "rosca inv x ant","rosca banco", "biceps baix", "triceps testa","triceps p", "triceps sent", "ombro frontalx mbr " ,"desenvolvimento"],
    "repetições A": ["5x15", "5x15", "5x15", "5x15", "5x15", "5x15", "5x15", "5x15", "5x15"],

    "treino B": ["agachamento", "abdômen x agachamento", "panturrilha", "abdominal", "agachamento afundo", "", "","",""],
    "repetições B": ["20x18x16x14x12", "5x12", "5x12", "5x12", "5x12", "", "", "", ""],

    "treino C": ["fex_inferior", "peito sup", "costas baixo  ", "polia peito", "costa banco",  "", "", "", ""],
    "repetições C": ["5x15", "5x15", "5x15", "5x15", "5x15",  "", "", "", ""],

    "treino D": ["stiff", "gluteos banco", "gluteos canela", "agaxmento maquina", "elevação lateral", "", "", "", ""],
    "repetições D": ["5x15", "5x15", "5x15", "5x15", "5x15",  "", "", "", ""],
}


# Criar DataFrame
df = pd.DataFrame(dados)


# Mostrar tabela
print(df)

# Salvar em Excel
df.to_csv("treino2.csv", index=False)
