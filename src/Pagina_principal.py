import flet as ft
from db import Movimientos
from json_manager import cargar_sesion
from ingresos import ListaIngresos


#TODO: SEGUIR CON LA PAGINA PRINCIPAL

# --- Colores base ---
BG_COLOR = "#30304d"
CONTAINER_COLOR = "#23243d"
CONTAINER2_COLOR = "#484a66"

class Pagina_principal(ft.View):
    def __init__(self, page):
        #vamos a traer los datos de la clase movimientos
        #Tambien accedemos a esta instancia en metodos de mas abajo
        self.movimiento = Movimientos()
        ingreso = self.movimiento.mostrar_ingreso()
        egreso = self.movimiento.mostrar_egresos()
        diferencia = ingreso - egreso

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
                ft.Text(f"Bienvenido de nuevo {nombre}", color=ft.Colors.WHITE, size=18)
            ], alignment=ft.MainAxisAlignment.START)
        )

        self.config = ft.Container(
            height=50,
            content=ft.Row(controls=[
                ft.PopupMenuButton(
                    items=[
                        ft.PopupMenuItem(text="Item 1"),
                        ft.PopupMenuItem(text="Item 2")
                    ],
                    icon=ft.Icons.SETTINGS_SHARP,
                    icon_color=ft.Colors.WHITE,
                    tooltip="Configuracion"
                )
            ], alignment=ft.MainAxisAlignment.END)
        )

        self.header = ft.Row(
            controls=[ self.bienvenida, self.config ],
            expand=True,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )

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
                            ft.Text(f"$ {ingreso:.0f}", size=25, weight="bold"),
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
                            ft.Text(f"$ {egreso:.0f}", size=25, weight="bold"),
                        ]
                    )
                )
            ])
        )

        # Gráfica
        x_values = list(range(1, 16))
        green_line = [1.2, 1.5, 2.0, 8, 3.2, 5, 2.0, 2.5, 5, 10, 2.1, 4, 2.0, 6, 1.7]
        red_line = [1.8, 8, 1.5, 7, 1.6, 1.8, 2.0, 10, 1.8, 3, 2.0, 2.2, 5, 2.0, 9]

        bottom_axis = ft.ChartAxis(labels_size=25, labels_interval=3, show_labels=True)
        left_axis = ft.ChartAxis(labels_size=25, labels_interval=5, show_labels=True)

        self.chart_data = ft.LineChart(
            tooltip_bgcolor="transparent",
            data_series=[
                ft.LineChartData(
                    data_points=[
                        ft.LineChartDataPoint(x, y, selected=(x == 8))
                        for x, y in zip(x_values, green_line)
                    ],
                    color=ft.Colors.GREEN,
                    stroke_width=1,
                    curved=True,
                    below_line_bgcolor=ft.Colors.with_opacity(0.2, ft.Colors.GREEN),
                ),
                ft.LineChartData(
                    data_points=[
                        ft.LineChartDataPoint(x, y, selected=(x == 8))
                        for x, y in zip(x_values, red_line)
                    ],
                    color=ft.Colors.RED,
                    stroke_width=1,
                    curved=True,
                    below_line_bgcolor=ft.Colors.with_opacity(0.2, ft.Colors.RED),
                )
            ],
            min_y=0,
            max_y=10,
            expand=True,
            border=ft.Border(
                bottom=ft.BorderSide(1, ft.Colors.with_opacity(0.3, ft.Colors.WHITE)),
                left=ft.BorderSide(1, ft.Colors.with_opacity(0.3, ft.Colors.WHITE)),
            ),
            bottom_axis=bottom_axis,
            left_axis=left_axis,
        )

        self.row_2 = ft.Container(
            bgcolor=CONTAINER2_COLOR,
            border_radius=10,
            height=120,
            padding=10,
            content=ft.Column(
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Text("Diferencia"),
                            ft.Text(f"$ {diferencia}", size=15, weight="bold"),
                        ]
                    ),
                    self.chart_data
                ]
            )
        )

        #Barra de todos, ingresos y egresos

        self.btn_gastos = ft.ElevatedButton(
            text="Gastos",
            color=CONTAINER2_COLOR,
            bgcolor=CONTAINER_COLOR,
            style=ft.ButtonStyle(
                side=ft.BorderSide(1, CONTAINER2_COLOR),
                shape=ft.RoundedRectangleBorder(radius=10)
            )
        )

        self.btn_ingresos = ft.ElevatedButton(
            text="Ingresos",
            color=CONTAINER2_COLOR,
            bgcolor=CONTAINER_COLOR,
            style=ft.ButtonStyle(
                side=ft.BorderSide(1, CONTAINER2_COLOR),
                shape=ft.RoundedRectangleBorder(radius=10)
            ),
            on_click=self.mostrar_ingreso
        )

        self.barra_contenido = ft.Container(
            height=30,
            border_radius=10,
            bgcolor=CONTAINER_COLOR,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.ElevatedButton(
                        text="Todos",
                        color=CONTAINER2_COLOR,
                        bgcolor=CONTAINER_COLOR,
                        style=ft.ButtonStyle(
                            side=ft.BorderSide(1, CONTAINER2_COLOR),
                            shape=ft.RoundedRectangleBorder(radius=10)
                        )
                    ),
                    self.btn_ingresos,
                    self.btn_gastos
                ]
            )
        )

        #Aqui se mostrara todo lo de los ingresos / gastos
        #Tiene su propio metodo
        self.panel_dinamico = ft.Column(spacing=10)

        self.controls = [
            ft.Column(
                expand=True,
                scroll="auto",
                spacing=10,
                controls=[
                    self.header,
                    ft.Divider(),
                    self.ingresos_egresos,
                    self.row_2,
                    self.barra_contenido,
                    self.panel_dinamico
                    #self.lista_ingresos_ui
                ]
            )
        ]

    def mostrar_ingreso(self, e):
        #Obtencion de ingresos
        lista_tuplas = self.movimiento.obtener_ingresos()
        ingresos_ui = ListaIngresos(lista_tuplas).build()
        
        #CAMBIAR VALORES DE LOS BOTONES
        self.btn_ingresos.bgcolor = CONTAINER2_COLOR
        self.btn_ingresos.color = "white"
        self.btn_ingresos.style = ft.ButtonStyle(
            side=ft.BorderSide(0.4, "white"),
            shape=ft.RoundedRectangleBorder(radius=10)
        )

        #Cambiar los valores del boton de gastos
        self.btn_gastos.color = CONTAINER2_COLOR
        self.btn_gastos.bgcolor = CONTAINER_COLOR
        self.btn_gastos.style = ft.ButtonStyle(
            side=ft.BorderSide(1, CONTAINER2_COLOR),
            shape=ft.RoundedRectangleBorder(radius=10)
        )

        #Limpiar la seleccion
        self.panel_dinamico.controls.clear()

        #Anadir nuevo contenido
        self.panel_dinamico.controls.append(
            ft.Text("Ingresos")
        )
        self.panel_dinamico.controls.append(ingresos_ui)
        self.update()

"""
        #Obtencion de ingresos - Esta parte es muy importante para ahorita
        lista_tuplas = movimiento.obtener_ingresos()
        self.lista_ingresos_ui = ft.Column(spacing=5)

        for i, (monto, fecha, tipo) in enumerate(lista_tuplas, start=0):
            item = ft.Container(
                padding=10,
                border=ft.border.all(1, "white"),
                content=ft.Column([
                    ft.Text(f"Ingreso {i}: ${monto}"),
                    ft.Text(f"Fecha: {fecha}")
                ])
            )            
            self.lista_ingresos_ui.controls.append(item)
"""

