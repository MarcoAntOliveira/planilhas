import pandas as pd

def soma_gastos(arquivo):
    df = pd.read_excel(arquivo)
    return df['custo_março'].sum()

# Criando um DataFrame com dados de exemplo
dados = {'março': ['café', 'BC', 'passagem'],
         'custo_março': [25, 50, 35],
         }

df = pd.DataFrame(dados)

# Escreve o DataFrame em um arquivo Excel
df.to_excel('saida.xlsx', index=False)

print(df.head())