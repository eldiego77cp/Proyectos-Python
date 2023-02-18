# Librerías de Selenium para webScrapping

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Otras librerías

import time

# Manejador automatizado de Chrome (buscar el archivo chromedriver.exe)
# Definir el path del chromedriver.exe y ejecutarlo

path = "E:\\Chromedriver\\chromedriver.exe"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(path, chrome_options=chrome_options)

# Abrir cualquier página web llamando al objeto objeto.get(website)

hsbcLoginPage = "https://www.obempresas.hsbc.com.ar/bib/login"
hsbcMainPage = "https://www.obempresas.hsbc.com.ar/bib/#welcome"
hsbcInversionesPage = 'https://www.obempresas.hsbc.com.ar/bib/#ConsultaPlazosFijos'
hsbcNuevoPfPage = 'https://www.obempresas.hsbc.com.ar/bib/#NuevoPlazoFijo'
hsbcAutorizacionesPage = 'https://www.obempresas.hsbc.com.ar/bib/#AutorizacionesPendientes'

# Variables de logueo / pf

user = "argenbio2006"
password = "subaru50"
cuentaDebito = "CC ARS - 3003337010 - "
fechaVto = "02/03/2023"
importePf = "1000000"
totalPf = 15

#------------------------------------------------------
# Ids de la página de logueo

usuarioId = 'userName'
confirmarId = 'dijit_form_Button_0_label'
claveXpath = '//*[@id="dijit_form_ValidationTextBox_0"]'
claveTokenId = 'dijit_form_ValidationTextBox_1'
confirmarIngresoId = 'dijit_form_Button_1_label'
cancelarId = 'dijit_form_Button_0_label'

# Ids de la página de inicio

salirId = 'dijit_form_Button_0'

# Ids, Xpaths de la página de nuevo PF

menuCuentaDebitoFxpath = "//span[@role='option' and contains(text(), 'Seleccione uno ...')]"
cuentaDebitoFxpath = "//td[contains(text(), '3003337010')]"
radioBotonNoFxpath = "(//div[contains(text(), 'Declaración')]/descendant::input) [1]"
radioBotonSiFxpath = "(//div[contains(text(), 'Declaración')]/descendant::input) [2]"
botonAceptarDdjjFxpath = "//div[contains(@class, 'dijitDialog')]/descendant::h3[text()='Declaración Jurada']/ancestor::div[contains(@class, 'dijitDialog')]/descendant::span[text()='Aceptar']"
botonCerrarDjjjFxpath = "//div[contains(@class, 'dijitDialog')]/descendant::h3[text()='Declaración Jurada']/ancestor::div[contains(@class, 'dijitDialog')]/descendant::span[text()='Cerrar']"
radioBotonFechaVtoFxpath = "//span[contains(text(), 'Por Fecha de Vencimiento')]/preceding-sibling::div/child::input"
radioBotonCantDiasFxpath = "//span[contains(text(), 'Por Cantidad de Días')]/preceding-sibling::div/child::input"
textBoxDiasFxpath = "(//span[text()='30 (Días)']/preceding-sibling::input[@class='dijitReset dijitInputInner']) [1]"
textBoxFechaVtoFxpath = "(//span[text()='Seleccione Fecha']/preceding-sibling::input[@class='dijitReset dijitInputInner']) [1]"
textBoxMontoPfFxpath = "//div[@class='dijitTextBox STextBox currencyField']/descendant::input[@class='dijitReset dijitInputInner']"
botonContinuarFxpath = "//span[text()='Constituya nuevas cuentas de Plazo Fijo']/ancestor::div[@id='_body']/descendant::div[@class='submitButtonsPanel border_ext']/descendant::span[text()='Continuar']"
botonContinuar2Fxpath = "//h2[contains(text(), 'Verificación del Plazo Fijo')]/ancestor::div/descendant::div[@class='submitButtonsPanel']/descendant::span[text()='Continuar']"
botonAceptarSaldoFxpath = "//p[contains(text(), 'saldo')]/ancestor::div/descendant::span[text()='Aceptar']"


#------------------------------------------------------

# Logueo en HSBC Empresas

driver.get(hsbcLoginPage)

try:
    usuarioField = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, usuarioId))
        )
    usuarioField.send_keys(user)

    confirmarBoton = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, confirmarId))
        )
    confirmarBoton.click()
    
    claveField = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, claveXpath))
        )
    claveField.send_keys(password)
    time.sleep(15)
    
    driver.find_element(By.ID, 'dijit_form_Button_1_label').click()
    
    # driver.find_element(By.ID, usuarioId).send_keys(user)
    # driver.find_element(By.ID, confirmarId).click()
    # time.sleep(5)

    # driver.find_element(By.XPATH, claveXpath).send_keys(password)
    # time.sleep(15)

    # driver.find_element(By.ID, 'dijit_form_Button_1_label').click()
    # time.sleep(10)
except:
    driver.quit()

# Nuevo PF

for cantidadPf in range(totalPf):
    driver.get(hsbcNuevoPfPage)
    time.sleep(3)

    try:
        menuCtaDb = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, menuCuentaDebitoFxpath))
        )
        menuCtaDb.click()
        print(f"Click en Menú Cta Débito Ok")
        ctaDb = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, cuentaDebitoFxpath))
        )
        ctaDb.click()
        print(f"Click en Cta Débito Ok")
        radioBotonNo = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, radioBotonNoFxpath))
        )
        radioBotonNo.click()
        print(f"Click en radio boton DDJJ Ok")
        aceptarDdjj = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, botonAceptarDdjjFxpath))
        )
        aceptarDdjj.click()
        print(f"Click en boton Aceptar DDJJ Ok")
        radioBotonFechaVto = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, radioBotonFechaVtoFxpath))
        )
        radioBotonFechaVto.click()
        print(f"Click en radio boton Fecha Vto Ok")
        driver.find_element(By.XPATH, textBoxFechaVtoFxpath).send_keys(fechaVto)
        driver.find_element(By.XPATH, textBoxMontoPfFxpath).send_keys(importePf)
        
        continuarPf = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, botonContinuarFxpath))
        )
        continuarPf.click()
        print(f"Click en Continuar PF Ok")
        time.sleep(2)
        continuar2Pf = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, botonContinuar2Fxpath))
        )
        continuar2Pf.click()
        print(f"Click en Continuar 2 PF Ok")
        aceptarSaldo = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, botonAceptarSaldoFxpath))
        )
        aceptarSaldo.click()
        print(f"Click en Aceptar Saldo Ok")
    except:
        driver.get(hsbcMainPage)
    
driver.get(hsbcAutorizacionesPage)
    
    # time.sleep(10)
    # driver.find_element(By.XPATH, menuCuentaDebitoFxpath).click()
    # time.sleep(1)11111
    # driver.find_element(By.XPATH, cuentaDebitoFxpath).click()
    # time.sleep(1)
    # driver.find_element(By.XPATH, radioBotonNoFxpath).click()
    # time.sleep(2)
    # driver.find_element(By.XPATH, botonAceptarDdjjFxpath).click()
    # time.sleep(5)
    # driver.find_element(By.XPATH, radioBotonFechaVtoFxpath).click()
    # time.sleep(1)
    # driver.find_element(By.XPATH, textBoxFechaVtoFxpath).send_keys(fechaVto)
    # driver.find_element(By.XPATH, textBoxMontoPfFxpath).send_keys(importePf)
    # driver.find_element(By.XPATH, botonContinuarFxpath).click()
    # time.sleep(5)
    # 
    # driver.find_element(By.XPATH, botonContinuar2Fxpath).click()
    # time.sleep(5)
    #
    # driver.find_element(By.XPATH, botonAceptarSaldoFxpath).click()
    # time.sleep(3)



# driver.quit()