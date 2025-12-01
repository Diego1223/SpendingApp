import mysql.connector

from json_manager import guardar_sesion, cargar_sesion

CONFIG = {
    "host":"localhost",
    "user":"root",
    "password":"tuclave",
    "database":"spendingApp",
    "auth_plugin":"mysql_native_password"   
}
#Las primeras tablas que hare es de login
#id, nombre, correo y contrasena (correo unique)


class Database:
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(**CONFIG)
            self.cursor = self.conexion.cursor()
        except:
            print("Error base de datos")

    
class Login(Database):
    def __init__(self):
        super().__init__()

    def verificar_usuario(self, nombre:str, contrasena: str) -> bool:
        query = "SELECT id, nombre FROM usuarios WHERE nombre = %s AND contrasena = %s"
        parametros= (nombre, contrasena)
        self.cursor.execute(query, parametros)
        #Guardar los resultados
        self.usuario = self.cursor.fetchone()
        if self.usuario:
            self.user_id, self.nombre_usuario = self.usuario
            #persistencia en el inicio de sesion
            guardar_sesion({
                "user_id":self.user_id,
                "nombre":self.nombre_usuario,
                "is_logged":True
            })
            return True
        else:
            return False
    

    def crear_usuario(self, nombre: str, correo: str, contrasena: str) -> bool:
        try:
            query = "INSERT INTO usuarios (nombre, correo, contrasena) VALUES (%s, %s, %s)"
            parametros = (nombre, correo, contrasena)

            self.cursor.execute(query, parametros)
            self.conexion.commit()

            #Persistencia
            query2 = "SELECT id FROM usuarios WHERE correo = %s"
            parametro  = (correo,)
            self.cursor.execute(query2, parametro)
            user_id = self.cursor.fetchone()

            #Lo guardamos en el archivo json
            guardar_sesion({
                "user_id": user_id,
                "nombre": nombre,
                "is_logged":True
            })
        
        
            return True 
        #Captura errores unique
        except mysql.connector.errors.IntegrityError as er:
            print(f"Error unique")
            return False
        

class Movimientos(Database):
    def __init__(self):
        super().__init__()

        
    def mostrar_ingreso(self):
        sesion = cargar_sesion()
        self.user_id = sesion.get("user_id") #Si no existe solo devuelve None

        #SUM es para sumar los ingresos (total de ingresos)
        query = "SELECT SUM(monto) FROM movimientos WHERE usuario_id = %s AND tipo = 'ingreso'"
        parametro = (self.user_id)

        self.cursor.execute(query, parametro)
        ingreso = self.cursor.fetchone()[0] #-> [0] Es una tupla, por eso se accede asi
        return ingreso

    def mostrar_egresos(self):
        sesion = cargar_sesion()
        self.user_id = sesion.get("user_id") #Si no existe solo devuelve None

        #SUM es para sumar los ingresos (total de ingresos)
        query = "SELECT SUM(monto) FROM movimientos WHERE usuario_id = %s AND tipo = 'egreso'"
        parametro = (self.user_id)

        self.cursor.execute(query, parametro)
        egreso = self.cursor.fetchone()[0] #-> [0] Es una tupla, por eso se accede asi
        return egreso
    

    def obtener_ingresos(self):
        query = """
            SELECT monto, fecha, tipo
            FROM movimientos
            WHERE usuario_id = %s AND tipo = 'ingreso'
            ORDER BY fecha ASC
            """     
        
        self.cursor.execute(query, (self.user_id))
        resultados = self.cursor.fetchall()

        #los resultados los recibimos asi: (lista de tuplas)
        #[(1200, '2025-01-05'), (1500, '2025-01-12')]
        return resultados
    

