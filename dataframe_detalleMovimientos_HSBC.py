import os
import pathlib
import pandas as pd

inputDirectory = 'C:\\Users\\Alejandro\\Downloads\\'
inputFile = 'DetalleMovimientos.csv'

workingDirectory = os.getcwd()
print(os.listdir(inputDirectory))

print(workingDirectory)

df = pd.read_csv(inputDirectory+inputFile, header=0, delimiter=',')

print(df)

help(pd)