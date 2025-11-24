import flet as ft
from db import Database
from json_manager import cargar_sesion


# --- Colores base ---
BG_COLOR = "#30304d"
CONTAINER_COLOR = "#23243d"
CONTAINER2_COLOR = "#484a66"

class Pagina_principal(ft.View):
    def __init__(self, page):
        super().__init__(
            route="/Pagina_principal",
            bgcolor = BG_COLOR,
            horizontal_alignment="center",
            vertical_alignment="center"
        )
        self.page = page
       
          
        self.header = ft.Container(
            height=50,
            content= ft.Row(controls=[
                ft.Text(f"Bienvenido de nuevo =")
            ], alignment=ft.MainAxisAlignment.SPACE_AROUND)
        )

        self.controls = [ft.Column(
            expand=True, scroll="auto",
            controls=[self.header]
            )]