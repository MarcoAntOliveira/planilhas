from openpyxl import Workbook

# Cria um novo arquivo Excel
wb = Workbook()

# Seleciona a ativa (primeira) aba
sheet = wb.active

# Escreve dados em células específicas
sheet['A1'] = 'Nome'
sheet['B1'] = 'Idade'
sheet['A2'] = 'Alice'
sheet['B2'] = 25

# Salva o arquivo
wb.save('saida.xlsx')
 