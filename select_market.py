from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
import pandas as pd
import mercados

def buscar(todos_los_productos):
    """
    docstring
    """
    busqueda = input("ingrese su busqueda: ")
    if not busqueda == "":
        todos_los_productos = []
        driver.get(mercados.select_market+busqueda)
        producto_a_objeto(todos_los_productos)
        df = pd.DataFrame(todos_los_productos)
        print(df)
        busqueda = ""
        todos_los_productos = []
    buscar(todos_los_productos)

def main():
    """
    docstring
    """
    todos_los_productos = []
    buscar(todos_los_productos)


def producto_a_objeto(todos_los_productos):

    productos = driver.find_elements_by_css_selector(
        ".nombre a")
    precios = driver.find_elements_by_css_selector(
        ".precio")

    for i in range(len(productos)):
        todos_los_productos.append(
            {"producto": productos[i].text, "precio": precios[i].text.replace("\n", " ")})

def is_int(string):  
    final = ''  
    for i in string:  
        try:   
            final += str(int(i))   
        except ValueError:  
            return int(final)


if __name__ == "__main__":
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)

    print("inicializando...")
    driver = webdriver.Firefox(executable_path='geckodriver')
    driver.implicitly_wait(5)
    print("inicializacion finalizada.")
    main()



