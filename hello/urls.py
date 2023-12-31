from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"), # "" este string vacio hace referencia a una url sin argumentos, es decir sin nada al final
    path("<str:name>", views.greet, name="greet"),
    path("brian", views.brian, name="brian")
]