#!/bin/bash

# Actualiza Homebrew
brew update

# Instalar MySQL y SQLite3
brew install mysql sqlite

# Instalar Python y pip si no están instalados
brew install python

# Instalar dependencias de Python
pip3 install -r requirements.txt

echo "Instalación completada con éxito. Ahora puedes ejecutar el script con 'python3 main.py'."
