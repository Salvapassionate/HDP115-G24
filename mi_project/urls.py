"""mi_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from my_app import views
from my_app.views import mostrar_estadisticas
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', mostrar_estadisticas, name='mostrar_estadisticas'),
    url(r'^index/$', views.index, name='index'),
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),

   
    url('^registrar_estadistica', views.registrar_estadistica),
    url('^edicion_etadistica/<nombre>/$', views.edicion_estadistica),
    url('^editar_estadistica', views.editar_estadistica),
    url('^eliminar_estadistica/<nombre>/$', views.eliminar_estadistica),

    url(r'^$', views.sistema, name='sistema'),
    url('^login/$', views.login_view, name='login'),
    url(r'^register/$', views.register, name='register'),
    url('logout/', views.sistema, name='logout'),
    

    

]
