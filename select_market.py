from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
import pandas as pd
import os, sys
import datetime
from natsort import index_natsorted
import numpy as np
import mercados


def main():
    """
    docstring
    """

    categorias = ["ofertas", "frutas", "verduras", "organicos",
                  "viandas", "limpieza", "perfumeria"]

    almacen = ["fideos-y-legumbres", "snacks", "aceites-acetos", "galletitas-golosinas", "frutos-secos",
               "especias", "salsas", "infusiones-endulzantes", "mermeladas-dulces", "conservas", "harinas", "aderezos"]
    
    frios = ["frescos", "congelados"]

    bebidas = ["aguas","gaseosas","jugos","bebidas-sin-alcohol","cervezas","vinos"]

    for i in range(len(categorias)):
        buscar(categorias[i], categorias[i])

    for i in range(len(almacen)):
        buscar("almacen/"+almacen[i], almacen[i])

    for i in range(len(frios)):
        buscar("frios/"+frios[i], frios[i])    

    for i in range(len(bebidas)):
        buscar("bebidas/"+bebidas[i], bebidas[i])    

def buscar(busqueda, categoria):
    """
    docstring
    """
    if not busqueda == "":
        todos_los_productos = []
        driver.get(mercados.select_market+busqueda)
        producto_a_objeto(todos_los_productos)
        df = pd.DataFrame(todos_los_productos)
        orden = "producto"
        ordenado = df.sort_values(
            by=str(orden),
            key=lambda x: np.argsort(index_natsorted(df[str(orden)]))
        )
        today = str(datetime.date.today())
        localdir = os.getcwd()
        #time = str(datetime.datetime.now()).replace(" ", "_").replace(":", "-")
        if not os.path.isdir(localdir+"/tablas/select_market/"+today):
            os.mkdir(localdir+"/tablas/select_market/"+today)
        
        if not os.path.isfile(f"tablas/select_market/{today}/por_{orden}_{categoria}_tabla.csv"):
            f = open(
                f"tablas/select_market/{today}/por_{orden}_{categoria}_tabla.csv", "x")
            f.write(ordenado.to_csv(index=False))
            f.close()
        busqueda = ""
        orden = ""
        print("busqueda finalizada")

def producto_a_objeto(todos_los_productos):

    productos = driver.find_elements_by_css_selector(
        ".nombre a")
    precios = driver.find_elements_by_css_selector(
        ".precio")

    for i in range(len(productos)):
        todos_los_productos.append(
            {"producto": productos[i].text, "precio": precios[i].text.replace("\n", " ")})

if __name__ == "__main__":
#   options = Options()
#   options.headless = True
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)

    print("inicializando...")
    driver = webdriver.Firefox(executable_path='geckodriver')
    driver.implicitly_wait(5)
    print("inicializacion finalizada.")
    main()
