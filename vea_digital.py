from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
import pandas as pd
import mercados

busqueda = "carne"
todos_los_productos = []


def producto_a_objeto():
    productos = driver.find_elements_by_css_selector(
        ".grilla-producto-descripcion")
    precios = driver.find_elements_by_css_selector(".grilla-producto-precio")
    unidades = driver.find_elements_by_css_selector(
        ".grilla-producto-unidades")
    for i in range(len(productos)):
        todos_los_productos.append(
            {"producto": productos[i].text, "precio": precios[i].get_attribute("textContent"), "unidad": unidades[i].text})


#options = Options()
#options.headless = True
driver = webdriver.Firefox(executable_path='geckodriver')
driver.implicitly_wait(5)
driver.get(mercados.vea+busqueda)


lista = driver.find_elements_by_id("product-list")

producto_a_objeto()
#todos_los_productos.replace("<div class='precio-tachado'></div>", "")

df = pd.DataFrame(todos_los_productos)

print(df)
