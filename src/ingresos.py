import flet as ft
from datetime import datetime

class Semana_Ingreso:
    def __init__(self, app, ingreso, n_semana):
        #Para despues hacer las operaciones para mostrar
        #las horas extras a la semana
        #if ingreso semana == 7200 (No hubo extras)
        #else ingreso semana >= 7200 (Hubo extras -> Mostrar)
        self.app = app
        self.ingreso = ingreso
        self.n_semana = n_semana
        self.expandido = False
        self.mostrar_extras = ingreso > 7200

        self.flecha = ft.IconButton(
            icon=ft.icons.KEYBOARD_ARROW_DOWN,
            icon_color="white",
            on_click=self.toggle_expandir
        )

        self.detalle_column = ft.Column(
            visible=False,  # Inicialmente oculto
            controls=[
                ft.Text(f"Pago semanal: {self.ingreso}", color=self.app.container2_color),
                ft.Text(f"Pago horas extras: {self.ingreso - 7200 if self.mostrar_extras else 'No hubo'}", color=self.app.container2_color),
                ft.Text(f"Horas trabajadas: {round(self.ingreso / (7200 / 48))}", color=self.app.container2_color),
                ft.Text(f"Horas extras: {round(self.ingreso / (7200 / 48)) - 48 if self.mostrar_extras else 'No hubo'}", color=self.app.container2_color)
            ]
        )

        self.container = ft.Container(
            bgcolor=self.app.container_color,
            height=50,
            padding=5,
            border_radius=10,
            animate=ft.Animation(300, "easeInOut"),
            border=ft.border.all(1, self.app.container2_color),
            content=ft.Column(
                spacing=2,
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            self.flecha,
                            ft.Text(f"Semana {self.n_semana} (Ingreso activo)"),
                            ft.IconButton(ft.icons.EDIT_CALENDAR, icon_color="white", on_click=self.mostrar_calendario)
                        ]
                    ),
                    self.detalle_column
                ]
            )
        )

    def toggle_expandir(self, e):
        self.expandido = not self.expandido
        self.flecha.icon = ft.icons.KEYBOARD_ARROW_UP if self.expandido else ft.icons.KEYBOARD_ARROW_DOWN
        self.detalle_column.visible = self.expandido
        self.container.height = 180 if self.expandido else 50
        self.app.page.update()

    def mostrar_calendario(self, e):
        self.app.date_picker.open = True
        self.app.page.update()


class Clase_ingresos:
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
        self.ingreso_semana1 = 7200
        self.ingreso_semana2 = 7450
        self.ingreso_semana3 = 7200
        self.ingreso_semana4 = 7300
        self.horas_laboradas = 8
        self.app.main_content.controls.clear()
        ingresos_lista = [self.ingreso_semana1, self.ingreso_semana2, self.ingreso_semana3, self.ingreso_semana4]
        
        for i, ingreso in enumerate (ingresos_lista, start=1):
            semana = Semana_Ingreso(self.app, ingreso, i)
            self.app.main_content.controls.append(semana.container)
        

        #El DatePicker se crea una vez, no en cada llamada
        #hassatar(objeto, atributo) -> pregunta el objeto self.app tiene un atributo llamado date_picker? 
        #SI no, lo crea
        #De esta forma solo tenemos un date picker en toda la aplicacioon y la podemos usar donde sea
        if not hasattr(self.app, "Date picker"):
            self.app.date_picker = ft.DatePicker(on_change=lambda e: e.control.value)
            #EL overlay es una lista de elementos flotantes sobre la interfaz principal (como modales o datepickers)
            self.app.page.overlay.append(self.app.date_picker) 


        self.CambiarValores_btn()
        self.app.page.update()
