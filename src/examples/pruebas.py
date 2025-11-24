import flet as ft

def main(page: ft.Page):
    page.title = "Container Expandible con Flecha"
    page.bgcolor = "white"
    # Estado del contenedor expandido o no
    expandido = False

    # Contenedor con altura animada
    contenedor = ft.Container(
        content=ft.Text("Contenido desplegable aquí"),
        width=300,
        height=0,  # Altura inicial
        bgcolor=ft.colors.BLACK,
        animate=ft.Animation(300, "easeInOut"),
        padding=10,
        border_radius=10,
        alignment=ft.alignment.top_center,
    )

    # Icono de flecha
    flecha = ft.IconButton(
        icon=ft.icons.KEYBOARD_ARROW_DOWN,
        on_click=lambda e: toggle_expandir()
    )

    # Función para alternar expansión
    def toggle_expandir():
        nonlocal expandido
        expandido = not expandido

        # Cambiar icono de la flecha y altura
        if expandido:
            flecha.icon= ft.icons.KEYBOARD_ARROW_UP
            contenedor.height = 100  # Altura expandida
        else:
            flecha.icon = ft.icons.KEYBOARD_ARROW_DOWN
            contenedor.height = 0  # Altura contraída

        page.update()

    # Agregar a la página
    page.add(
        flecha,
        contenedor
    )

ft.app(target=main)


#2
"""import flet as ft

def main(page: ft.Page):
    page.title = "Container Desplegable"
    page.bgcolor = "white"
    # Contenido que se va a mostrar/ocultar
    contenido = ft.Container(
        content=ft.Text("Este es el contenido desplegable"),
        padding=10,
        bgcolor=ft.colors.BLACK,
        border_radius=5,
        visible=False  # Oculto inicialmente
    )

    # Función para alternar visibilidad
    def toggle_contenido(e):
        contenido.visible = not contenido.visible
        page.update()

    # Botón para mostrar/ocultar el contenedor
    boton_toggle = ft.ElevatedButton(
        text="Mostrar/Ocultar",
        on_click=toggle_contenido
    )

    # Agregar elementos a la página
    page.add(
        boton_toggle,
        contenido
    )

ft.app(target=main)"""