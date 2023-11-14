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
