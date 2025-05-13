import flet as ft


class Clase_gastos:
    #El constructor hace referencia a la clase SpendingApp de main.py
    def __init__(self, app):
        self.app = app
    #Restaura los valores del Progressbar cuando se cliquea el boton
    def restaurar_valores(self,e):
        self.pgbagua.value = 0
        self.pgbinternet.value = 0
        self.pgbluz.value = 0
        self.pgbtaxi.value =0 
        self.pgbtren.value = 0
        self.pgbvuelo.value = 0 
        self.pgb_total.value = 0
        self.app.page.update()

    def cambiar_valores_btn(self):
        self.app.btn_gastos.bgcolor = self.app.container2_color
        self.app.btn_gastos.color = "white" 
        self.app.btn_gastos.style = ft.ButtonStyle(side=ft.BorderSide(0.4, "white"), shape=ft.RoundedRectangleBorder(radius=10))
       
        #Cambia los valores de los otros dos botones
        self.app.btn_ingresos.color = self.app.container2_color
        self.app.btn_ingresos.bgcolor = self.app.container_color 
        self.app.btn_ingresos.style = ft.ButtonStyle(side=ft.BorderSide(1, self.app.container2_color), shape=ft.RoundedRectangleBorder(radius=10))
    def Gastos(self,e=None):
        #Progresbar1
        #Vuelo, tren y taxi
        self.pgbvuelo = ft.ProgressBar(value=0.7, bgcolor=self.app.container2_color, border_radius=5, height=5, width=150, color="white")
        self.pgbtren = ft.ProgressBar(value=0.85, bgcolor=self.app.container2_color, border_radius=5, height=5, width=150, color="white")
        self.pgbtaxi = ft.ProgressBar(value=0.65, bgcolor=self.app.container2_color, border_radius=5, height=5, width=150, color="white")
        bgcolor=self.app         
        self.row_4 = ft.Container(
        bgcolor=self.app.container_color,
        height=140,padding=5,
        border_radius=10,   
        border=ft.border.all(1, self.app.container2_color), #Sirve para darle el color de los bordes
        content=ft.Column(
            spacing=2,
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.IconButton(icon=ft.icons.DIRECTIONS_CAR_FILLED_OUTLINED, icon_color="white"),
                        ft.Text("Viajes y Transporte", color=self.app.container2_color),
                        ft.IconButton(icon=ft.icons.EDIT_CALENDAR, icon_color="white"),
                        ]
                    ),
                    ft.Column(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Row([
                                ft.Text("Vuelo", color=self.app.container2_color, width=40),
                                self.pgbvuelo,
                                ft.Text("70 %", color=self.app.container2_color),
                            ]),
                            ft.Row([
                                ft.Text("Tren", color=self.app.container2_color, width=40),
                                self.pgbtren,
                                ft.Text("85 %", color=self.app.container2_color),
                            ]),
                            ft.Row([
                                ft.Text("Taxi", color=self.app.container2_color, width=40),
                                self.pgbtaxi,
                                ft.Text("68 %", color=self.app.container2_color),
                            ]),
                        ]
                    ),
                ]
            ))
        
        #ProgressBar 2
        #Valores que despues en otra funcion reanudaremos
        self.pgbluz = ft.ProgressBar(value=0.75, bgcolor=self.app.container2_color, border_radius=5, height=5, width=150, color="white")
        self.pgbagua = ft.ProgressBar(value=0.39, bgcolor=self.app.container2_color, border_radius=5, height=5, width=150, color="white")
        self.pgbinternet = ft.ProgressBar(value=0.45, bgcolor=self.app.container2_color, border_radius=5, height=5, width=150, color="white")
        self.row_5 = ft.Container(
            bgcolor=self.app.container_color,
            height=140,padding=5,
            border_radius=10,   
            border=ft.border.all(1, self.app.container2_color),
            content=ft.Column(
            spacing=2,
            controls=[
                 ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.IconButton(icon=ft.icons.HOME_OUTLINED, icon_color="white"),
                        ft.Text("Casa", color=self.app.container2_color),
                        ft.IconButton(icon=ft.icons.EDIT_CALENDAR, icon_color="white"),
                    ]),
                ft.Column(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Row([
                            ft.Text("Luz", color=self.app.container2_color, width=60),
                            self.pgbluz,
                            ft.Text("75 %", color=self.app.container2_color),
                            ]),
                            ft.Row([
                            ft.Text("Agua", color=self.app.container2_color, width=60),
                            self.pgbagua,
                            ft.Text("39 %", color=self.app.container2_color),
                            ]),
                            ft.Row([
                            ft.Text("Internet", color=self.app.container2_color, width=60),
                            self.pgbinternet,
                            ft.Text("45 %", color=self.app.container2_color),
                        ]),
                    ]),
                ])
            )

        #Progress bar container 3
        self.pgb_total = ft.ProgressBar(value=0.45, bgcolor=self.app.container2_color, border_radius=5, height=10, width=150, color=self.app.blue_color)
        self.row_6 = ft.Container(
            bgcolor=self.app.container_color,
            height= 70,padding=10,
            border_radius=10,
            content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Column(controls=[
                    ft.Text("Total gastado $7,800", color=self.app.container2_color, weight="bold",size=15),
                    self.pgb_total
                    ]),
                    ft.IconButton(icon=ft.icons.POWER_SETTINGS_NEW, bgcolor="transparent",
                    style = ft.ButtonStyle(side = ft.BorderSide(1, self.app.container2_color),
                    shape=ft.RoundedRectangleBorder(radius=10)), on_click=self.restaurar_valores),
                    ]
                )
            )
        self.app.main_content.controls.clear()
        self.app.main_content.controls.extend([self.row_4, self.row_5, self.row_6])

        self.cambiar_valores_btn()
        self.app.page.update()
