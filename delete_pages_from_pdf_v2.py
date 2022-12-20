# Programa que permite eliminar páginas de un archivo pdf sin tener que editarlo

# Importa los módulos a utilizar

from PyPDF2 import PdfWriter, PdfReader
from io import open
import os


# Fases de manipulación de archivos: Crear (si no existe) > Abrir > Manipular > Cerrar
# Setea el directorio dónde se encuentran los pdfs y genera la lista de archivos para extraer sus páginas

directorioPdfs = 'C:\\Output\\'

listaTodosLosArchivosPdf = os.listdir(directorioPdfs)
listaNuevosArchivosPdf = []

for archivoPdf in range (len(listaTodosLosArchivosPdf)):
    #nombreArchivoPdf = listaTodosLosArchivosPdf[i]
    #if nombreArchivoPdf.find('TRF') < 0:
    #    listaNuevosArchivosPdf.append(nombreArchivoPdf)
    nombreArchivoPdf = directorioPdfs + listaTodosLosArchivosPdf[archivoPdf]
    leerPdf = PdfReader(nombreArchivoPdf)
    datosPdf = leerPdf.getPage(0).extract_text().split("  ")
    fecha = ''
    letraFc = ''
    numero = ''
    proveedor = ''
    for letra in range(len(datosPdf)):
        if datosPdf[letra] == 'C' and datosPdf[letra+1] == 'O' and datosPdf[letra+2] == 'D' and datosPdf[letra+3] == '.':
            letraFc = datosPdf[letra-1]
    for letra in range(len(datosPdf)):
        if datosPdf[letra] == 'N' and datosPdf[letra+1] == 'r' and datosPdf[letra+2] == 'o' and datosPdf[letra+3] == ':':
            numero = datosPdf[letra+5:letra+19]
    for letra in range(len(datosPdf)):
        if datosPdf[letra] == 'N' and datosPdf[letra+1] == 'r' and datosPdf[letra+2] == 'o' and datosPdf[letra+3] == ':':
            numero = datosPdf[letra+5:letra+19]

    print(datosPdf)

#os.mkdir('C:\\Output\\out_dir\\')
#outDir = 'C:\\Output\\out_dir\\'

# Inicializa los objetos 

#for i in range (len(listPdfFiles)):
#    inputPdfStr = dirReadPdf + listPdfFiles[i]
#    outputPdfStr = outDir + listPdfFiles[i]
#    outputPdf = open(outDir + listPdfFiles[i], 'wb')
#
#    pdfReader = PdfReader(inputPdfStr)
#    pdfWriter = PdfWriter()
#
#    # Obtiene la página 0 del pdf
#
#    page = pdfReader.pages[0]
#    pdfWriter.add_page(page)
#    pdfWriter.write(outputPdf)
#
#    outputPdf.close()