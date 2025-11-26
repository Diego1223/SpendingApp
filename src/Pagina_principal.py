import flet as ft
from db import Database
from json_manager import cargar_sesion

#TODO: SEGUIR CON LA PAGINA PRINCIPAL
 

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
        sesion = cargar_sesion()
        nombre = sesion.get("nombre")

        #Widgets del header
        self.bienvenida = ft.Container(
            height=50,
            content= ft.Row(controls=[
                ft.Text(f"Bienvenido de nuevo {nombre}", 
                    color=ft.Colors.WHITE,
                    #weight=ft.FontWeight.BOLD,
                    size=18
                )
            ], alignment=ft.MainAxisAlignment.START)
        )

        self.config = ft.Container(
            height=50,
            content=ft.Row(controls=[
                ft.IconButton(ft.Icons.SETTINGS_SHARP, icon_color=ft.Colors.WHITE)
            ], alignment=ft.MainAxisAlignment.END)
        )

        self.header = ft.Row(controls=[
            self.bienvenida, self.config
        ], expand=True, alignment=ft.MainAxisAlignment.SPACE_BETWEEN)


        #Widgets de ingresos y egresos
        self.ingresos_egresos = ft.Container(
            content=ft.Row([
                # Ingresos
                ft.Container(
                    height=80,
                    expand=True,
                    padding=5,
                    bgcolor=CONTAINER2_COLOR,
                    border_radius=10,
                    content=ft.Column(
                        controls=[
                            ft.Row(
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    ft.Text("Ingreso"),
                                    ft.Container(
                                        alignment=ft.alignment.center,
                                        bgcolor="green",
                                        height=10,
                                        width=10,
                                        border_radius=5
                                    )
                                ]
                            ),
                            ft.Text("$ 74,900", size=25, weight="bold"),
                        ]
                    )
                ),
                # Gastos
                ft.Container(
                    height=80,
                    expand=True,
                    padding=5,
                    bgcolor=CONTAINER2_COLOR,
                    border_radius=10,
                    content=ft.Column(
                        controls=[
                            ft.Row(
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    ft.Text("Gastos"),
                                    ft.Container(
                                        alignment=ft.alignment.center,
                                        bgcolor="red",
                                        height=10,
                                        width=10,
                                        border_radius=5
                                    )
                                ]
                            ),
                            ft.Text("$ 24,845", size=25, weight="bold"),
                        ]
                    )
                )
            ])
        )

        self.controls = [ft.Column(
            expand=True, scroll="auto",spacing=10,
            controls=[
                self.header, 
                ft.Divider(),
                self.ingresos_egresos
                ]
            )]