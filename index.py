import mysql.connector

# Configuración de la conexión a la base de datos
conexion = mysql.connector.connect(
    host="tu_host",
    user="tu_usuario",
    password="tu_contraseña",
    database="tu_base_de_datos"
)

# Crear un cursor para ejecutar consultas SQL
cursor = conexion.cursor()

# Operación CREATE (Crear)
def crear_usuario(nombre, edad):
    consulta = "INSERT INTO usuarios (nombre, edad) VALUES (%s, %s)"
    valores = (nombre, edad)
    cursor.execute(consulta, valores)
    conexion.commit()
    print("Usuario creado con éxito")


# Operación READ (Leer)
def leer_usuarios():
    consulta = "SELECT * FROM usuarios"
    cursor.execute(consulta)
    usuarios = cursor.fetchall()
    for usuario in usuarios:
        print(usuario)


# Operación UPDATE (Actualizar)
def actualizar_usuario(id_usuario, nuevo_nombre):
    consulta = "UPDATE usuarios SET nombre = %s WHERE id = %s"
    valores = (nuevo_nombre, id_usuario)
    cursor.execute(consulta, valores)
    conexion.commit()
    print("Usuario actualizado con éxito")
    
    
# Operación DELETE (Eliminar)
def eliminar_usuario(id_usuario):
    consulta = "DELETE FROM usuarios WHERE id = %s"
    valores = (id_usuario,)
    cursor.execute(consulta, valores)
    conexion.commit()
    print("Usuario eliminado con éxito")
    
    
# Ejemplos de uso
crear_usuario("Juan", 25)
crear_usuario("Ana", 30)    
leer_usuarios()
actualizar_usuario(1, "Juan Pérez")
leer_usuarios()
eliminar_usuario(2)
