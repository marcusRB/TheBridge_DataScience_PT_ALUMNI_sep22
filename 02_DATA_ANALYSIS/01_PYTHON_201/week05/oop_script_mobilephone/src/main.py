'''
Docstring main.py
'''

# Importamos las librerías
from setup import config
from utils import utils

# importamos la estructura del telefono
mobile_phone = config.mobile
perc_carga = 0.80
appname_yt = config.youtube



if __name__ == '__main__':
    # ejecuta el script o función del main.py
    objeto_telefono = utils.MobilePhone(mobile_phone)
    
    
    objeto_telefono.carga_mobile(perc_carga)
    print(objeto_telefono.perc_carga)

    objeto_telefono.install_app(appname_yt)
    print(objeto_telefono.phone)