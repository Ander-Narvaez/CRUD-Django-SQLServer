# CRUD-Django-SQLServer

Este es un pequeño proyecto de Django para demostrar la funcionalidad CRUD de Django, que te que permite crear, mostrar, actualizar y eliminar datos, usando SQL Server como motor de base de datos para la realización de las consultas DML.

# Tecnologías utilizadas:
- Django
- Bootstrap v5.2
- JavaScript

## Instalar paquetes requeridos 

Para que se ejecute en su máquina local, siga los pasos a continuación
```
    git clone https://github.com/Ander-Narvaez/CRUD-Django-SQLServer.git
```    
    Cambie settings.py SQL CONFIGURATIONS (name, user, password)
```    
    pip install -r requirements.txt
 
 ## Ejecución de la aplicación
 
Antes de ejecutar la aplicación necesitamos crear las tablas de base de datos mediante el modelo ORM:

    python manage.py migrate

Ahora puede ejecutar el servidor web de desarrollo:

    python manage.py runserver

Para acceder a las aplicaciones vaya a la URL: http://127.0.0.1:8000

## Necesito un usuario y contraseña para acceder a la aplicación

Esto porque el app esta para que cuando arranque redireccione al login de manera que solo 
se puede acceder a la app teniendo un user y password, debido a que cada ruta esta protegida
con el decorador de login_required, para que el usario puede hacer login y logout.

Puede crear un usuario utilizando el siguiente comando:

    python manage.py createsuperuser
    
Nota: Le solicitara lo siguiente: (enter username, email, password)

Para crear un usuario normal (no superusuario), debe iniciar sesión en la página de administración y crearla: http://localhost:8000/admin/

Desarrollador  ✒️
------------------
| Primer Apellido | Segundo Apellido | Nombre | sitios 📌  |
| :-------- | :-------: | --------: | :-------: |
| Narvaez | Gonzalez | Ander | https://github.com/Ander-Narvaez |


