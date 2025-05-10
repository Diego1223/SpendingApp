import flet as ft

class Clase_ingresos:
    #Hace referencia a SpendingApp del archivo main.py
    def __init__(self, app):
        self.app = app

    def CambiarValores_btn(self):
        self.app.btn_ingresos.bgcolor = self.app.container2_color
        self.app.btn_ingresos.color = "white"
        self.app.btn_ingresos.style = ft.ButtonStyle(side=ft.BorderSide(0.4, "white"),shape=ft.RoundedRectangleBorder(radius=10))

        #Cambia los valores de los otros botones (Gastos y todos)
        self.app.btn_gastos.color = self.app.container2_color
        self.app.btn_gastos.bgcolor = self.app.container_color
        self.app.btn_gastos.style = ft.ButtonStyle(side=ft.BorderSide(1, self.app.container2_color), shape=ft.RoundedRectangleBorder(radius=10))

    def Ingresos(self, e=None):
        #Para despues hacer las operaciones para mostrar
        #las horas extras a la semana
        #if ingreso semana == 7200 (No hubo extras)
        #else ingreso semana >= 7200 (Hubo extras -> Mostrar)
        ingreso_semana1 = 7200
        ingreso_semana2 = 7450
        ingreso_semana3 = 7200
        ingreso_semana4 = 7300


        self.row_ingresos1 = ft.Container(
            bgcolor=self.app.container_color,
            height=140, padding=5, border_radius=10,
            border=ft.border.all(1, self.app.container2_color),
            content=ft.Column(
                spacing=2,
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            #Ingresar una ventana emergente aqui mostrando las horas trabajadas a la semana
                            ft.IconButton(ft.icons.ATTACH_MONEY,icon_color="white"),
                            ft.Text("Ingresos activos", color=self.app.container2_color),
                            ft.IconButton(ft.icons.EDIT_CALENDAR, icon_color="white")
                        ]
                    ),
                    ft.Column(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            #El ingreso_semana1:, le indica a python que use coma como separador de miles
                            ft.Text(f"Ingreso semana 1: {ingreso_semana1:,}"),
                            ft.Text(f"Ingreso semana 2: {ingreso_semana2:,}"),
                            ft.Text(f"Ingreso semana 3: {ingreso_semana3:,}"),
                            ft.Text(f"Ingreso semana 4: {ingreso_semana4:,}")
                    ])
                ]
            )
        )
        self.app.main_content.controls.clear()
        #Actualizar esta linea de codigo
        self.app.main_content.controls.extend([self.row_ingresos1])

        self.CambiarValores_btn()
        self.app.page.update()
