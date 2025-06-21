"""
URL configuration for recipe_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from vege.views import *
from vege import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings  # Import settings module
from django.conf.urls.static import static  # Import static function


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('showdata/',views.showdata,name='showdata'),
    path('login/',views.login_page,name="login"),
    path('register/',views.register_page,name="register"),
    path('logout/',views.logout_page,name='logout'),
    path('student/',views.get_students,name='student'),
    # path('see_marks/int:<student_id>/',views.see_marks,name='see_marks'),
    path('see_marks/<student_id>/',views.see_marks,name='see_marks'),
]