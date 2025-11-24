import mysql.connector

CONFIG = {
    "host":"localhost",
    "user":"root",
    "password":"tuclave",
    "database":"spendingApp",
    "auth_plugin":"mysql_native_password"   
}
#Las primeras tablas que hare es de login
#id, nombre, correo y contrasena (correo unique)

#TODO -> HACER QUE si el correo existe, mostrar un mensaje

class Database:
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(**CONFIG)
            self.cursor = self.conexion.cursor()
        except:
            print("Error base de datos")

    
    def verificar_usuario(self, nombre:str, contrasena: str) -> bool:
        query = "SELECT id, nombre FROM usuarios WHERE nombre = %s AND contrasena = %s"
        parametros= (nombre, contrasena)
        self.cursor.execute(query, parametros)
        #Guardar los resultados
        self.usuario = self.cursor.fetchone()
        if self.usuario:
            self.user_id, self.nombre_usuario = self.usuario
            return True
        else:
            return False
    

    def crear_usuario(self, nombre: str, correo: str, contrasena: str) -> bool:
        try:
            query = "INSERT INTO usuarios (nombre, correo, contrasena) VALUES (%s, %s, %s)"
            parametros = (nombre, correo, contrasena)

            self.cursor.execute(query, parametros)
            self.conexion.commit()

            print("Verificado")
        #Captura errores unique
        except mysql.connector.errors.IntegrityError as er:
            print(f"Error unique")

