from django.urls import path,include
from . import views 
urlpatterns = [
    path("",views.home,name="homepage"),
    path("projects/",views.projects,name="projects"),
    path("contact/",views.contact,name="contact"),
]
