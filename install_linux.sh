#!/bin/bash

# Actualiza los paquetes
sudo apt update

# Instalar MySQL y SQLite3
sudo apt install mysql-client sqlite3 python3-pip -y

# Instalar dependencias de Python
pip3 install -r requirements.txt

echo "Instalación completada con éxito. Ahora puedes ejecutar el script con 'python3 main.py'."
