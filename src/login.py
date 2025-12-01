import flet as ft
import db
from Pagina_principal import Pagina_principal

# --- Colores base ---
BG_COLOR = "#30304d"
CONTAINER_COLOR = "#23243d"
CONTAINER2_COLOR = "#484a66"


#Base -> No es view (Sirve para contener los widgets)
#IniciarSesion -> Es view y  hereda widgets
#Registro -> Es view y hereda widgets
class Base:
    def build_common_widgets(self):
        #Vamos a hacer la imagen circular
        self.logo = ft.Container(
            width=120, height=120, 
            border_radius=60, #La mitad del ancho circular
            clip_behavior = ft.ClipBehavior.ANTI_ALIAS, #hace que la imagen se recorte dentro del circulo
            content=ft.Image(src="assets/logo.jpeg", fit=ft.ImageFit.COVER), #Asegura que la imagen se ajuste bien
            alignment=ft.alignment.center   
        )
    
        self.nombre = ft.TextField(label="Nombre", width=300,
            label_style=ft.TextStyle(color="#D0E0D8"),
            text_style=ft.TextStyle(color=ft.Colors.WHITE))
        
        self.correo = ft.TextField(label="Correo", width=300, 
                label_style=ft.TextStyle(color="#D0E0D8"), 
                text_style=ft.TextStyle(color=ft.Colors.WHITE))
        

        self.contrasena = ft.TextField(label="Contrasena", 
                password=True, can_reveal_password=True, 
                width=300, label_style=ft.TextStyle(color="#D0E0D8"), 
                text_style=ft.TextStyle(color=ft.Colors.WHITE))
 

class IniciarSesion(ft.View, Base):
    def __init__(self, page):
        super().__init__(
            route="/",
            bgcolor=BG_COLOR,
            horizontal_alignment="center",
            vertical_alignment="center"
        )
        self.page = page

        #Widgets compartidos de las clases
        self.build_common_widgets()        

        self.boton_iniciarSesion = ft.ElevatedButton(
                text="Ingresar",
                color=ft.Colors.WHITE,
                bgcolor=CONTAINER_COLOR,
                width=200,
                height=45,
                style=ft.ButtonStyle(
                side=ft.BorderSide(1, CONTAINER2_COLOR),
                shape=ft.RoundedRectangleBorder(radius=5)
            ), on_click=self.clicked
        )
        


        self.text_button = ft.TextButton(
            text="No tienes cuenta. Crea una aqui",
            style=ft.ButtonStyle(color=CONTAINER2_COLOR),
            on_click= lambda e: self.page.go("/registro")
        )

        self.controls = [ft.Row(controls=[
            ft.Column(controls=[
                #Vamos a hacer la imagen circular
                self.logo,
                ft.Container(
                    content=ft.Text("Iniciar sesion", color=ft.Colors.WHITE, size=20, weight=ft.FontWeight.BOLD),
                    width=300,
                    alignment=ft.alignment.center
                ),
                self.correo, self.contrasena,
                ft.Container(content=self.boton_iniciarSesion, width=300, alignment=ft.alignment.center),
                ft.Container(content=self.text_button, width=300,alignment=ft.alignment.center)
            
            ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=15)
        ], vertical_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER, expand=True)]

    #data.user -> para acceder a los valores del metodo de la clase Database 
    def clicked(self, e):
        #Instancia a conexion a base de datos para verificar si existe el usuario
        data = db.Login()

        data.verificar_usuario(self.correo.value, self.contrasena.value) 
        #Si esta correcto te manda a la pagina principal, si no pues te lanza un alert dialog
        if  data.usuario: #usuario es el del cursor.fetchone
            self.page.go("/Pagina_principal")
        else:
            self.dlg_iniciarSesion = ft.AlertDialog(
                title=ft.Text("Error en los parametros", weight=ft.FontWeight.BOLD, text_align="center", color=ft.Colors.RED_300),
                content=ft.Container(width=300, height=100,content=ft.Text("Tu correo o contrasena son incorrectas, favor de volver a intentarlo", weight=ft.FontWeight.BOLD)),
                content_padding=20,
                elevation=50,
                actions=[
                    ft.TextButton("Aceptar", on_click=lambda e: self.page.close(self.dlg_iniciarSesion))
                ]
            )

            self.page.open(self.dlg_iniciarSesion)
            return #importante detener aqui la funcion
                 


class Registro(ft.View, Base):
    #Esta seccion de codigo verificara si la contrasena esta bien
    def verificar_contrasena(self,e):
        self.errores = []
        if len(self.contrasena.value) < 8 or len(self.contrasena.value) > 15:
            self.errores.append("La contraseña debe tener entre 8 y 15 caracteres.")

        if not any(c.isupper() for c in self.contrasena.value):
            self.errores.append("La contraseña debe contener al menos una letra mayúscula.")

        if not any(c.islower() for c in self.contrasena.value):
            self.errores.append("La contraseña debe contener al menos una letra minúscula.")

        if not any(c.isdigit() for c in self.contrasena.value):
            self.errores.append("La contraseña debe contener al menos un número.")

        if not any(c in "!@#$%&/" for c in self.contrasena.value):
            self.errores.append("La contraseña debe contener al menos uno de los siguientes caracteres especiales: !, @, #, $, %, &. /.")

        if len(self.errores) >= 1:
            contenido = ft.Column(controls=[
                ft.Text(f" {i}. {e}", weight=ft.FontWeight.BOLD, text_align="START") for i, e in enumerate(self.errores, start=1)
            ])

        
            self.dlg = ft.AlertDialog(
                title=ft.Text("Contrasena debil", text_align="center", weight=ft.FontWeight.BOLD, color=ft.Colors.RED_300),
                content=ft.Container(width=400, height=200,content=contenido),
                content_padding=20,
                elevation=50,
                actions=[
                    ft.TextButton("Aceptar", on_click=lambda e: self.page.close(self.dlg))
                ]
            )

            self.page.open(self.dlg)
            return #importante detener aqui la funcion
        
        #Si no hay errores ira a otra pagina - que sera la pagina principal
        data = db.Login()

        #Tenemos que ponerlo en una variable el resultado
        #porque si hacemos if data como lo estabamos haciendo devolvera true siempre porque hacemos referencia al objeto de la clase
        #no al resultado que tenemos
        resultado = data.crear_usuario(self.nombre.value, self.correo.value, self.contrasena.value)
        if resultado:
            self.page.go("/Pagina_principal")
        else:
            #Mostrar que su correo esta repetido!
            dlg = ft.AlertDialog(
                title=ft.Text("Correo inhabil", text_align="center", weight=ft.FontWeight.BOLD, color=ft.Colors.RED_300),
                content=ft.Container(width=400, height=100,content=ft.Text("Tu correo ya existe en nuestra base de datos", text_align="center")),
                content_padding=20,
                elevation=50,
            )
            self.page.open(dlg)
            self.page.update()
            
            self.page.go("/")
            return 

    def __init__(self, page):
        super().__init__(
            route="/registro",
            bgcolor=BG_COLOR,
            horizontal_alignment="center",
            vertical_alignment="center"
        )
        self.page = page
        self.build_common_widgets()

        self.regresar_inicio = ft.TextButton(
            text="Regresar",
            style=ft.ButtonStyle(color=CONTAINER2_COLOR),
            on_click= lambda e: self.page.go("/")
        )

        self.boton_registrarse = ft.ElevatedButton(
                text="Registrarse",
                color=ft.Colors.WHITE,
                bgcolor=CONTAINER_COLOR,
                width=200,
                height=45,
                style=ft.ButtonStyle(
                side=ft.BorderSide(1, CONTAINER2_COLOR),
                shape=ft.RoundedRectangleBorder(radius=5)
            ), on_click= self.verificar_contrasena
        )

        self.controls = [ft.Row(controls=[
            ft.Column(controls=[
                
                self.logo,
                ft.Container(
                    content=ft.Text("Registrarse", color=ft.Colors.WHITE, size=20, weight=ft.FontWeight.BOLD),
                    width=300,
                    alignment=ft.alignment.center
                ),
                self.nombre, self.correo, self.contrasena, self.boton_registrarse,
                self.regresar_inicio
             
            
            ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=15)
        ], vertical_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER, expand=True)]
