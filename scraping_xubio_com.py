from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

pathWebdriver = 'C:\\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(pathWebdriver)

xubioLogin = 'https://xubio.com/NXV/newLogin'
xubioMayores = 'https://xubio.com/NXV/contabilidad/libro-mayor'

userName = 'administracion@argenbio.org'
userPass = '*#Xubio1977#*'

# Ids de la página de logueo de xubio.com
htmlIdUserName = 'userName'
htmlIdUserPass = 'password'
htmlIdIngresarButton = 'loginbuton'

# Carga de la página xubio.com y toma del control por parte del webdriver
driver.get(xubioLogin)

# Ubicación de los elementos por ids
windowUser = driver.find_element_by_id(htmlIdUserName)
windowPass = driver.find_element_by_id(htmlIdUserPass)
ingresarButton = driver.find_element_by_id(htmlIdIngresarButton)

windowUser.send_keys(userName)
windowPass.send_keys(userPass)
ingresarButton.click()

# Carga de la página https://xubio.com/NXV/contabilidad/libro-mayor y toma del control por parte del webdriver
driver.get(xubioMayores)

# Xpaths de la página de mayores de xubio.com
fechaDia = driver.find_elements_by_name('day').text
fechaMes = driver.find_elements_by_name('month').text
fechaAño = driver.find_elements_by_name('year').text
cuentaContable = driver.find_element_by_xpath('/html/body/div[8]/table/tbody/tr[1]/td/div/table/tbody/tr[6]/td[1]/input')

print(fechaDia)
print(fechaMes)
print(fechaAño)

driver.quit()