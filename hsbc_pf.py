import unittest
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

# Manejador automatizado de Chrome (buscar el archivo chromedriver.exe)
# Definir el path del chromedriver.exe y ejecutarlo

path = 'E:\\Chromedriver\\chromedriver.exe'
chrome_driver = webdriver.Chrome(path)

# Abrir cualquier página web llamando al objeto objeto.get(website)

hsbcLoginPage = 'https://www.obempresas.hsbc.com.ar/bib/login'
chrome_driver.get(hsbcLoginPage)

# Buscar y completar campos textos (inspeccionar previamente los elementos para obtener los name, id, etc)

usuario = chrome_driver.find_element_by_name('userName')
usuario.send_keys('argenbio2006')