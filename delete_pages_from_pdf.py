'''
def deletePagesInPDFFile (inPdfFilename, outPdfFilename, pages):
    pdfWriter = PyPDF2.PdfWriter()
    pdfReader = PyPDF2.PdfReader(inPdfFilename)
    for i in range(pdfReader.getNumPages()):
        if i not in pages:
            page = pdfReader.getPage(i)
            pdfWriter.addPage(page)
    
    with open(outPdfFilename, 'wb') as outPdf: 
        pdfWriter.write(outPdf)

# Ejecución de la función con los parámetros pasados

indPdfFilename = ''
outPdfFilename = ''
pages = (0, 1)
deletePagesInPDFFile(indPdfFilename, outPdfFilename, pages)
'''

# Programa que permite eliminar páginas de un archivo pdf sin tener que editarlo

# Importa los módulos a utilizar

from PyPDF2 import PdfFileWriter, PdfFileReader
from io import open
import os


# Fases de manipulación de archivos: Crear (si no existe) > Abrir > Manipular > Cerrar
# Setea el directorio dónde se encuentran los pdfs y genera la lista de archivos para extraer sus páginas

dirReadPdf = 'C:\\Output\\'
listAllPdfFiles = os.listdir(dirReadPdf)
listPdfFiles = []

for i in range (len(listAllPdfFiles)):
    filename = listAllPdfFiles[i]
    if filename.find('TRF') < 0:
        listPdfFiles.append(filename)

os.mkdir('C:\\Output\\out_dir\\')
outDir = 'C:\\Output\\out_dir\\'

# Inicializa los objetos 

for i in range (len(listPdfFiles)):
    inputPdfStr = dirReadPdf + listPdfFiles[i]
    outputPdfStr = outDir + listPdfFiles[i]
    outputPdf = open(outDir + listPdfFiles[i], 'wb')

    pdfReader = PdfFileReader(inputPdfStr)
    pdfWriter = PdfFileWriter()

    # Obtiene la página 0 del pdf

    page = pdfReader.getPage(0)
    pdfWriter.addPage(page)
    pdfWriter.write(outputPdf)

    outputPdf.close()

    


