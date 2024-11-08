import pandas as pd

# Criando um DataFrame com dados de exemplo
dados = {'Nome': ['Alice', 'Bob', 'Charlie'],
         'Idade': [25, 30, 35],
         'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']}

df = pd.DataFrame(dados)

# Escreve o DataFrame em um arquivo Excel
df.to_excel('saida.xlsx', index=False)

print(df.head())