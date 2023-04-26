# 2023-1-Grupo-3
## Primer commit 25-04
python -m venv myvenv (crear ambiente virtual)

. myvenv\Scripts\activate (activar ambiente virtual)

pip install -r requirements.txt (instalar librerias, con el ambiente virtual activado)

python manage.py startapp [nombre_de_app]  (crear una app dentro de la carpeta del proyecto, con el ambiente virtual activado)

Correr el proyecto
python manage.py makemigrations
python manage.py migrate 
python manage.py runserver