import pandas as pd 

file = pd.ExcelFile('./sales.xlsx')
print(file.sheet_names)
sheet = file.parse('sales')
print(sheet)
print(sheet.Date)