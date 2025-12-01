import flet as ft

#TODO: VER LO DE PAGINA PRINCIPAL PARA MOSTRAR LOS INGRESOS
#ESTA EN CHATGPT

class ListaIngresos():
    #Vamos a recibir la lista de ingresos cada que creemos un objeto de la clase
    def __init__(self, lista_ingresos):
        self.lista_ingresos = lista_ingresos
    
    #Clase para construir, osea construccion de widgets
    def build(self):
        column = ft.Column(spacing=5)
        
        self.flecha = ft.IconButton(
            icon=ft.Icons.KEYBOARD_ARROW_DOWN,
            icon_color="white",
            on_click=self.toggle_expandir
        )
        for i, (monto, fecha, tipo) in enumerate(self.lista_ingresos, start=0):
            item = ft.Container(
                padding=10,
                border=ft.border.all(1, "white"),
                content=ft.Column([
                    ft.Text(f"Ingreso {i}: ${monto}"),
                    ft.Text(f"Fecha: {fecha}")
                ])
            )
            column.controls.append(item)

        return column
    
    def toggle_expandir(self, e):
        self.expandido = not self.expandido
        self.flecha.icon = (
            ft.Icons.KEYBOARD_ARROW_UP if self.expandido else ft.Icons.KEYBOARD_ARROW_DOWN
        )

        self.detalle_column.visible = self.expandido
        self.container.height = 10 if self.expandido else 50
        self.update()