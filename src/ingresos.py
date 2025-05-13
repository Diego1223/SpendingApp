import flet as ft
from datetime import datetime

class Clase_ingresos:
    #Hace referencia a SpendingApp del archivo main.py
    def __init__(self, app):
        self.app = app
        self.expandido = False
    #Expande el panel de las semanas trabajadas
    def toggle_expandir(self):
        self.expandido = not self.expandido

        if self.expandido:
            self.flecha.icon = ft.icons.KEYBOARD_ARROW_UP
            self.row_ingresos1.height = 180

        else:
            self.flecha.icon = ft.icons.KEYBOARD_ARROW_DOWN    
            self.row_ingresos1.height = 50 

        self.app.page.update()

    def mostrar_calendario(self,e):
        self.date_picker.open = True
        self.app.page.update()
    

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
        self.ingreso_semana1 = 7200
        self.ingreso_semana2 = 7450
        self.ingreso_semana3 = 7200
        self.ingreso_semana4 = 7300
        self.horas_laboradas = 8

        #CREAR EL DATE PICKER para mostrar el calendario
        self.date_picker = ft.DatePicker(
            on_change= lambda e: e.control.value
        )
        self.app.page.overlay.append(self.date_picker)
        
        #La flecha sirve para el toggle
        self.flecha = ft.IconButton(ft.icons.KEYBOARD_ARROW_DOWN,icon_color="white",on_click=lambda e: self.toggle_expandir())
        self.mostrar_extra = False
        

        self.row_ingresos1 = ft.Container(
            bgcolor=self.app.container_color,
            height=50, padding=5, border_radius=10,animate=ft.Animation(300, "easeInOut"),
            border=ft.border.all(1, self.app.container2_color),
            content=ft.Column(
                spacing=2,
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            #Ingresar una ventana emergente aqui mostrando las horas trabajadas a la semana
                            self.flecha,
                            ft.Text("Semana 1 (Ingreso activo)"),
                            ft.IconButton(ft.icons.EDIT_CALENDAR, icon_color="white", on_click=self.mostrar_calendario)
                        ]
                    ),
                    ft.Column(
                        #Usamos 8 porque son las horas laborales obligatorias en el dia
                        #round() -> sirve para quitar los puntos decimales
                        controls=[
                        ft.Text(f"Pago semanal: {self.ingreso_semana1}", color=self.app.container2_color),
                        ft.Text(f"Pago horas extras: {(self.ingreso_semana1 - 7200) if self.mostrar_extra else "No hubo"}", color=self.app.container2_color),
                        ft.Text(f"Horas trabajadas: {round(((8*self.ingreso_semana1) / 7200) * 6)}", color=self.app.container2_color),
                        ft.Text(f"Horas extras: {(8*self.ingreso_semana1) / 7200 - 8 if self.mostrar_extra else "No hubo"}", color=self.app.container2_color)
                    ])
                ]
            )
        )
        self.app.main_content.controls.clear()
        #Actualizar esta linea de codigo
        self.app.main_content.controls.extend([self.row_ingresos1])

        self.CambiarValores_btn()
        self.app.page.update()
