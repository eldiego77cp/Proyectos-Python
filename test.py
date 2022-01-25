frase = '01062021 PAOLA CAREGLIO TRF FC B-0001-00000123'

lugarFrase = frase.find('TRF')

if frase.find('PAOLA') > 0:
    print(lugarFrase)
else:
    print('No existe la palabra "TRF" en la frase')