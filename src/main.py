import flet as ft
from datetime import datetime 
import gastos 
import ingresos


class SpendingApp(ft.Container):
    #Restaura los valores de las Progressbar cuando se presione el boton de apagado 
    def restaurar_valores(self, e):
        self.pgbagua.value = 0
        self.pgbinternet.value = 0
        self.pgbluz.value = 0
        self.pgbtaxi.value =0 
        self.pgbtren.value = 0
        self.pgbvuelo.value = 0 
        self.pgb_total.value = 0
        self.page.update()


    def __init__(self, page: ft.Page):
        super().__init__(expand=True)
        self.page = page 
        self.bg_color = "#30304d"
        self.page.bgcolor = self.bg_color
        self.blue_color = "#88ddfb"
        self.container_color = "#23243d"
        self.container2_color = "#484a66"

        self.menu_usuarios = ft.PopupMenuButton(
            icon=ft.Icons.PERSON_OUTLINED,
            icon_color=ft.Colors.WHITE,
            elevation=10,
            tooltip="Usuarios", #Muestra el texto "Usuarios cuando el cursor se coloca"
            items=[
                ft.PopupMenuItem(
                    content=ft.Row([
                        ft.Image(src="assets/avatar.png", height=30, width=30, border_radius=20),
                        ft.Text("Jhon")
                        ])),
                ft.PopupMenuItem(content=ft.Row([
                    ft.Image(src="assets/deni.enc", height=30, width=30, border_radius=20),
                    ft.Text("Denisse")
                ]))
            ]
        ) 
        self.header = ft.Container(
            height=50,
            content=ft.Row(
            #Espacio equitativo 
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            controls=[
                    ft.IconButton(icon=ft.icons.ARROW_BACK_IOS, icon_color="white"),
                    ft.Dropdown(
                        width=150,
                        hint_text="Este mes",
                        border_color= self.container2_color,
                        suffix_icon= ft.icons.KEYBOARD_ARROW_DOWN,
                        bgcolor = self.bg_color,
                        border_radius=10,                
                        icon_enabled_color="transparent",
                        options=[
                            ft.dropdown.Option("Noviembre"),
                            ft.dropdown.Option("Diciembre"),
                            ft.dropdown.Option("Enero"),
                        ],
                    ),
                    self.menu_usuarios
            ]
        ))
        
        #Listas del dia y mes
        self.dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
        self.meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
        self.dia = datetime.now()
    
        self.dia_str = self.dias[self.dia.weekday()]
        self.mes_str = self.meses[self.dia.month - 1]   
 
        self.title = ft.Container(
            height=20, padding=0,
            #Introducir fecha actual 
            content=ft.Text(f"a {self.dia_str} de {self.mes_str} de {self.dia.year}", color=ft.colors.with_opacity(0.5, "white"))
            )
        
        self.row_1 = ft.Container(
            content=ft.Row([
                ft.Container(
                    height=80,
                    expand=True,padding=5,
                    bgcolor=self.container2_color,
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
                                height=10, width=10,
                                border_radius=5
                            )
                        ]
                    ),
                    ft.Text("$ 74,900", size=25, weight="bold"),
                    ]
                    )
                ),
                ft.Container(
                    height=80,
                    expand=True,padding=5,
                    bgcolor=self.container2_color,
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
                                height=10, width=10,
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

        #grafica
        x_values = list(range(1, 16))
        green_line = [1.2, 1.5, 2.0, 8, 3.2, 5, 2.0, 2.5, 5, 10, 2.1, 4, 2.0, 6, 1.7]
        red_line = [1.8, 8, 1.5, 7, 1.6, 1.8, 2.0, 10, 1.8, 3, 2.0, 2.2, 5, 2.0, 9]

        bottom_axis = ft.ChartAxis(labels_size=25, labels_interval=3, show_labels=True)
        left_axis = ft.ChartAxis(labels_size=25, labels_interval=5, show_labels=True)

        self.chart_data = ft.LineChart(
            tooltip_bgcolor="transparent",
            data_series=[
                ft.LineChartData(
                    data_points=[ft.LineChartDataPoint(x, y, selected=(x == 8)) for x, y in zip(x_values, green_line)],
                    color=ft.colors.GREEN,
                    stroke_width=1,
                    curved=True,
                    below_line_bgcolor=ft.colors.with_opacity(0.2, ft.colors.GREEN),
                ),
                ft.LineChartData(
                    data_points=[ft.LineChartDataPoint(x, y, selected=(x == 8)) for x, y in zip(x_values, red_line)],
                    color=ft.colors.RED,
                    stroke_width=1,
                    curved=True,
                    below_line_bgcolor=ft.colors.with_opacity(0.2, ft.colors.RED),
                )
            ],
            min_y=0,
            max_y=10,
            expand=True,
            border=ft.Border(
                bottom=ft.BorderSide(1, ft.colors.with_opacity(0.3, ft.colors.WHITE)),
                left=ft.BorderSide(1, ft.colors.with_opacity(0.3, ft.colors.WHITE))
            ),
            bottom_axis=bottom_axis,
            left_axis=left_axis,
        )

        self.row_2 = ft.Container(
            bgcolor= self.container2_color,
            border_radius=10,
            height=120,padding=10,
            content=ft.Column(
                        controls=[
                            ft.Row(
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    ft.Text("Diferencia"),
                                    ft.Text("$ 18,290", size=15, weight="bold"),
                                ]
                            ),
                            # grafica
                            self.chart_data
                        ]
                )
        )

        #Instanciamos las clases
        self.llamar_gastos = gastos.Clase_gastos(self) 
        self.llamar_ingresos = ingresos.Clase_ingresos(self)

        #Aqui se agregara el contenido de la parte inferior
        self.main_content = ft.Column([])
        self.btn_gastos = ft.ElevatedButton(text="Gastos", color=self.container2_color, bgcolor=self.container_color,
                                        style= ft.ButtonStyle(side=ft.BorderSide(1, self.container2_color), shape=ft.RoundedRectangleBorder(radius=10)),
                                        on_click=self.llamar_gastos.Gastos) #Mandamos a llamar la funcion gastos de la clase
        
        self.btn_ingresos = ft.ElevatedButton(text="Ingresos",color=self.container2_color, bgcolor=self.container_color,
                                          style=ft.ButtonStyle(side=ft.BorderSide(1, self.container2_color), shape=ft.RoundedRectangleBorder(radius=10)),
                                          on_click=self.llamar_ingresos.Ingresos)


        self.row_3 = ft.Container(
            height=30,
            border_radius=10,
            bgcolor=self.container_color,
            content=ft.Row(
                alignment= ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                ft.ElevatedButton(text="Todos", color=self.container2_color, bgcolor=self.container_color,
                                style = ft.ButtonStyle(side = ft.BorderSide(1, self.container2_color),
                                        shape=ft.RoundedRectangleBorder(radius=10) 
                                )                                
                                ),
                self.btn_ingresos,                
                self.btn_gastos
                
            ])
        )



        self.page.add(ft.Column(
            expand=True, scroll="auto",
            controls=[
                    self.header,
                    self.title,
                    self.row_1,
                    self.row_2,
                    self.row_3,
                    self.main_content
            ]
        ))

ft.app(target=SpendingApp)