import pandas as pd
import openpyxl
import random as rd


# df = pd.read_excel('C:/Users/Alejandro/Downloads/my_df.xlsx')

#print(len(df)+1)
#
#print(df['total_amount'].head(5))
#
#print(df['total_amount'].loc[0])
#
#tendencia = []
#for index in range(0, len(df), 1):
#    if index == 0:
#        tendencia.append(df['total_amount'].loc[index]*1.05)
#        tendencia.append(df['total_amount'].loc[index]*0.9)
#    else:
#        tendencia.append(df['total_amount'].loc[index]*0.9)
#
#print(tendencia)

# df4 = (df.groupby(by='week').sum()).sort_values('total_amount',ascending=False)
# print(len(df4.index))
# print(df4['total_amount'])
# 
# tendencia = []
# for index in df4.index:
#     if index == 1:
#         tendencia.append(int(df4['total_amount'].loc[index]*1.05))
#         tendencia.append(int(df4['total_amount'].loc[index]*0.9))
#     else:
#         tendencia.append(int(df4['total_amount'].loc[index]*0.9))
# 
# print(tendencia)


results = {'Vicky': 0, 'Lola': 0}
lados = list(results.keys())

for x in range(1): 
    results[rd.choice(lados)] =+1

if results['Vicky'] == 1:
    print('Vicky va a la ducha primero porque tiene mucho olor a culo')
else:
    print('Lola va a la ducha primero porque tiene mucho olor a culo')