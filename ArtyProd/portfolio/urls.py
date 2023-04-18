from django.urls import path
from . import views

urlpatterns = [
    path('',views.portfolio , name='portfolio'),
    path('project/<str:pk>',views.project, name='project'),
    path('request/',views.req_project, name='req_project'),
]
