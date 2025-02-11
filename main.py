import os
import mysql.connector
import sqlite3

def export_mysql_to_sqlite(mysql_db_name, sqlite_db_name):
    # Establecer conexión a MySQL
    try:
        mysql_conn = mysql.connector.connect(
            host='localhost',
            user='root',  # Asumiendo que el usuario es root. Cambia si es necesario.
            password='password',  # Cambia con la contraseña correspondiente
            database=mysql_db_name
        )
        cursor = mysql_conn.cursor()

        # Crear base de datos SQLite
        sqlite_conn = sqlite3.connect(sqlite_db_name)
        sqlite_cursor = sqlite_conn.cursor()

        # Exportar las tablas de MySQL
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()

        for table in tables:
            table_name = table[0]
            cursor.execute(f"SELECT * FROM {table_name}")
            rows = cursor.fetchall()

            # Crear tabla en SQLite
            cursor.execute(f"SHOW CREATE TABLE {table_name}")
            create_table_query = cursor.fetchone()[1]
            create_table_query = create_table_query.replace("ENGINE=InnoDB", "")
            sqlite_cursor.execute(create_table_query)

            # Insertar los datos
            for row in rows:
                placeholders = ', '.join(['?' for _ in range(len(row))])
                sqlite_cursor.execute(f"INSERT INTO {table_name} VALUES ({placeholders})", row)

            sqlite_conn.commit()

        # Cerrar conexiones
        sqlite_conn.close()
        mysql_conn.close()
        print(f"Base de datos {sqlite_db_name} restaurada correctamente.")
    except Exception as e:
        print(f"Error: {e}")
    
def main():
    # Buscar el archivo SQL
    sql_file = None
    for file in os.listdir():
        if file.endswith('.sql'):
            sql_file = file
            break

    if not sql_file:
        print("No se encontró un archivo .sql en el directorio.")
        return

    print(f"Archivo encontrado: {sql_file}")

    # Solicitar nombre para la base de datos en MySQL
    mysql_db_name = input("Ingresa el nombre de la base de datos de MySQL: ")

    # Preguntar nombre de la base de datos SQLite
    sqlite_db_name = input("Ingresa el nombre para la base de datos SQLite (sin la extensión): ") + ".db"

    # Realizar el proceso de exportación
    export_mysql_to_sqlite(mysql_db_name, sqlite_db_name)

if __name__ == "__main__":
    main()
