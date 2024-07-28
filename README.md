# Tercera pre-entrega Barroca

Proyecto realizado en Coderhouse para la tercera pre-entrega del curso Python

Proyecto de pagina web en la cual se pueden cargar datos por medio de formularios, datos los cuales se almacenan en una base de datos. tambien se puede acceder a estos datos mediante los buscadores y desde "AdminDjango"

## Instalaciones necesarias

•	```Python``` (mi versión es 3.12.4)

•	```Visual Studio Code```

#### Extensiones instaladas en Visual Studio Code:

•	```SQLite```

•	```SQLite Viewer```

•	```Djaneiro```

## Uso y ejecución

1-	Descargar el archivo  de [GitHub](https://github.com/Sebarroca/Tercera-pre-entrega-Barroca) 

2-	Arrastrar la carpeta a una nueva ventana de Visual Studio Code

3-	Abrir la terminal con Ctrl+C

4-	Ingresar en la terminal el comando: ```python -m pip install Django==5.0.6``` - Instala Django

5-	Ingresar en la terminal el comando : ```python manage.py runserver```  - Ejecuta el servidor

6-	Ingresar al puerto que figure (http://127.0.0.1:8000/) para ingresar a la página



•	Una vez que se ingrese a la página, se puede ir a las pestañas mencionadas an continuación para cargar los datos que se requieran. 

•	El inicio ya cuenta con datos generados a modo de guía, y también figurarán los cargados posteriormente.

## Características de la web


```Inicio```: Vista principal. Figuran los datos cargados en las pestañas de Cursos, Estudiantes y Profesores. A su vez se pueden buscar estos datos  individualmente en los buscadores que están presentes en el Inicio .

```Cursos```: pestaña en la cual hay un formulario para ingresar el nombre del curso y el número de la comisión.

```Estudiantes```: pestaña en la cual hay un formulario para ingresar el nombre, apellido, curso y dirección de correo electrónico de los estudiantes.

```Profesores```: pestaña en la cual hay un formulario para ingresar el nombre, apellido, dirección de correo electrónico y la especialidad de los profesores.

```Admin```: pestaña que accede a la base de datos, creando un usuario con una contraseña.

•	Para acceder a “Admin” se deberá crear un “Super Usuario” con el comando ```python manage.py createsuperuser``` el cual solicita nombre de usuario y contraseña
