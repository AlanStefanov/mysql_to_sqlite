# MySQL a SQLite

Este proyecto permite migrar una base de datos MySQL a una base de datos SQLite de forma sencilla mediante un script en Python. Es útil cuando necesitas convertir bases de datos grandes de MySQL a un formato más ligero y portátil como SQLite.

## Requisitos

- Python 3
- MySQL
- SQLite3

## Instalación

### En macOS

1. Clona este repositorio.
2. Ejecuta el siguiente comando para instalar las dependencias necesarias:

    ```bash
    bash install_mac.sh
    ```

3. Una vez completada la instalación, puedes ejecutar el script con:

    ```bash
    python3 main.py
    ```

### En Linux

1. Clona este repositorio.
2. Ejecuta el siguiente comando para instalar las dependencias necesarias:

    ```bash
    bash install_linux.sh
    ```

3. Una vez completada la instalación, puedes ejecutar el script con:

    ```bash
    python3 main.py
    ```

## Uso

1. Coloca tu archivo `.sql` de MySQL en el directorio raíz del proyecto.
2. Ejecuta el script con:

    ```bash
    python3 main.py
    ```

3. El script te pedirá que ingreses el nombre de la base de datos MySQL y el nombre que deseas para la base de datos SQLite.
4. El proceso de migración comenzará y tu base de datos SQLite estará lista.

## Contribuciones

Si deseas contribuir a este proyecto, abre un Pull Request o crea un Issue si encuentras algún problema.

## Acerca de mí

Hola, soy **Alan Stefanov**, un entusiasta de la tecnología con experiencia en desarrollo de software. Si te ha gustado este proyecto o si tienes alguna pregunta, no dudes en contactarme.

- [Mi LinkedIn](https://www.linkedin.com/in/alanstefanov/)
- [Mi GitHub](https://github.com/AlanStefanov/)

## Licencia

Este proyecto está bajo la Licencia MIT.
