import pandas as pd

# Dados dos treinos organizados em colunas separadas
treinos = {
    "Treino A": [
        ("Flexão", "8 x 15"),
        ("Flexão com elástico", "8 x 15"),
        ("Supino elástico", "8 x 15"),
        ("Peito porção inferior", "8 x 15"),
        ("Puxada sentado", "8 x 15"),
        ("Puxada em pé", "8 x 15"),
        ("Desenvolvimento", "8 x 15"),
        ("Deltoide", "8 x 15"),
        ("Trapézio", "8 x 15")
    ],
    "Treino B": [
        ("Abdominal crunch", "8 x 10"),
        ("Abdominal elevação", "8 x 10"), 
        ("Agachamento afundo", "8 x 10"),
        ("Agachamento lento", "8 x 10"),
        ("Agachamento búlgaro quadríceps", "8 x 10"),
        ("-", "-"),
        ("-", "-"),
        ("-", "-"),
        ("-", "-")
    ]
}

# Criar DataFrame e separar os dados em duas colunas para cada treino
df_treinos = pd.DataFrame({
    "Exercício A": [ex[0] for ex in treinos["Treino A"]],
    "Repetições A": [ex[1] for ex in treinos["Treino A"]],
    "Exercício B": [ex[0] for ex in treinos["Treino B"]],
    "Repetições B": [ex[1] for ex in treinos["Treino B"]]
})

# Exportar para Excel
with pd.ExcelWriter("treinos.xlsx") as writer:
    df_treinos.to_excel(writer, index=False)

print("Planilha criada com sucesso!")
