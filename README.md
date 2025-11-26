# SpendingApp (Flet, MySQL, python)

La aplicacion es basicamente un software para manejar ingresos y egresos.Es una aplicacion recreada pero con funcionalidad, tiene login funcional, validacion de contrasena segura, se usa con una base de datos relacion MySQL, inicio de sesion, registro y tratamiento de excepciones.

Cada que un usuario inicia sesion o se registra se crea un archivo json el cual se consulta cada que se ejecuta la aplicacion;
si esta creado se manda a la pagina principal, si no hay archivo directamente al login


## Funcionalidades nuevas
- Login (Inicio sesion y registro con validacion de contrasenas)
- Base de datos para guardar y verificar usuarios
- No se puede registrar mas de una vez un correo electronico (campo UNIQUE)
- Tratamiento de excepciones y contrasena segura 

## ENUM MySQL
- Solo puede contener valores seleccinados
```SQL
CREATE TABLE movimientos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    tipo ENUM('ingreso', 'egreso') NOT NULL,
    categoria VARCHAR(100),
    descripcion TEXT,
    monto DECIMAL(10,2) NOT NULL,
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP
);
```


# Creditos

Esta aplicacion es inspirada en el codigo de @MagnoEfren, con nuevas funcionalidades, diferentes directorios, pero sigue el paradigma orientado a objetos con el que fue escrito principalmente




