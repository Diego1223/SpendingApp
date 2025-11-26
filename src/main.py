import flet as ft
from datetime import datetime
from login import IniciarSesion, Registro
from Pagina_principal import Pagina_principal
from json_manager import cargar_sesion

#Actulizacion a futuro 
#1. Migrar la persistencia a SQLite

# Colores
BG_COLOR = "#30304d"
BLUE_COLOR = "#88ddfb"
CONTAINER_COLOR = "#23243d"
CONTAINER2_COLOR = "#484a66"

# EJECUTAR: flet run main.py -d
class SpendingApp(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__(expand=True)
        self.page = page
        self.page.bgcolor = BG_COLOR
        self.page.horizontal_alignment = "center"
        self.page.vertical_alignment ="center"
        self.window_maximized = True

        #Sesiones
        sesion = cargar_sesion()

        def route_change(route):
            self.page.views.clear()
            
            if self.page.route == "/" and not sesion.get("is_logged", False):
                self.page.views.append(IniciarSesion(self.page))
            elif self.page.route == "/registro":
                self.page.views.append(Registro(self.page))
            elif self.page.route == "/Pagina_principal":
                self.page.views.append(Pagina_principal(self.page))
            else:
                #Redireccion automatica si ya tiene sesion
                #sesion.get dice -> quiero saber si el diccionario tiene el valor logged 
                #si lo tiene damelo si no manda False
                if sesion.get("is_logged", False):
                    self.page.go("/Pagina_principal")
                    return #Es importante parar aqui
            self.page.update()
                

        self.page.on_route_change = route_change
        self.page.go(self.page.route)
 


def main(page: ft.Page):
    SpendingApp(page)
    page.update()


ft.app(target=main)
