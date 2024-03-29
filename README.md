# Reseñas Cool con Django
### 2023-1-Grupo-3
#### Pedro Astaburuaga - Valeria Gutiérrez - Kathleen Kohler - Demian Hott - Cristóbal Suazo

Reseñas Cool es una aplicación web desarrollada con Django que permite a los usuarios crear, ver, modificar, puntuar y borrar reseñas de productos, además de agregar comentarios a las mismas. Además, incluye un sistema de autenticación para permitir a los usuarios crear y gestionar sus propias reseñas, así como ver las reseñas de otros usuarios.

## Características

* Creación de nuevas reseñas por usuarios autenticados.
* Visualización individual de reseñas.
* Visualización agrupada de reseñas por última fecha de creación.
* Filtrar reseñas por categoría y usuarios.
* Modificación y eliminación de reseñas existentes por el usuario autor de la reseña.
* Asociación de reseñas a categorías predefinidas.
* Sistema de autenticación de usuarios.
* Valoración de reseñas.
* Agregar, modificar y borrar comentarios a las reseñas.

## Modelo de Datos

Los usuarios se trabajan con el modelo predefinido de Django Users, principalmente se usan los atributos id, username, password y email. Las reseñas, categorías, valoraciones y comentarios se modelan de la siguiente forma:

### Reseñas

Representa la reseña del producto creada por un usuario autenticado. Tiene los siguientes atributos: 

* Id
* Nombre del producto
* Título de la reseña
* Descripción de la reseña
* Foto del producto
* Fecha de creación
* Categoría
* Usuario creador

### Categorías

Instancias predefinidas para clasificar las reseñas creadas. Tiene los siguientes atributos:

* Id
* Nombre de la categoría

### Valoraciones

Cruce entre usuario y reseña que representa una valoración positiva del usuario por la reseña. La suma de todas
las valoraciones de una reseña particular, representa la valoración total de la reseña. Tiene los siguientes
atributos:

* Id
* Usuario valorador
* Reseña valorada

### Comentarios

Representa el comentario que un usuario agrega a una reseña. Tiene los siguientes atributos:

* Id
* Usuario comentador
* Reseña comentada
* Contenido del comentario

## Requisitos

Para correr la aplicación se necesitan las siguientes versiones de programas:

* Python 3.10.3
* Django 4.2

## Instalación

Para instalar y correr la aplicación, se deben seguir los siguientes pasos:

1. Clonar el repositorio

2. Crear un ambiente virtual fuera del directorio de la aplicación con `python -m venv myvenv`

3. Activar el ambiente virtual con `. myvenv\Scripts\activate`

4. Dentro del ambiente viertual, instalar las librerías necesarias para la aplicación, ejecutando `pip install -r requirements.txt`

5. Ejecutar las migraciones de la base de datos con el siguiente comando: `python manage.py makemigrations` y luego, `python manage.py migrate`

6. Correr el servidor con el siguiente comando `python manage.py runserver`

7. Finalmente, abrir un navegador e ir a la dirección indicada por el comando `runserver` ejecutado

## Uso

Para visualizar un ejemplo de uso de la aplicación se deben seguir los siguientes pasos:

1. Crear una cuenta de usuario e iniciar sesión con ella

2. Crear una nueva reseña desde la página principal

3. Modificar o eliminar reseñas creadas

4. Visualizar reseñas creadas por otros usuarios

5. Mostrar en detalle la reseña de otro usuario y valorarla

6. Agregar un comentario en dicha reseña, modificarlo y borrarlo




