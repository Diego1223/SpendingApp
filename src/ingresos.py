import flet as ft

class Clase_ingresos:
    #Hace referencia a SpendingApp del archivo main.py
    def __init__(self, app):
        self.app = app

    def Ingresos(self, e=None):
        self.texto = ft.Text("Ingresos")

        self.app.main_content.controls.clear()
        #Actualizar esta linea de codigo
        #self.app.main_content.controls.extend([self.texto])

        self.app.page.update()

        