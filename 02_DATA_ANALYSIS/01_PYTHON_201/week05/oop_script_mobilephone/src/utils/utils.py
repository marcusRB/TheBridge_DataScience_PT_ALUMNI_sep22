'''
Docstring del fichero - utils.py
Date:

'''

# Creamos una clase Mobile

class MobilePhone():
    '''
    Doc String
    Description de la clase
    '''
    def __init__(self, phone):
        self.phone = phone
        print("Clase MobilePhone inicializada correctamente!")

    def install_app(self, appname):
            '''
            La función .... instala la aplicación dado un objeto creado...

            Args:
            -----
                phone
                new_app Dict...
            Return:
            ------
            '''
            self.phone['apps'].append(appname)
            return self.phone

    def uninstall_app(self, appname):
        for pos, i in enumerate(self.phone['apps']):
            if i['name'] == appname:
                self.phone['apps'].pop(pos)
        return self.phone

    def update_app(self):
        pass

    def update_so(self):
        pass

    def carga_mobile(self, perc_carga=0):
        '''
        La función tome como parámetro un objeto tipo mobile y carga la bateria

        Args:
        ----
            phone Obj dict positional
        
        Return:
        ------
            Mismo objeto dict con valor charge actualizado
        '''
        # Convertimos perc_carga a nonlocal para uso como atributo
        self.perc_carga = perc_carga
        self.phone['bateria']['charge'] = self.perc_carga
        return self.phone


def prueba_fun():
    print("Hola")