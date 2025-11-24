import flet as ft

def main(page: ft.Page):
    page.title = "App con Views"
    page.theme_mode = "dark"
    page.on_route_change = lambda e: route_change(page)
    
    page.go("/login")


# ================
# VISTA LOGIN
# ================
def login_view(page: ft.Page):
    correo = ft.TextField(label="Correo", width=300)
    self.contrasena = ft.TextField(label="Contraseña", password=True, width=300)

    pagina_inicio = ft.Container(
        expand=True,                              # <-- aquí EXPANDE
        alignment=ft.alignment.center,
        content=ft.Column(
            controls=[
                ft.Text(
                    "Diego",
                    size=30,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE
                ),
                correo,
                contrasena,
                ft.ElevatedButton("Entrar", on_click=lambda e: page.go("/inicio"))
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )

    return ft.View(
        "/login",
        controls=[pagina_inicio],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )


# ================
# VISTA INICIO
# ================
def inicio_view(page: ft.Page):
    return ft.View(
        "/inicio",
        controls=[
            ft.Container(
                expand=True,
                alignment=ft.alignment.center,
                content=ft.Text("Bienvenido Diego 🎉", size=40)
            )
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )


# ================
# CAMBIO DE RUTAS
# ================
def route_change(page: ft.Page):
    page.views.clear()

    if page.route == "/login":
        page.views.append(login_view(page))

    elif page.route == "/inicio":
        page.views.append(inicio_view(page))

    page.update()


ft.app(main)
