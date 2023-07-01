"""
URL configuration for resenas_cool project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from inicio import views as views_i
from resenas import views as views_r
from usuarios import views
from django.urls import path
from django.contrib import admin
import sys
import os

sys.path.append(os.path.join(os.path.dirname('views.py'), 'usuarios'))
sys.path.append(os.path.join(os.path.dirname('views.py'), 'resenas'))
sys.path.append(os.path.join(os.path.dirname('views.py'), 'comentarios'))


from django.contrib import admin
from django.urls import path
from usuarios import views
from resenas import views as views_r
from inicio import views as views_i
from comentarios import views as views_c
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    #modifiqué el metodo al cual llama la vista
    path('login', views.ingreso, name = 'login'),
    path('register', views.register, name = 'register'),
    path('nueva_resena', views_r.nueva_resena, name = 'nueva_resena'),
    path('mostrar_resena/<int:review_id>/', views_r.mostrar_resena, name = 'mostrar_resena'),
    path('borrar/<int:review_id>/', views_r.borrar, name = 'borrar'),
    path('modificar_resena/<int:review_id>/', views_r.modificar_resena, name = 'modificar_resena'),
    path('', views_i.ver_resenas, name = 'ver_resenas'),
    path('ver_resenas', views_i.ver_resenas, name = 'ver_resenas'),
    path('ver_resenas/cat=<str:categoria>/usr=<str:usuario>', views_i.ver_resenas, name='ver_resenas'),
    path('ver_resenas/cat=<str:categoria>', views_i.ver_resenas, name='ver_resenas'),
    path('ver_resenas/usr=<str:usuario>', views_i.ver_resenas, name='ver_resenas'),
    path('nuevo_comentario/<int:review_id>/', views_c.nuevo_comentario, name = 'nuevo_comentario'),
    path('modificar_comentario/<int:comment_id>/', views_c.modificar_comentario, name = 'modificar_comentario'),
    path('borrar_comentario/<int:comment_id>/', views_c.borrar_comentario, name = 'borrar_comentario'),
    path('logout', views_i.logout_view, name='logout')
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

